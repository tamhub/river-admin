<template>
  <v-container fluid>
    <v-row justify="center" align="center">
      <v-col class="flex justify-between items-center">
        <h1 class="page-header font-bold text-2xl">
          Functions
        </h1>
        <div class="" v-if="has_add_function_permission">
          <v-btn
            large
            color="primary"
            @click="goToCreateFunctionPage"
            dark
            class="rounded-[64px] !py-5 !px-4"
          >
            <v-icon>mdi-plus-circle-outline</v-icon>
            <span class="normal-case font-bold text-base">Create new</span>
          </v-btn>
        </div>
      </v-col>
    </v-row>
    <v-row justify="center" align="center">
      <v-col>
        <v-data-table
          :headers="headers"
          :items="items"
          :items-per-page="10"
          class="elevation-1 custom-data-table"
          :footer-props="{
            'items-per-page-text': 'View',
          }"
        >
          <template v-slot:item="{ item }">
            <tr class="custom-row  group hover:!bg-[#fafafa] cursor-pointer">
              <td
                class="text-[#121722] !ps-[48px] rounded-tl-2xl  group-hover:text-[#5E45FF] group-hover:font-bold transition duration-150 rounded-bl-2xl"
                @click="goToViewFunctionPage(item.id)"
              >
                {{ item.name }}
              </td>
              <td
                class="font-bold text-base text-[#A0A2A7]"
                @click="goToViewFunctionPage(item.id)"
              >
                {{ item.version }}
              </td>
              <td @click="goToViewFunctionPage(item.id)">
                <span class="text-[#A0A2A7] font-normal">{{
                  item.date_created | moment("h:mm ")
                }}</span>
                <span class="text-[#121722]">{{
                  item.date_created | moment("DD/MM/YYYY ")
                }}</span>
              </td>
              <td @click="goToViewFunctionPage(item.id)">
                <span class="text-[#A0A2A7] font-normal">{{
                  item.date_updated | moment("h:mm ")
                }}</span>
                <span class="text-[#121722]">{{
                  item.date_updated | moment("DD/MM/YYYY ")
                }}</span>
              </td>

              <td class="rounded-tr-2xl rounded-br-2xl flex gap-4 items-center">
                <div
                  class="flex items-center gap-2  border border-[#121722] p-4 rounded-[64px] ms-auto cursor-pointer"
                  @click="goToEditFunctionPage(item.id)"
                >
                  <v-icon
                    class="mr-1"
                    color="#121722"
                    :disabled="!has_change_function_permission"
                    >mdi-pencil-outline</v-icon
                  >

                  <!-- <v-icon
                    class="mr-1"
                    color="warning"
                    @click="showDeletingDialog(item)"
                    :disabled="!has_delete_state_permission"
                    >mdi-delete</v-icon
                  > -->
                  <span
                    class="text-[#121722] font-bold text-base flex-1 text-center"
                    >Edit</span
                  >
                </div>
                <div
                  class="flex items-center gap-2 bg-[#FFDFDF] p-4 rounded-[64px] ms-auto cursor-pointer"
                  @click="showDeletingDialog(item)"
                >
                  <svg
                    width="16"
                    height="17"
                    viewBox="0 0 16 17"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M2 4.5H3.33333H14"
                      stroke="#E33554"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                    <path
                      d="M5.33325 4.50016V3.16683C5.33325 2.81321 5.47373 2.47407 5.72378 2.22402C5.97383 1.97397 6.31296 1.8335 6.66659 1.8335H9.33325C9.68687 1.8335 10.026 1.97397 10.2761 2.22402C10.5261 2.47407 10.6666 2.81321 10.6666 3.16683V4.50016M12.6666 4.50016V13.8335C12.6666 14.1871 12.5261 14.5263 12.2761 14.7763C12.026 15.0264 11.6869 15.1668 11.3333 15.1668H4.66659C4.31296 15.1668 3.97382 15.0264 3.72378 14.7763C3.47373 14.5263 3.33325 14.1871 3.33325 13.8335V4.50016H12.6666Z"
                      stroke="#E33554"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>

                  <span
                    class="text-[#FF0F0F] font-bold text-base flex-1 text-center"
                    >Delete</span
                  >
                </div>
              </td>
            </tr>
            <!-- <v-icon
              class="mr-1"
              color="primary"
              @click="goToViewFunctionPage(item.id)"
              >mdi-details</v-icon
            > -->
            <!--  
            <v-icon
              class="mr-1"
              color="primary"
              @click="goToEditFunctionPage(item.id)"
              :disabled="!has_change_function_permission"
              >mdi-pencil-outline</v-icon
            >
            <v-icon
              class="mr-1"
              color="warning"
              @click="showDeletingDialog(item)"
              :disabled="!has_delete_function_permission"
              >mdi-delete</v-icon
            > -->
          </template>
        </v-data-table>
      </v-col>
    </v-row>

    <v-dialog
      v-if="this.deletingFunction"
      v-model="deleteDialog"
      max-width="581"
    >
      <v-card>
        <v-card-title class="headline flex flex-col gap-[17px]">
          <svg
            width="133"
            height="132"
            viewBox="0 0 133 132"
            fill="none"
            class="m-auto"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              opacity="0.1"
              d="M11.5 60C11.5 90 44.8056 126 66 126C87.1944 126 120.5 90 120.5 60V42C120.5 33 114.444 24 102.333 18C102.333 18 81.1389 6 66 6C50.8611 6 29.6667 18 29.6667 18C17.5556 24 11.5 33 11.5 42V60Z"
              fill="#E33554"
            />
            <path
              opacity="0.2"
              d="M13.5 60.2C13.5 89.2 45.5833 124 66 124C86.4167 124 118.5 89.2 118.5 60.2V42.8C118.5 34.1 112.667 25.4 101 19.6C101 19.6 80.5833 8 66 8C51.4167 8 31 19.6 31 19.6C19.3333 25.4 13.5 34.1 13.5 42.8V60.2Z"
              fill="#E33554"
            />
            <path
              opacity="0.3"
              d="M16.5 60.5C16.5 88 46.75 121 66 121C85.25 121 115.5 88 115.5 60.5V44C115.5 35.75 110 27.5 99 22C99 22 79.75 11 66 11C52.25 11 33 22 33 22C22 27.5 16.5 35.75 16.5 44V60.5Z"
              fill="#E33554"
            />
            <path
              d="M66.4805 47.8335V67.8335"
              stroke="#E33554"
              stroke-width="4.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M66.4805 87.8335H66.5273"
              stroke="#E33554"
              stroke-width="4.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          <span class="font-bold text-[40px] text-[#E33554]">
            {{ "Function Deletion" }}
          </span>
          <p class="text-center text-xl text-[#121722] break-normal mb-0">
            {{ "Are you sure you want to remove this function?" }}
          </p>
          <v-card-actions class="flex gap-[17px] items-center justify-start">
            <div
              class="flex items-center gap-2 bg-transparent text-[#5E45FF] border-[#5E45FF] border  p-4 rounded-[64px] w-[200px] ms-auto cursor-pointer"
              @click="deleteDialog = false"
            >
              <span class=" font-bold text-base flex-1 text-center"
                >No, keep</span
              >
            </div>

            <div
              class="flex items-center gap-2 bg-[#FFDFDF] p-4 rounded-[64px] w-[200px] ms-auto cursor-pointer"
              @click="deleteFunction()"
            >
              <svg
                width="16"
                height="17"
                viewBox="0 0 16 17"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M2 4.5H3.33333H14"
                  stroke="#E33554"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M5.33325 4.50016V3.16683C5.33325 2.81321 5.47373 2.47407 5.72378 2.22402C5.97383 1.97397 6.31296 1.8335 6.66659 1.8335H9.33325C9.68687 1.8335 10.026 1.97397 10.2761 2.22402C10.5261 2.47407 10.6666 2.81321 10.6666 3.16683V4.50016M12.6666 4.50016V13.8335C12.6666 14.1871 12.5261 14.5263 12.2761 14.7763C12.026 15.0264 11.6869 15.1668 11.3333 15.1668H4.66659C4.31296 15.1668 3.97382 15.0264 3.72378 14.7763C3.47373 14.5263 3.33325 14.1871 3.33325 13.8335V4.50016H12.6666Z"
                  stroke="#E33554"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>

              <span
                class="text-[#FF0F0F] font-bold text-base flex-1 text-center"
                >Yes, delete</span
              >
            </div>
          </v-card-actions>
        </v-card-title>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { emit_success } from "@/helpers/event_bus";
import { auth, FUNCTION } from "@/helpers/auth";
import http from "@/helpers/http";
export default {
  name: "ListCallbackFunctionPage",
  data: () => ({
    deletingFunction: null,
    deleteDialog: false,
    headers: [
      { text: "Name", value: "name", align: "left", class: "custom-width" },
      { text: "Version", value: "version", align: "left" },
      { text: "Created At", value: "date_created", align: "left" },
      { text: "Last Updated At", value: "date_updated", align: "left" },
      {
        text: "Actions",
        value: "action",
        sortable: false,
        class: "hidden-header-cell",
      },
    ],
    items: [],
    has_add_function_permission: false,
    has_delete_function_permission: false,
    has_change_function_permission: false,
  }),
  mounted() {
    this.fetchFunctions();
  },
  methods: {
    setAlertMessage(message) {
      this.message = message;
      this.messageAlert = true;
      var that = this;
      setTimeout(() => (that.messageAlert = false), 3000);
    },
    fetchFunctions() {
      var functions_fetcher = http.get("/function/list/", (response) => {
        this.items = response.data.map((item) => ({
          ...item,
          version: `v${item.version}`,
        }));
      });

      var add_function_permission_checker = auth.has_add_permission(
        FUNCTION,
        (answer) => {
          this.has_add_function_permission = answer;
        }
      );

      var change_function_permission_checker = auth.has_change_permission(
        FUNCTION,
        (answer) => {
          this.has_change_function_permission = answer;
        }
      );

      var delete_function_permission_checker = auth.has_delete_permission(
        FUNCTION,
        (answer) => {
          this.has_delete_function_permission = answer;
        }
      );

      Promise.all([
        functions_fetcher,
        add_function_permission_checker,
        change_function_permission_checker,
        delete_function_permission_checker,
      ]).then(() => (this.initialized = true));
    },
    goToCreateFunctionPage() {
      this.$router.push({ name: "create-callback-function" });
    },
    goToViewFunctionPage(functionId) {
      this.$router.push({
        name: "view-callback-function",
        params: { id: functionId },
      });
    },
    goToEditFunctionPage(functionId) {
      this.$router.push({
        name: "edit-callback-function",
        params: { id: functionId },
      });
    },
    showDeletingDialog(_function) {
      this.deletingFunction = _function;
      this.deleteDialog = true;
    },
    deleteFunction() {
      if (this.deletingFunction) {
        http.delete(`/function/delete/${this.deletingFunction.id}/`, () => {
          this.fetchFunctions();
          this.deleteDialog = false;
          emit_success(`Function '${this.deletingFunction.name}' is deleted`);
        });
      }
    },
  },
};
</script>

<style>
body {
  background-color: #fcfcfc;
}
.fab_container {
  position: fixed;
  bottom: 45px;
  right: 30px;
}

.container {
  max-width: 100% !important;
}
.custom-width {
  width: 400px;
}
.custom-data-table {
  background-color: #f0f0f0;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.custom-row {
  background-color: #ffffff;
  color: #333333;
  border-radius: 16px;
  padding-inline-start: 48px;
}
.custom-row td {
  border-top: 0.5px solid #e4e4e4;
  border-bottom: 0.5px solid #e4e4e4 !important;
  padding: 24px 24px;
}
thead:after {
  content: "@";
  display: block;
  line-height: 24px;
  text-indent: -99999px;
}
.header-first-cell {
  padding-inline-start: 48px !important;
}
.hidden-header-cell span {
  visibility: hidden;
}
.v-data-table td {
  height: auto;
}
.custom-row:hover {
  background-color: #fafafa !important;
  border-radius: 16px !important;
  transition: all 200ms;
}
.page-header {
  text-align: start;
  margin-bottom: 0;
}

.page-header .v-icon {
  display: none;
}
.page-header {
  color: #121722;
}

.v-data-table-header thead {
  padding-block: 20px;
  border-radius: 16px;
}
.v-data-table-header th {
  background-color: #f6f6f6;
  color: #333333;
  font-weight: 700;
  font-size: 16px;
  padding: 24px;
  border-bottom: none !important;
}

.v-data-footer {
  justify-content: start;
  padding-inline: 40px;
}
.v-data-footer__select {
  flex: 1 1 0%;
  justify-content: start;
  color: #a0a2a7;
  font-size: 16px !important;
}
.v-data-footer__select .v-select {
  border: 1px solid #f1f1f1;
  background-color: #fafafa;
  padding: 8px;
  margin: 13px 0 13px 8px !important;
}
.v-data-footer__select .v-select__selections .v-select__selection--comma {
  font-size: 16px;
  color: #a0a2a7;
}
.v-data-footer__pagination {
  font-size: 16px;
  color: #a0a2a7;
}
.v-text-field > .v-input__control > .v-input__slot:before {
  border: none;
}
.v-input__icon .mdi:before {
  content: "\F140";
  font-size: 24px;
}
.v-dialog {
  border-radius: 16px !important;
}
.v-card {
  border-radius: 16px !important;
  box-shadow: -59px 170px 50px 0px #ffc1c100, -38px 109px 46px 0px #ffc1c103,
    -21px 61px 39px 0px #ffc1c10d, -10px 27px 29px 0px #ffc1c117,
    -2px 7px 16px 0px #ffc1c11a;
}
.custom-dialoge {
  background: #ffeff2 !important;
}
.custom-dialoge .headline,
.v-card .headline {
  padding: 40px !important;
}
</style>
