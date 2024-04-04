<template>
  <div class="container pe-10">
    <!-- <EmptyState label="Create your initial state"
      description="Creating your initial state, you'll be able to start designing your workflow."> -->
    <!-- <template v-slot:icon>mdi-file-tree</template> -->
    <!-- <template v-slot:content> -->
    <div>
      <div class="flex gap-1 flex-col">
        <span class="pb-2">Workflow Title</span>
        <WorkflowInput v-model="workflow" />
      </div>
    </div>
    <div
      class="flex items-center justify-center w-full h-[calc(100vh-350px)]  bg-[#E9E9E9] rounded-[20px] relative select-none cursor-default">
      <span class="absolute top-0 left-0 px-6 py-4 text-[#A0A2A7]">Diagram</span>

      <div class="flex flex-col items-center justify-center gap-16">
        <svg width="201" height="49" viewBox="0 0 201 49" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="0.5" width="200" height="49" rx="24.5" fill="#E4E4E4" />
        </svg>
        <h3 class="max-w-[480px] text-[#CCCCCC] text-[40px] text-center leading-10">
          Create your workflow’s
          <span class="font-bold">

            initial state.
          </span>
        </h3>
      </div>

    </div>

    <div class="flex items-start justify-start gap-3 pt-6">
      <div class="max-w-[500px] w-full">
        <StateInput v-model="initial_state" placeholder="Search for initial state" />
      </div>
      <div>
        <v-btn class="rounded-full mt-0.5" :disabled="!(workflow && initial_state)" @click="createWorkflow" large
          color="primary">

          <svg width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M8.50004 15.25C12.1819 15.25 15.1667 12.2653 15.1667 8.58335C15.1667 4.90146 12.1819 1.91669 8.50004 1.91669C4.81814 1.91669 1.83337 4.90146 1.83337 8.58335C1.83337 12.2653 4.81814 15.25 8.50004 15.25Z"
              stroke="white" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M8.5 5.91669V11.25" stroke="white" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M5.83337 8.58337H11.1667" stroke="white" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          <span class="font-bold capitalize">

            Add state
          </span>
        </v-btn>
      </div>
    </div>

    <!-- </template> -->
    <!-- </EmptyState> -->
  </div>
</template>

<script>
import WorkflowInput from "@/components/WorkflowInput.vue";
import StateInput from "@/components/StateInput.vue";
import EmptyState from "@/components/EmptyState.vue";
import { Workflow } from "@/models/models";
import { emit_success } from "@/helpers/event_bus";
import http from "@/helpers/http";

export default {
  name: "CreateWorkflowPage",
  components: {
    WorkflowInput,
    StateInput,
    EmptyState
  },
  data: () => ({
    workflow: null,
    initial_state: null
  }),
  methods: {
    createWorkflow() {
      if (this.workflow && this.initial_state) {
        var promise = Promise.resolve();
        if (this.initial_state.is_new) {
          promise = http.post("/state/create/", this.initial_state.to_create_request(), response => {
            this.initial_state.is_new = false;
            this.initial_state.id = response.data.id;
            this.initial_state.final_label = this.initial_state.label;
          });
        }

        promise.then(response => {
          this.workflow.initial_state = this.initial_state;
          http.post("/workflow/create/", this.workflow.to_create_request(), response => {
            this.workflow.id = response.data.id;
            emit_success(`Workflow ${this.workflow.identifier} is created with initial state ${this.initial_state.label}`);
            this.$router.push({ name: "edit-workflow", params: { id: this.workflow.id } });
          });
        });
      }
    }
  }
};
</script>