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
              >{{ functionName }}
            </p>
          </div>
          <h1
            class="flex items-center gap-2 cursor-pointer w-fit"
            @click="goBack"
          >
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
            <v-icon>mdi-content-save</v-icon>
            <span class="normal-case font-bold text-base flex-1">Update </span>
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
    functionName: null,
  }),
  mounted() {
    var function_id = this.$route.params.id;
    http.get(`/function/get/${function_id}/`, (response) => {
      console.log(response);
      this.callback_function_name = response.data.name;
      this.callback_function_body = response.data.body;
      this.functionName = response.data.name;
    });
  },
  methods: {
    publish() {
      if (this.$refs.form.validate()) {
        var function_id = this.$route.params.id;
        http.put(
          `/function/update/${function_id}/`,
          {
            name: this.callback_function_name,
            body: this.callback_function_body,
          },
          () => {
            emit_success(
              `Function '${this.callback_function_name}' is updated`
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
