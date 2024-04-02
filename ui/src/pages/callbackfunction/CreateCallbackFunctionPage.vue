<template>
  <v-container fluid>
    <v-form ref="form" v-model="valid">
      <v-row justify="center" align="center">
        <v-col justify="center" align="center" class="page-header">
          <div>
            <p class="text-[#121722] mb-6">
              <span
                class="text-[#A0A2A7 ] cursor-pointer"
                @click="navigateToFunctions"
                >Functions / </span
              >[New Functoins]
            </p>
          </div>
          <h1 class="flex items-center gap-2 cursor-pointer" @click="goBack">
            <span class="mdi mdi-arrow-left text-[23px]"></span>
            <span class="text-[#121722]">Back</span>
          </h1>
        </v-col>
      </v-row>
      <v-row justify="center" align="center">
        <v-col>
          <v-row>
            <v-col class="functions">
              <p class="mb-0 !text-[#121722]">Function Name</p>
              <v-text-field
                v-model="callback_function_name"
                :rules="functionNameRules"
                required
                variant="outlined"
                placeholder="Callback Function Name"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <CodeEditor
                v-model="callback_function_body"
                class="border border-[#E7E8E9] rounded-[4px]"
              />
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <v-row>
        <v-col justify="center" align="right">
          <v-btn
            large
            color="primary"
            @click="publish"
            dark
            class="rounded-[64px] !py-5 !px-4 w-[150px]"
          >
            <v-icon>mdi-check</v-icon>
            <span class="normal-case font-bold text-base flex-1">Create </span>
          </v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
import CodeEditor from "@/components/CodeEditor.vue";
import { emit_success } from "@/helpers/event_bus";
import http from "@/helpers/http";

export default {
  name: "CreateCallbackFunctionPage",
  components: {
    CodeEditor,
  },
  data: () => ({
    valid: true,
    callback_function_name: null,
    callback_function_body: null,
    functionNameRules: [
      (v) => !!v || "Function name is required",
      (v) => (v && v.length <= 200) || "Name must be less than 200 characters",
    ],
  }),
  methods: {
    publish() {
      if (this.$refs.form.validate()) {
        http.post(
          "/function/create/",
          {
            name: this.callback_function_name,
            body: this.callback_function_body,
          },
          () => {
            emit_success(
              `Function '${this.callback_function_name}' is created`
            );
            this.$router.push({ name: "list-callback-functions" });
          }
        );
      }
    },
    navigateToFunctions() {
      this.$router.push({ name: "list-callback-functions" });
    },
    goBack() {
      this.$router.go(-1);
    },
  },
};
</script>
<style>
.functions .v-input__slot {
  max-width: 550px !important;
  border: 1px solid #d2d2d2 !important;
  border-radius: 100px !important;
  padding: 12px 16px !important;
  caret-color: #121722 !important;
  margin: 0 0 8px 0 !important;
}
.functions .v-input__slot:after {
  border: none !important;
}
</style>
