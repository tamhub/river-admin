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
      </v-row>
      <v-row>
        <v-flex xs12 sm12 md8>
          <v-container>
            <WorkflowIllustration
              :states="states"
              :transitions="transitions"
              :editable="true"
              @on-transition-selected="on_transition_selected"
              @refetch="refetch"
            />
          </v-container>
        </v-flex>
        <v-flex class="py-3 pr-4" xs12 sm12 md4>
          <div
            class="border border-[#E4E4E4] rounded-[20px] bg-[#FAFAFA] w-full overflow-x-hidden"
            style="box-shadow: 0px 0px 64px 0px #D2D2D23D inset;

box-shadow: -2px 7px 16px 0px #BFBFBF1A;

box-shadow: -59px 170px 50px 0px #BFBFBF00;
"
          >
            <div class="w-full h-full" v-if="selected_transition">
              <div
                class="h-full flex flex-col flex-nowrap pb-5 max-h-[calc(100vh-300px)] overflow-y-auto "
              >
                <div class="w-full px-4 py-3">
                  <div class="w-full h-full">
                    <span class="text-[#A0A2A7] text-base">Transition</span>
                    <div
                      class="flex items-center justify-start flex-nowrap gap-1 w-full pt-2 pb-4 border-b border-[#DBDBDB]"
                    >
                      <div
                        class="bg-[#EFECFF] text-base text-[#5E45FF] max-w-[calc(50%-20px)] px-2.5 py-1 rounded-full truncate select-none"
                      >
                        <span
                          v-text="
                            selected_transition.name
                              ? selected_transition.name
                              : this._get_state_by_id(
                                  selected_transition.destination_state_id
                                ).label
                          "
                        ></span>
                      </div>
                      <!-- <span class="text-base">
                        to
                      </span>
                      <div
                        class="bg-[#EFECFF] text-base text-[#5E45FF] max-w-[calc(50%-20px)] px-2.5 py-1 rounded-full truncate select-none"
                      >
                        <span
                          v-text="
                            get_state_by(
                              selected_transition.destination_state_id
                            ).label
                          "
                        ></span>
                      </div> -->
                    </div>
                  </div>
                  <div class="flex-grow-1"></div>
                </div>
                <div class="">
                  <ApprovalList
                    :workflow="workflow"
                    :approvals="selected_transition.approvals"
                    :editable="!readonly"
                    @on-delete="on_approval_deleted"
                    @on-order-change="on_approvals_order_change"
                    @on-hook-create="on_approval_hook_created"
                    @on-hook-delete="on_approval_hook_deleted"
                  />
                </div>
                <div class="w-full px-6 mt-auto">
                  <div
                    class="flex pb-5 "
                    v-if="selected_transition.hooks.length > 0"
                  >
                    <div class="w-full px-4 py-3 bg-white rounded-lg shadow-md">
                      <span class="flex items-center justify-between pb-5 ">
                        <span
                          class="flex items-center justify-start gap-2 text-[#595D64] text-base "
                        >
                          <svg
                            width="14"
                            height="16"
                            viewBox="0 0 14 16"
                            fill="none"
                            xmlns="http://www.w3.org/2000/svg"
                          >
                            <path
                              d="M7.66667 1.33325L1 9.33325H7L6.33333 14.6666L13 6.66658H7L7.66667 1.33325Z"
                              stroke="#595D64"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                            />
                          </svg>

                          Before completing the transition...
                        </span>

                        <button
                          v-if="!readonly"
                          @click="allowEditingHooks = !allowEditingHooks"
                        >
                          <span
                            v-if="!allowEditingHooks"
                            class="flex items-center justify-center w-8 h-8"
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
                                  stroke="#121722"
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
                          </span>
                          <svg
                            v-else
                            width="32"
                            height="32"
                            viewBox="0 0 32 32"
                            fill="none"
                            xmlns="http://www.w3.org/2000/svg"
                          >
                            <path
                              d="M0 16C0 7.16344 7.16344 0 16 0C24.8366 0 32 7.16344 32 16C32 24.8366 24.8366 32 16 32C7.16344 32 0 24.8366 0 16Z"
                              fill="#5E45FF"
                            />
                            <path
                              d="M21.3332 12L13.9998 19.3333L10.6665 16"
                              stroke="white"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                            />
                          </svg>
                        </button>
                      </span>
                      <div class="flex gap-2">
                        <div
                          v-for="(hook, index) in selected_transition.hooks"
                          :key="hook.id"
                        >
                          <HookDetail
                            :hook="hook"
                            :editable="!readonly && allowEditingHooks"
                            @on-delete="on_transition_hook_deleted"
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                  <v-speed-dial v-if="!readonly" v-model="fab" direction="top">
                    <template v-slot:activator>
                      <v-btn
                        large
                        v-model="fab"
                        color="primary"
                        class="w-full rounded-full"
                      >
                        <span
                          class="flex items-center justify-between w-full gap-1 "
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
                            Add
                          </span>
                          <span></span>
                        </span>
                      </v-btn>
                    </template>

                    <div
                      class="flex flex-col w-full overflow-hidden shadow rounded-3xl approval-shadow"
                      top
                    >
                      <button
                        class="flex items-center justify-start w-full gap-4 p-5 bg-white"
                        @click="newApprovalDialog = true"
                      >
                        <svg
                          width="16"
                          height="16"
                          viewBox="0 0 16 16"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <g clip-path="url(#clip0_23_515)">
                            <path
                              d="M14.6666 7.38674V8.00007C14.6658 9.43769 14.2003 10.8365 13.3395 11.988C12.4787 13.1394 11.2688 13.9817 9.89016 14.3893C8.51154 14.797 7.03809 14.748 5.68957 14.2498C4.34104 13.7516 3.18969 12.8308 2.40723 11.6248C1.62476 10.4188 1.25311 8.99212 1.3477 7.55762C1.44229 6.12312 1.99806 4.75762 2.93211 3.66479C3.86615 2.57195 5.12844 1.81033 6.53071 1.4935C7.93298 1.17668 9.4001 1.32163 10.7133 1.90674"
                              stroke="#A0A2A7"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                            />
                            <path
                              d="M14.6667 2.66675L8 9.34008L6 7.34008"
                              stroke="#A0A2A7"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                            />
                          </g>
                          <defs>
                            <clipPath id="clip0_23_515">
                              <rect width="16" height="16" fill="white" />
                            </clipPath>
                          </defs>
                        </svg>

                        <span>Add Approval Step</span>
                      </button>

                      <span class="w-full h-[1px] bg-[#F1F1F1]"></span>
                      <button
                        class="flex items-center justify-start w-full gap-4 p-5 bg-white"
                        @click="newTransitionHookDialog = true"
                      >
                        <svg
                          width="16"
                          height="16"
                          viewBox="0 0 16 16"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            d="M8.66667 1.33325L2 9.33325H8L7.33333 14.6666L14 6.66658H8L8.66667 1.33325Z"
                            stroke="#5E45FF"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                          />
                        </svg>

                        <span>Add Transition Hook</span>
                      </button>
                    </div>
                  </v-speed-dial>
                </div>
              </div>
            </div>
            <div class="px-2 py-2" v-else-if="!readonly">
              <EmptyState
                label="Select a transition"
                description="Selecting a transition by clicking the arrow, you'll be able to create the rules."
              >
                <template v-slot:icon>mdi-mouse</template>
              </EmptyState>
            </div>
          </div>
        </v-flex>
      </v-row>
    </v-container>
    <v-dialog
      v-model="newApprovalDialog"
      max-width="800"
      v-if="!readonly && selected_transition"
    >
      <CreateApprovalForm
        :workflow="workflow"
        :transition_id="selected_transition.id"
        @on-create="on_approval_created"
      />
    </v-dialog>
    <v-dialog
      v-model="newTransitionHookDialog"
      max-width="800"
      v-if="!readonly && selected_transition"
    >
      <CreateTransitionHookForm
        :workflow="workflow"
        :transition_meta="selected_transition.id"
        :excluded_function_ids="
          selected_transition.hooks.map((hook) => hook.callback_function.id)
        "
        @on-create="on_transition_hook_created"
      />
    </v-dialog>
  </div>
</template>

<script>
import ApprovalList from "@/components/ApprovalList.vue";
import CreateApprovalForm from "@/components/CreateApprovalForm.vue";
import CreateTransitionHookForm from "@/components/CreateTransitionHookForm.vue";
import EmptyState from "@/components/EmptyState.vue";
import HookDetail from "@/components/HookDetail.vue";
import WorkflowIllustration from "@/components/WorkflowIllustration.vue";
import { emit_success } from "@/helpers/event_bus";
import http from "@/helpers/http";
import {
  Approval,
  ApprovalHook,
  State,
  Transition,
  TransitionHook,
  Workflow,
} from "@/models/models";

export default {
  name: "EditWorkflowRulesPage",
  components: {
    EmptyState,
    CreateApprovalForm,
    CreateTransitionHookForm,
    WorkflowIllustration,
    ApprovalList,
    HookDetail,
  },
  props: ["readonly"],
  data: () => ({
    newApprovalDialog: false,
    newTransitionHookDialog: false,
    fab: false,
    workflow: null,
    initialized: false,
    selected_transition: null,
    states: [],
    transitions: [],
    alert_timeout: 2000,
    allowEditingHooks: false,
  }),
  mounted() {
    this.refetch();
  },
  methods: {
    refetch() {
      var workflow_id = this.$route.params.id;
      this.workflow = http.get(`/workflow/get/${workflow_id}/`, (response) => {
        this.workflow = Workflow.of(
          response.data.id,
          response.data.content_type,
          response.data.initial_state,
          response.data.field_name
        );

        var state_fetcher = this.get_states(workflow_id).then(
          (states) => (this.states = states)
        );
        var transitions_meta_fetcher = this.get_transition_metas(
          workflow_id
        ).then((transitions) => (this.transitions = transitions));

        Promise.all([state_fetcher, transitions_meta_fetcher]).then(() => {
          var selected_transition_id = this.$route.query.selected_transition_id;
          if (selected_transition_id) {
            this.on_transition_selected(selected_transition_id);
          }
          this.initialized = true;
        });
      });
    },
    get_states(workflow_id) {
      return http.get(`/workflow/state/list/${workflow_id}/`, (response) => {
        return response.data.map((state) =>
          State.of(state.id, state.label).of_description(state.description)
        );
      });
    },

    get_transition_metas(workflow_id) {
      var that = this;
      return http.get(
        `/workflow/transition-meta/list/${workflow_id}/`,
        (response) => {
          return Promise.all(
            response.data.map((transition_meta) => {
              var transition = Transition.of(
                transition_meta.id,
                this.workflow,
                transition_meta.source_state,
                transition_meta.destination_state,
                transition_meta.name
              );

              var transition_approval_metas_fetcher = that
                .get_transition_approval_metas(transition.id)
                .then((transition_approval_metas) => {
                  transition.approvals = transition_approval_metas;
                });

              var transition_hooks_fetcher = that
                .get_transition_hooks(transition.id)
                .then((transition_hooks) => {
                  transition.hooks = transition_hooks;
                });

              return Promise.all([
                transition_approval_metas_fetcher,
                transition_hooks_fetcher,
              ]).then(() => transition);
            })
          );
        }
      );
    },

    get_transition_hooks(transition_id) {
      return http.get(
        `/transition-meta/transition-hook/list/${transition_id}/`,
        (response) => {
          return response.data.map((transition_hook) =>
            TransitionHook.of(
              transition_hook.id,
              this.workflow,
              transition_hook.callback_function,
              transition_hook.transition_meta,
              transition_hook.transition,
              transition_hook.object_id,
              false
            )
          );
        }
      );
    },

    get_transition_approval_metas(transition_id) {
      var that = this;
      return http.get(
        `/transition-meta/transition-approval-meta/list/${transition_id}/`,
        (response) => {
          return Promise.all(
            response.data.map((transition_approval_meta) => {
              var approval = Approval.of(
                transition_approval_meta.id,
                this.workflow,
                transition_approval_meta.transition,
                transition_approval_meta.permissions,
                transition_approval_meta.groups
              );

              return that
                .get_transition_approval_hooks(approval.id)
                .then((transition_approval_hooks) => {
                  approval.hooks = transition_approval_hooks;
                })
                .then(() => approval);
            })
          );
        }
      );
    },
    get_transition_approval_hooks(transition_approval_meta_id) {
      return http.get(
        `/transition-approval-meta/approval-hook/list/${transition_approval_meta_id}/`,
        (response) => {
          return response.data.map((transition_approval_hook) =>
            ApprovalHook.of(
              transition_approval_hook.id,
              this.workflow,
              transition_approval_hook.callback_function,
              transition_approval_hook.transition_approval_meta,
              transition_approval_hook.transition_approval,
              transition_approval_hook.object_id,
              false
            )
          );
        }
      );
    },

    on_approval_created(created_approval) {
      if (this.selected_transition) {
        var max_priority = this.selected_transition.approvals.reduce(
          (max, approval) => Math.max(max, approval.priority),
          0
        );
        created_approval.priority = max_priority + 1;
        http.post(
          "/transition-approval-meta/create/",
          created_approval.to_create_request(),
          (response) => {
            created_approval.id = response.data.id;
            this.selected_transition.approvals.push(created_approval);
            this._update_transition(this.selected_transition);
            this.newApprovalDialog = false;
            emit_success(
              `The transition approval meta is created`,
              this.alert_timeout
            );
          }
        );
      }
    },
    on_approval_deleted(deleted_approval) {
      if (this.selected_transition) {
        http.delete(
          `/transition-approval-meta/delete/${deleted_approval.id}/`,
          (response) => {
            this.selected_transition.approvals = this.selected_transition.approvals.filter(
              (approval) => approval.id != deleted_approval.id
            );
            this._update_transition(this.selected_transition);
            emit_success(
              `The transition approval meta is deleted`,
              this.alert_timeout
            );
          }
        );
      }
    },
    on_approvals_order_change(newApprovals) {
      http
        .post(
          `/transition-approval-meta/re-prioritize/`,
          newApprovals.map((new_aproval) => ({
            transition_approval_meta_id: new_aproval.id,
            priority: new_aproval.priority,
          }))
        )
        .then((response) => {
          this.selected_transition.approvals = newApprovals;
          this._update_transition(this.selected_transition);
          emit_success(
            `Re-prioritization has been applied`,
            this.alert_timeout
          );
        });
    },
    on_transition_hook_created(created_hook) {
      if (
        this.selected_transition &&
        !this.selected_transition.hooks.find(
          (hook) => hook.id == created_hook.id
        )
      ) {
        http.post(
          "/transition-hook/create/",
          created_hook.to_create_request(),
          (response) => {
            created_hook.id = response.data.id;
            this.selected_transition.hooks.push(created_hook);
            this._update_transition(this.selected_transition);
            this.newTransitionHookDialog = false;
            emit_success(`The transition hook is created`, this.alert_timeout);
          }
        );
      }
    },
    on_transition_hook_deleted(deleted_hook) {
      if (this.selected_transition) {
        http.delete(
          `/transition-hook/delete/${deleted_hook.id}/`,
          (response) => {
            this.selected_transition.hooks = this.selected_transition.hooks.filter(
              (hook) => hook.id != deleted_hook.id
            );
            this._update_transition(this.selected_transition);
            emit_success(`The transition hook is deleted`, this.alert_timeout);
          }
        );
      }
    },
    on_approval_hook_created(created_hook) {
      if (this.selected_transition) {
        var approval = this.selected_transition.approvals.find(
          (approval) => approval.id == created_hook.transition_approval_meta_id
        );
        if (
          approval &&
          !approval.hooks.find((hook) => hook.id == created_hook.id)
        ) {
          http.post(
            "/approval-hook/create/",
            created_hook.to_create_request(),
            (response) => {
              created_hook.id = response.data.id;
              approval.hooks.push(created_hook);
              this._update_approval(this.selected_transition, approval);
              this._update_transition(this.selected_transition);
              emit_success(`The approval hook is created`, this.alert_timeout);
            }
          );
        }
      }
    },
    on_approval_hook_deleted(deleted_hook) {
      if (this.selected_transition) {
        var approval = this.selected_transition.approvals.find(
          (approval) => approval.id == deleted_hook.transition_approval_meta_id
        );
        if (approval) {
          http.delete(
            `/approval-hook/delete/${deleted_hook.id}/`,
            (response) => {
              approval.hooks = approval.hooks.filter(
                (hook) => hook.id != deleted_hook.id
              );
              this._update_approval(this.selected_transition, approval);
              this._update_transition(this.selected_transition);
              emit_success(`The approval hook is deleted`, this.alert_timeout);
            }
          );
        }
      }
    },
    on_transition_selected(transition_id) {
      this.selected_transition = this.transitions.find(
        (transition) => transition.id == transition_id
      );

      this._update_query({
        selected_transition_id: JSON.stringify(transition_id),
      });
    },
    get_state_by(id) {
      return this.states.find((state) => state.id == id);
    },
    _update_transition(transition) {
      // this._repriotise_approvals(transition);
      this.transitions = this.transitions.map((t) =>
        t.id == transition.id ? transition : t
      );
    },
    _update_approval(transition, approval) {
      transition.approvals = transition.approvals.map((a) =>
        a.id == approval.id ? approval : a
      );
    },
    _update_query(update) {
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
    _repriotise_approvals(transition) {
      var that = this;
      transition.approvals = transition.approvals
        .sort((a1, a2) => a1.priority - a2.priority)
        .map((approval, index) => {
          var newApproval = { ...approval, priority: index + 1 };
          return newApproval;
        });
    },
    _get_state_by_id(state_id) {
      return this.states.find((state) => state.id == state_id);
    },
  },
};
</script>

<style>
.fab_container {
  position: fixed;
  bottom: 45px;
  right: 30px;
  z-index: 10;
}

.v-chip__content {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  /* Prevents the text from wrapping */
  width: 100%;
}

.approval-shadow {
  box-shadow: -2px 7px 16px 0px #bfbfbf1a;

  box-shadow: -10px 27px 29px 0px #bfbfbf17;

  box-shadow: -21px 61px 39px 0px #bfbfbf0d;

  box-shadow: -38px 109px 46px 0px #bfbfbf03;

  box-shadow: -59px 170px 50px 0px #bfbfbf00;
}
</style>
