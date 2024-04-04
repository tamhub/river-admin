<template>
  <v-autocomplete v-model="model" :items="items" :loading="loading" :search-input.sync="search" hide-selected
    item-text="identifier" label="Search for a workflow..." clearable return-object rounded solo
    prepend-inner-icon="fa-search">
    <template v-slot:no-data>
      <v-list-item>
        <v-list-item-title>
          Start typing to search for the
          <strong>workflows</strong>
        </v-list-item-title>
      </v-list-item>
    </template>
    <template v-slot:selection="{ attr, on, item, selected }">{{ item.identifier }}</template>
    <template v-slot:item="{ item }">
      <v-list-item-content>
        <v-list-item-title v-text="item.identifier"></v-list-item-title>
      </v-list-item-content>
    </template>
  </v-autocomplete>
</template>

<script>
import { Workflow } from "@/models/models";
import http from "@/helpers/http";

export default {
  name: "WorkflowInput",
  props: ["value"],
  data: () => ({
    loading: false,
    items: [],
    search: null,
    model: null
  }),
  watch: {
    model(val) {
      this.$emit("input", val);
    },
    search(val) {
      if (this.items.length > 0) return;
      this.loading = true;

      http
        .get("/workflow/state-field/list/", response => {
          var that = this;
          this.items = response.data.map(result => Workflow.create(result.content_type, null, result.field_name));
        })
        .finally(() => (this.loading = false));
    }
  }
};
</script>

<style>
.v-input__icon--prepend-inner {
  width: 20px;
  height: 20px;
  padding-right: 5px;
}

.v-text-field.v-text-field--solo:not(.v-text-field--solo-flat)>.v-input__control>.v-input__slot {
  box-shadow: none !important;
  border: 1.5px solid #D2D2D2;
}

.v-text-field.v-text-field--solo:not(.v-text-field--solo-flat)>.v-input__control>.v-input__slot:focus-within {
  border: 1.5px solid #5E45FF
}
</style>