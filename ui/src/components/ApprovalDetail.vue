<template>
  <v-container>
    <div class="bg-white rounded-lg shadow-md px-4 pt-4 py-2">
      <div class="w-full flex">
        <button class="column-drag-handle mb-1 mr-3" v-if="editable">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M2 12H14" stroke="#A0A2A7" stroke-width="0.75" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M2 8H14" stroke="#A0A2A7" stroke-width="0.75" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M2 4H14" stroke="#A0A2A7" stroke-width="0.75" stroke-linecap="round" stroke-linejoin="round" />
          </svg>

        </button>
        <!-- <v-icon class="mb-1 mr-3">mdi-account-multiple-check</v-icon> -->
        <span class=" flex items-center gap-2 text-[#595D64] !text-base">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_23_1648)">
              <path
                d="M14.6668 7.38674V8.00007C14.666 9.43769 14.2005 10.8365 13.3397 11.988C12.4789 13.1394 11.269 13.9817 9.8904 14.3893C8.51178 14.797 7.03834 14.748 5.68981 14.2498C4.34128 13.7516 3.18993 12.8308 2.40747 11.6248C1.62501 10.4188 1.25336 8.99212 1.34795 7.55762C1.44254 6.12312 1.9983 4.75762 2.93235 3.66479C3.8664 2.57195 5.12869 1.81033 6.53096 1.4935C7.93323 1.17668 9.40034 1.32163 10.7135 1.90674"
                stroke="#41454E" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M14.6667 2.66675L8 9.34008L6 7.34008" stroke="#41454E" stroke-linecap="round"
                stroke-linejoin="round" />
            </g>
            <defs>
              <clipPath id="clip0_23_1648">
                <rect width="16" height="16" fill="white" />
              </clipPath>
            </defs>
          </svg>

          Approved by...</span>
        <div class="flex-grow-1" />

        <v-speed-dial v-if="editable" v-model="fab" direction="left">
          <template v-slot:activator>
            <button>
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M11.333 2.00004C11.5081 1.82494 11.716 1.68605 11.9447 1.59129C12.1735 1.49653 12.4187 1.44775 12.6663 1.44775C12.914 1.44775 13.1592 1.49653 13.3879 1.59129C13.6167 1.68605 13.8246 1.82494 13.9997 2.00004C14.1748 2.17513 14.3137 2.383 14.4084 2.61178C14.5032 2.84055 14.552 3.08575 14.552 3.33337C14.552 3.58099 14.5032 3.82619 14.4084 4.05497C14.3137 4.28374 14.1748 4.49161 13.9997 4.66671L4.99967 13.6667L1.33301 14.6667L2.33301 11L11.333 2.00004Z"
                  stroke="#121722" stroke-width="0.75" stroke-linecap="round" stroke-linejoin="round" />
              </svg>

            </button>
          </template>

          <v-tooltip top>
            <template v-slot:activator="{ on }">
              <v-btn fab dark small v-on="on" color="green" @click="newHookDialog = true">
                <v-icon>mdi-function-variant</v-icon>
              </v-btn>
            </template>
            <span>Create Approval Hook</span>
          </v-tooltip>

          <v-tooltip top>
            <template v-slot:activator="{ on }">
              <v-btn fab dark small v-on="on" color="warning" @click="delete_approval()">
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </template>
            <span>Delete Approval Step</span>
          </v-tooltip>
        </v-speed-dial>
      </div>
      <div class="px-4">
        <div>
          <div class="">
            <v-row class="permissions-lane pl-4" v-if="approval.permissions.length > 0">
              <v-col>
                <span v-bind:key="permission.id" v-for="(permission, index) in approval.permissions">
                  <span
                    class="bg-[#E5E9F7] text-base mb-2 text-[#0028B3]  px-2.5 py-1 rounded-full truncate select-none inline-flex items-center gap-2">
                    <!-- <v-icon left>mdi-lock</v-icon> -->
                    <span v-text="permission.identifier || permission.codename"></span>
                  </span>
                  <span v-if="index != approval.permissions.length - 1">, </span>
                </span>
              </v-col>
            </v-row>
            <v-row class="groups-lane" v-if="approval.groups.length > 0">
              <v-col cols="4">
                <label>are in groups:</label>
              </v-col>
              <v-col>
                <span v-bind:key="group.id" v-for="(group, index) in approval.groups">
                  <span
                    class="bg-[#E5E9F7] text-base text-[#0028B3]  px-2.5 py-1 rounded-full truncate select-none inline-flex items-center gap-2">
                    <v-icon left>mdi-account-multiple</v-icon>
                    <span v-text="group.name"></span>
                  </span>
                  <span v-if="index != approval.groups.length - 1">or</span>
                </span>
              </v-col>
            </v-row>
            <v-row>
              <v-container class="border border-[#E4E4E4] rounded-lg mb-3" v-if="approval.hooks.length > 0" fluid style="box-shadow: -10px 27px 29px 0px #BFBFBF17;
">
                <span class="flex items-center justify-start gap-2 text-[#595D64] text-base ">
                  <svg width="14" height="16" viewBox="0 0 14 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7.66667 1.33325L1 9.33325H7L6.33333 14.6666L13 6.66658H7L7.66667 1.33325Z"
                      stroke="#595D64" stroke-linecap="round" stroke-linejoin="round" />
                  </svg>

                  After approval...
                </span>
                <div class="my-2" v-for="hook in approval.hooks" :key="hook.id">
                  <HookDetail :hook="hook" :editable="editable" @on-delete="() => on_hook_deleted(hook)" />
                </div>
              </v-container>
            </v-row>
          </div>
        </div>
      </div>
    </div>
    <v-dialog v-model="newHookDialog" max-width="800">
      <CreateApprovalHookForm :workflow="workflow" :transition_approval_meta_id="approval.id"
        :excluded_function_ids="approval.hooks.map(hook => hook.callback_function.id)" @on-create="on_hook_created" />
    </v-dialog>
  </v-container>
</template>

<script>
import { Approval } from "@/models/models";
import HookDetail from "@/components/HookDetail.vue";
import CreateApprovalHookForm from "@/components/CreateApprovalHookForm.vue";

export default {
  name: "ApprovalDetail",
  components: {
    HookDetail,
    CreateApprovalHookForm
  },
  props: ["workflow", "approval", "editable"],
  data: () => ({
    fab: false,
    newHookDialog: false
  }),
  methods: {
    delete_approval() {
      this.$emit("on-delete", this.approval);
    },
    on_hook_created(created_hook) {
      this.$emit("on-hook-create", created_hook);
      this.newHookDialog = false;
    },
    on_hook_deleted(deleted_hook) {
      this.$emit("on-hook-delete", deleted_hook);
    }
  }
};
</script>
