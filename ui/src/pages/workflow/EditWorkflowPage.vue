<template>
  <div>
    <v-container v-if="initialized">
      <v-row>
        <v-col justify="between" align="between">
          <h3 class="font-bold">
            Workflow
            <!-- <v-chip>{{ workflow.identifier }}</v-chip> -->
          </h3>
        </v-col>
        <!-- <v-col justify="center" align="end">
          <v-btn class="mr-5" :disabled="transitions.length == 0" color="primary" @click="goToEditWorkflowRules">Edit
            Workflow Rules</v-btn>
        </v-col> -->
      </v-row>
      <v-row>
        <v-col cols="12">
          <WorkflowIllustration
            :states="states"
            :transitions="transitions"
            :state_class_mapping="state_class_mapping"
            :editable="true"
            @on-transition-selected="onTransitionSelected"
            @on-state-clicked="onStateSelected"
            @refetch="refetch"
          />
        </v-col>
      </v-row>
      <div class="flex items-center gap-4">
        <div class="flex items-start justify-start gap-3 pt-2 flex-nowrap">
          <div class="max-w-[500px] w-full">
            <StateInput
              :disabled="!selected_state"
              v-model="new_transition_state"
              class="mb-0"
              :placeholder="
                selected_state
                  ? `New state from '${selected_state.label}':`
                  : 'Select a state to create a transition'
              "
            />
          </div>
          <div>
            <v-btn
              class="mt-2 rounded-full"
              :disabled="!selected_state || !new_transition_state"
              large
              color="primary"
              @click="createState"
            >
              <svg
                width="17"
                height="17"
                viewBox="0 0 17 17"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M8.50004 15.25C12.1819 15.25 15.1667 12.2653 15.1667 8.58335C15.1667 4.90146 12.1819 1.91669 8.50004 1.91669C4.81814 1.91669 1.83337 4.90146 1.83337 8.58335C1.83337 12.2653 4.81814 15.25 8.50004 15.25Z"
                  stroke="white"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M8.5 5.91669V11.25"
                  stroke="white"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M5.83337 8.58337H11.1667"
                  stroke="white"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <span class="font-bold capitalize">
                Add state
              </span>
            </v-btn>
          </div>
        </div>
        <div class="flex items-start justify-start gap-3 pt-2 flex-nowrap">
          <div class="max-w-[500px] w-full">
            <v-text-field
              class="pt-0 mt-0"
              :disabled="!new_transition_name && new_transition_name !== ''"
              v-model="new_transition_name"
              :placeholder="'Enter transition name'"
            />
          </div>
          <div>
            <v-btn
              class="mt-1 rounded-full"
              :disabled="!selected_transition || !new_transition_name"
              large
              color="primary"
              @click="updateTransitionName"
            >
              <svg
                width="16"
                height="16"
                viewBox="0 0 16 16"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <g clip-path="url(#clip0_24_1831)">
                  <path
                    d="M11.334 2.00004C11.5091 1.82494 11.7169 1.68605 11.9457 1.59129C12.1745 1.49653 12.4197 1.44775 12.6673 1.44775C12.9149 1.44775 13.1601 1.49653 13.3889 1.59129C13.6177 1.68605 13.8256 1.82494 14.0007 2.00004C14.1757 2.17513 14.3146 2.383 14.4094 2.61178C14.5042 2.84055 14.5529 3.08575 14.5529 3.33337C14.5529 3.58099 14.5042 3.82619 14.4094 4.05497C14.3146 4.28374 14.1757 4.49161 14.0007 4.66671L5.00065 13.6667L1.33398 14.6667L2.33398 11L11.334 2.00004Z"
                    stroke="white"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </g>
                <defs>
                  <clipPath id="clip0_24_1831">
                    <rect width="16" height="16" fill="white" />
                  </clipPath>
                </defs>
              </svg>
              <span class="font-bold capitalize">
                Edit name
              </span>
            </v-btn>
          </div>
        </div>
      </div>
    </v-container>
  </div>
</template>

<script>
import StateInput from "@/components/StateInput.vue";
import WorkflowIllustration from "@/components/WorkflowIllustration.vue";
import { emit_success } from "@/helpers/event_bus";
import http from "@/helpers/http";
import { State, Transition, Workflow } from "@/models/models";

export default {
  name: "CreateWorkflowPage",
  components: {
    WorkflowIllustration,
    StateInput,
  },
  data: () => ({
    workflow: null,
    initialized: false,
    selected_transition: null,
    states: [],
    transitions: [],
    transition_approvals: {},
    selected_state: null,
    new_transition_state: null,
    new_transition_name: null,
    state_class_mapping: {},
    selected_state_class: {
      rect: {
        fill: "black",
      },
      label: {
        stroke: "black",
      },
    },
    default_state_class: {
      rect: {
        fill: "black",
      },
      label: {
        stroke: "",
      },
    },
  }),
  mounted() {
    this.refetch();
  },
  methods: {
    refetch() {
      var workflow_id = this.$route.params.id;
      this.workflow = http.get(`/workflow/get/${workflow_id}/`, (result) => {
        this.workflow = Workflow.of(
          result.data.id,
          result.data.content_type,
          result.data.initial_state,
          result.data.field_name
        );

        var state_fetcher = http.get(
          `/workflow/state/list/${workflow_id}/`,
          (result) => {
            this.states = result.data.map((state) =>
              State.of(state.id, state.label).of_description(state.description)
            );
          }
        );

        var transition_meta_fetcher = http.get(
          `/workflow/transition-meta/list/${workflow_id}/`,
          (result) => {
            this.transitions = result.data
              .map((transition) =>
                Transition.of(
                  transition.id,
                  this.workflow,
                  transition.source_state,
                  transition.destination_state,
                  transition.name
                )
              )
              .sort((a, b) => a.id - b.id);
          }
        );

        Promise.all([state_fetcher, transition_meta_fetcher]).then(() => {
          this.initialized = true;

          var selected_state = JSON.parse(
            this.$route.query.selected_state || null
          );
          if (selected_state) {
            this._selected_state(selected_state);
          }
        });
      });
    },
    onStateSelected(state) {
      this._selected_state(state);
    },
    _selected_state(state) {
      if (this.selected_state) {
        this.$set(
          this.state_class_mapping,
          this.selected_state.id,
          this.default_state_class
        );
      }
      this.$set(this.state_class_mapping, state.id, this.selected_state_class);

      this.selected_state = state;

      this.updateQuery({
        selected_state: JSON.stringify(this.selected_state),
      });
    },
    createState() {
      if (this.new_transition_state) {
        var promise = Promise.resolve();
        var is_state_created = false;
        if (this.new_transition_state.is_new) {
          promise = http.post(
            "/state/create/",
            this.new_transition_state.to_create_request(),
            (response) => {
              is_state_created = true;
              this.new_transition_state.is_new = false;
              this.new_transition_state.id = response.data.id;
              this.new_transition_state.final_label = this.new_transition_state.label;
            }
          );
        }
        promise.then((response) => {
          var parent = this.states.find(
            (state) => state.id == this.selected_state.id
          );
          var new_transition = Transition.create(
            this.workflow,
            parent.id,
            this.new_transition_state.id
          );
          http.post(
            "/transition-meta/create/",
            new_transition.to_create_request(),
            (response) => {
              if (
                !this.states.find(
                  (state) => state.id == this.new_transition_state.id
                )
              ) {
                this.states.push(this.new_transition_state);
              }

              var source_state = this.states.find(
                (state) => state.id == new_transition.source_state_id
              );
              var destination_state = this.states.find(
                (state) => state.id == new_transition.destination_state_id
              );

              emit_success(
                `Transition meta ${source_state.label} -> ${
                  destination_state.label
                }${is_state_created ? " ( New )" : ""} is created`,
                2000
              );

              new_transition.is_new = false;
              new_transition.id = response.data.id;
              this.transitions.push(new_transition);
              this._selected_state(this.new_transition_state);
              this.new_transition_state = null;
            }
          );
        });
      }
    },
    updateQuery(update) {
      var query = { ...this.$route.query, ...update };

      var that = this;
      if (
        Object.keys(query).some(
          (queryKey) => that.$route.query[queryKey] != query[queryKey]
        )
      ) {
        this.$router.push({ query });
      }
    },

    onTransitionSelected(transition_id) {
      this.selected_transition = this.transitions.find(
        (transition) => transition.id == transition_id
      );
      if (this.selected_transition) {
        let transitionNameFallback = this._get_state_by_id(
          this.selected_transition.destination_state_id
        ).label;

        this.new_transition_name = this.selected_transition.name
          ? this.selected_transition.name
          : transitionNameFallback;
      }
    },
    updateTransitionName() {
      if (this.new_transition_name && this.selected_transition) {
        http
          .patch(`/transition-meta/update/${this.selected_transition.id}/`, {
            name: this.new_transition_name,
          })
          .then((response) => {
            this.refetch();
            this.selected_transition = {};
            this.new_transition_name = null;
            const edgePathElements = document.querySelectorAll(".edgePath");
            edgePathElements.forEach((element) => {
              element.classList.remove("edge-SELECTED");
            });
          })
          .catch((error) => {
            console.error("Error updating transition name:", error);
          });
      }
    },

    goToEditWorkflowRules() {
      this.$router.push({
        name: "edit-workflow-rules",
        params: { id: this.workflow.id },
      });
    },
    _get_state_by_id(state_id) {
      return this.states.find((state) => state.id == state_id);
    },
  },
};
</script>

<style>
.v-input__slot {
  max-width: 550px !important;
  border: 1px solid #d2d2d2 !important;
  border-radius: 100px !important;
  padding: 12px 16px !important;
  caret-color: #121722 !important;
  margin: 0 0 8px 0 !important;
}
.v-input__slot:focus-within {
  box-shadow: none !important;
  border: none !important;
}
</style>
