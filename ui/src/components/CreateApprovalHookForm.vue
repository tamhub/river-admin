<template>
  <v-card class="pa-5" :elevation="6">
    <v-card-title>
      <span class="flex items-center justify-start gap-2">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M12.5769 5.38449C12.7008 4.39366 11.4557 3.85317 10.8164 4.62027L4.36682 12.3598C3.82405 13.0111 4.2872 14 5.13504 14H10.8672C11.4687 14 11.9341 14.5272 11.8595 15.124L11.4231 18.6155C11.2992 19.6063 12.5443 20.1468 13.1836 19.3797L19.6332 11.6402C20.176 10.9889 19.7128 10 18.865 10H13.1328C12.5313 10 12.0659 9.47282 12.1405 8.87597L12.5769 5.38449Z"
            stroke="#4397D8" stroke-linecap="round" stroke-linejoin="round" />
        </svg>

        New Hook
      </span>

    </v-card-title>
    <v-card-text>
      <v-container fluid>
        <v-row>
          <v-col>
            <span>Before completing the transition...</span>
            <v-autocomplete v-model="selected_function" :items="functions" :loading="functions_loading"
              :search-input.sync="search_functions" hide-selected item-text="name" label="Search functions" clearable
              chips return-object rounded solo prepend-inner-icon="fa-search">
              <template v-slot:no-data>
                <v-list-item>
                  <v-list-item-title>
                    Start typing to search for the
                    <strong>callback functions</strong>
                  </v-list-item-title>
                </v-list-item>
              </template>
              <template v-slot:selection="{ attr, on, item, selected }">
                <v-chip v-bind="attr" :input-value="selected" color="primary" class="white--text" v-on="on">
                  <v-icon left>mdi-function-variant</v-icon>
                  <span v-text="item.name"></span>
                </v-chip>
              </template>
              <template v-slot:item="{ item }">
                <v-list-item-content>
                  <v-list-item-title v-text="item.name"></v-list-item-title>
                </v-list-item-content>
              </template>
            </v-autocomplete>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
    <v-card-actions>
      <v-row>
        <v-col justify="center" align="right">
          <v-btn class="rounded-full mt-0.5   mb-3" large color="primary" @click="createHook">
            <span class="flex w-full items-center gap-2 justify-between">


              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M8.66667 1.33325L2 9.33325H8L7.33333 14.6666L14 6.66658H8L8.66667 1.33325Z" stroke="#5E45FF"
                  stroke-linecap="round" stroke-linejoin="round" />
              </svg>

              <span class="font-bold capitalize">

                Create Hook
              </span>
              <span></span>
            </span>
          </v-btn>
        </v-col>
      </v-row>
    </v-card-actions>
  </v-card>
</template>

<script>
import { Function, ApprovalHook } from "@/models/models";
import http from "@/helpers/http";

export default {
  name: "CreateApprovalHookForm",
  props: ["workflow", "transition_approval_meta_id", "object_id", "transition_approval_id", "excluded_function_ids"],
  data: () => ({
    functions_loading: false,
    selected_function: null,
    functions: [],
    search_functions: null
  }),
  mounted() { },
  watch: {
    selected_function(val) {
      this.search_functions = null;
    },
    search_functions(searchTerm) {
      if (!searchTerm || (this.selected_function && this.selected_function.name.includes(searchTerm))) {
        return;
      }
      this.functions_loading = true;
      http
        .get(
          "/function/list/",
          response => (this.functions = response.data.map(f => Function.of(f.id, f.name, f.body)).filter(f => !this.excluded_function_ids.includes(f.id)))
        )
        .finally(() => (this.functions_loading = false));
    }
  },
  methods: {
    createHook() {
      var hook = ApprovalHook.create(this.workflow, this.selected_function, this.transition_approval_meta_id, this.transition_approval_id, this.object_id);
      this.$emit("on-create", hook);
      this.selected_function = null;
    }
  }
};
</script>