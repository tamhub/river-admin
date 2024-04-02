<template>
  <v-container fluid v-if="callback_function">
    <v-row justify="center" align="center">
      <v-col justify="center" align="center" class="page-header">
        <div>
          <p class="text-[#121722] mb-6">
            <span
              class="text-[#A0A2A7 ] cursor-pointer"
              @click="navigateToFunctions"
              >Functions / </span
            >{{ callback_function.name }}
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
        <v-row class="flex items-center">
          <v-col cols="auto">
            <label>
              <h3>Name:</h3>
            </label>
          </v-col>
          <v-col>
            <v-chip color="primary" class="white--text">
              <v-icon left>mdi-function-variant</v-icon>
              <span v-text="callback_function.name"></span>
            </v-chip>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <CodeEditor
              v-model="callback_function.body"
              class="border border-[#E7E8E9] rounded-[4px]"
              :read_only="true"
            />
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import CodeEditor from "@/components/CodeEditor.vue";
import http from "@/helpers/http";

export default {
  name: "CreateCallbackFunctionPage",
  components: {
    CodeEditor,
  },
  data: () => ({
    callback_function: null,
  }),
  mounted() {
    var function_id = this.$route.params.id;
    http.get(
      `/function/get/${function_id}/`,
      (response) => (this.callback_function = response.data)
    );
  },
  methods: {
    navigateToFunctions() {
      this.$router.push({ name: "list-callback-functions" });
    },
    goBack() {
      this.$router.go(-1);
    },
  },
};
</script>
