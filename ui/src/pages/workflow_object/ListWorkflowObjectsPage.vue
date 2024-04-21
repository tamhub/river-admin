<template>
  <v-container fluid v-if="initialized">
    <v-container fluid>
      <v-row justify="center" align="center">
        <v-col justify="start" align="start">
          <h1 class="font-bold text-[#121722] text-[24px]">
            {{ getItemTitle(workflow) }}
            <!-- <v-chip color="primary" class="white--text">
              <v-icon left>mdi-sitemap</v-icon>
              <span v-text="workflow.identifier"></span>
            </v-chip> -->
          </h1>
        </v-col>
      </v-row>
      <v-row justify="center" align="center">
        <v-col>
          <v-data-table :headers="headers" :items="workflow_objects" :items-per-page="10"
            class="elevation-1 custom-data-table">
            <template v-slot:item.action="{ item }">
              <v-tooltip top v-if="has_change_workflow_permission">
                <template v-slot:activator="{ on }">
                  <v-icon class="mr-1" v-on="on" color="primary" @click="goToTimeline(item)">mdi-timeline-text</v-icon>
                </template>
                <span>View & Edit Timeline</span>
              </v-tooltip>

              <v-tooltip top v-else>
                <template v-slot:activator="{ on }">
                  <v-icon class="mr-1" v-on="on" color="primary"
                    @click="goToViewTimeline(item)">mdi-timeline-text</v-icon>
                </template>
                <span>View Timeline</span>
              </v-tooltip>

              <v-tooltip top>
                <template v-slot:activator="{ on }">
                  <v-btn icon color="warning" v-on="on" @click="showDeletingDialog(item)"
                    :disabled="!has_delete_workflow_permission">
                    <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </template>
                <span>Delete Workflow Object</span>
              </v-tooltip>
            </template>
          </v-data-table>
        </v-col>
      </v-row>
    </v-container>
    <v-dialog v-if="this.deletingWorkflowObject" v-model="deleteDialog" max-width="50%">
      <v-card>
        <v-card-title class="headline flex flex-col gap-[17px]">
          <svg width="133" height="132" viewBox="0 0 133 132" fill="none" class="m-auto"
            xmlns="http://www.w3.org/2000/svg">
            <path opacity="0.1"
              d="M11.5 60C11.5 90 44.8056 126 66 126C87.1944 126 120.5 90 120.5 60V42C120.5 33 114.444 24 102.333 18C102.333 18 81.1389 6 66 6C50.8611 6 29.6667 18 29.6667 18C17.5556 24 11.5 33 11.5 42V60Z"
              fill="#E33554" />
            <path opacity="0.2"
              d="M13.5 60.2C13.5 89.2 45.5833 124 66 124C86.4167 124 118.5 89.2 118.5 60.2V42.8C118.5 34.1 112.667 25.4 101 19.6C101 19.6 80.5833 8 66 8C51.4167 8 31 19.6 31 19.6C19.3333 25.4 13.5 34.1 13.5 42.8V60.2Z"
              fill="#E33554" />
            <path opacity="0.3"
              d="M16.5 60.5C16.5 88 46.75 121 66 121C85.25 121 115.5 88 115.5 60.5V44C115.5 35.75 110 27.5 99 22C99 22 79.75 11 66 11C52.25 11 33 22 33 22C22 27.5 16.5 35.75 16.5 44V60.5Z"
              fill="#E33554" />
            <path d="M66.4805 47.8335V67.8335" stroke="#E33554" stroke-width="4.5" stroke-linecap="round"
              stroke-linejoin="round" />
            <path d="M66.4805 87.8335H66.5273" stroke="#E33554" stroke-width="4.5" stroke-linecap="round"
              stroke-linejoin="round" />
          </svg>
          <span class="font-bold text-[40px] text-[#E33554]">
            {{ "Delete workflow object" }}
          </span>
          <p class="text-center text-xl text-[#121722] break-normal mb-0">
            {{ `Are you sure you want to remove ${deletingWorkflowObject.identifier} this function?` }}
          </p>
          <v-card-actions class="flex gap-[17px] items-center justify-start">
            <div
              class="flex items-center gap-2 bg-transparent text-[#5E45FF] border-[#5E45FF] border  p-4 rounded-[64px] w-[200px] ms-auto cursor-pointer"
              @click="deleteDialog = false">
              <span class=" font-bold text-base flex-1 text-center">No, keep</span>
            </div>

            <div class="flex items-center gap-2 bg-[#FFDFDF] p-4 rounded-[64px] w-[200px] ms-auto cursor-pointer"
              @click="deleteWorkflowObject()">
              <svg width="16" height="17" viewBox="0 0 16 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2 4.5H3.33333H14" stroke="#E33554" stroke-linecap="round" stroke-linejoin="round" />
                <path
                  d="M5.33325 4.50016V3.16683C5.33325 2.81321 5.47373 2.47407 5.72378 2.22402C5.97383 1.97397 6.31296 1.8335 6.66659 1.8335H9.33325C9.68687 1.8335 10.026 1.97397 10.2761 2.22402C10.5261 2.47407 10.6666 2.81321 10.6666 3.16683V4.50016M12.6666 4.50016V13.8335C12.6666 14.1871 12.5261 14.5263 12.2761 14.7763C12.026 15.0264 11.6869 15.1668 11.3333 15.1668H4.66659C4.31296 15.1668 3.97382 15.0264 3.72378 14.7763C3.47373 14.5263 3.33325 14.1871 3.33325 13.8335V4.50016H12.6666Z"
                  stroke="#E33554" stroke-linecap="round" stroke-linejoin="round" />
              </svg>

              <span class="text-[#FF0F0F] font-bold text-base flex-1 text-center">Yes, delete</span>
            </div>
          </v-card-actions>
        </v-card-title>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import EmptyState from "@/components/EmptyState.vue";
import WorkflowIllustration from "@/components/WorkflowIllustration.vue";

import { Workflow } from "@/models/models";
import { emit_success } from "@/helpers/event_bus";
import { auth, WORKFLOW } from "@/helpers/auth";
import http from "@/helpers/http";

export default {
  name: "ListWorkflowObjectsPage",
  components: {
    EmptyState,
    WorkflowIllustration
  },
  data: () => ({
    initialized: false,
    workflow_loading: false,
    workflow: null,
    headers: null,
    deletingWorkflowObject: null,
    deleteDialog: false,
    workflow_objects: [],
    has_delete_workflow_permission: false,
    has_change_workflow_permission: false,
    replaceList: {
      "stage": "Tarjim Submissions",
      "budgetexpense": "Tarjim",
      "budgetstage": "Stages",
      "pk": "ID",
      "river_status": "Status",
      "content_type": "Content Type",
      "initial_state": "Initial State",
      "field_name": "Field Name",
      "my_state_field": "Status"
    },
  }),
  watch: {
    $route(to, from) {
      if (to.params.workflow_id != from.params.workflow_id) {
        this.load();
      }
    }
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      this.initialized = false;
      var workflow_id = this.$route.params.workflow_id;
      var workflow_fetcher = http.get(
        `/workflow/get/${workflow_id}/`,
        response => (this.workflow = Workflow.of(response.data.id, response.data.content_type, response.data.initial_state, response.data.field_name))
      );

      var change_workflow_permission_checker = auth.has_change_permission(WORKFLOW, answer => {
        this.has_change_workflow_permission = answer;
      });

      var delete_workflow_permission_checker = auth.has_delete_permission(WORKFLOW, answer => {
        this.has_delete_workflow_permission = answer;
      });

      Promise.all([workflow_fetcher, change_workflow_permission_checker, delete_workflow_permission_checker])
        .then(() => this.fetchWorkflowObjects())
        .then(() => (this.initialized = true))
        .finally(() => (this.workflow_loading = false));
    },
    goToCreateWorkflowPage() {
      this.$router.push({ name: "create-workflow" });
    },
    fetchWorkflowObjects() {
      this.workflow_object_loading = true;
      return http
        .get(`/workflow/object/list/${this.workflow.id}/`, response => {
          this.headers = response.data.headers
            .map(key => ({ text: this.replaceList[key] || key, value: key, align: "left" }))
            .concat([{ text: "Actions", value: "action", sortable: false }]);
          this.workflow_objects = response.data.workflow_objects.map(workflow_object => ({ ...workflow_object, identifier: workflow_object.__str }));
        })
        .finally(() => (this.workflow_object_loading = false));
    },
    goToTimeline(item) {
      this.$router.push({
        name: "edit-workflow-object-timeline",
        params: { workflow_id: this.workflow.id, object_id: item.pk }
      });
    },
    goToViewTimeline(item) {
      this.$router.push({
        name: "view-workflow-object-timeline",
        params: { workflow_id: this.workflow.id, object_id: item.pk }
      });
    },
    showDeletingDialog(workflow_object) {
      this.deletingWorkflowObject = workflow_object;
      this.deleteDialog = true;
    },
    deleteWorkflowObject() {
      if (this.deletingWorkflowObject) {
        http.delete(`/workflow-object/delete/${this.workflow.id}/${this.deletingWorkflowObject.id}/`, () => {
          this.fetchWorkflowObjects();
          this.deleteDialog = false;
          emit_success(`Workflow object ${this.deletingWorkflowObject.identifier} is deleted.`);
        });
      }
    },
    _updateQuery(update) {
      var query = { ...this.$route.query, ...update };

      var that = this;
      if (Object.keys(query).some(queryKey => that.$route.query[queryKey] != query[queryKey])) {
        this.$router.push({ query });
      }
    },
    getItemTitle(item) {
      return this.replaceList[item.content_type.model] || item.content_type.model
    }
  }
};
</script>