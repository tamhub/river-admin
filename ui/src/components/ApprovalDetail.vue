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

          Triggered by...</span>
        <div class="flex-grow-1" />

        <div class="flex items-center justify-end gap-2">
          <button v-if="allowEditing" @click="delete_approval()">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M0.5 16C0.5 7.43959 7.43959 0.5 16 0.5C24.5604 0.5 31.5 7.43959 31.5 16C31.5 24.5604 24.5604 31.5 16 31.5C7.43959 31.5 0.5 24.5604 0.5 16Z"
                stroke="#E33554" />
              <path d="M10 12H11.3333H22" stroke="#E33554" stroke-linecap="round" stroke-linejoin="round" />
              <path
                d="M13.333 11.9999V10.6666C13.333 10.313 13.4735 9.97382 13.7235 9.72378C13.9736 9.47373 14.3127 9.33325 14.6663 9.33325H17.333C17.6866 9.33325 18.0258 9.47373 18.2758 9.72378C18.5259 9.97382 18.6663 10.313 18.6663 10.6666V11.9999M20.6663 11.9999V21.3333C20.6663 21.6869 20.5259 22.026 20.2758 22.2761C20.0258 22.5261 19.6866 22.6666 19.333 22.6666H12.6663C12.3127 22.6666 11.9736 22.5261 11.7235 22.2761C11.4735 22.026 11.333 21.6869 11.333 21.3333V11.9999H20.6663Z"
                stroke="#E33554" stroke-linecap="round" stroke-linejoin="round" />
            </svg>

          </button>
          <button v-if="editable" @click="allowEditing = !allowEditing">
            <span v-if="!allowEditing" class="w-8 h-8 flex items-center justify-center">


              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_24_1831)">
                  <path
                    d="M11.334 2.00004C11.5091 1.82494 11.7169 1.68605 11.9457 1.59129C12.1745 1.49653 12.4197 1.44775 12.6673 1.44775C12.9149 1.44775 13.1601 1.49653 13.3889 1.59129C13.6177 1.68605 13.8256 1.82494 14.0007 2.00004C14.1757 2.17513 14.3146 2.383 14.4094 2.61178C14.5042 2.84055 14.5529 3.08575 14.5529 3.33337C14.5529 3.58099 14.5042 3.82619 14.4094 4.05497C14.3146 4.28374 14.1757 4.49161 14.0007 4.66671L5.00065 13.6667L1.33398 14.6667L2.33398 11L11.334 2.00004Z"
                    stroke="#121722" stroke-linecap="round" stroke-linejoin="round" />
                </g>
                <defs>
                  <clipPath id="clip0_24_1831">
                    <rect width="16" height="16" fill="white" />
                  </clipPath>
                </defs>
              </svg>

            </span>
            <svg v-else width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M0 16C0 7.16344 7.16344 0 16 0C24.8366 0 32 7.16344 32 16C32 24.8366 24.8366 32 16 32C7.16344 32 0 24.8366 0 16Z"
                fill="#5E45FF" />
              <path d="M21.3332 12L13.9998 19.3333L10.6665 16" stroke="white" stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>


          </button>

        </div>

        <!-- <v-speed-dial v-if="editable" v-model="fab" direction="left">
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


</v-speed-dial> -->
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
            <v-row class="groups-lane pl-4" v-if="approval.groups.length > 0">
              <v-col class="pb-0" cols="12">
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

                  Or users who are in groups...</span>
              </v-col>
              <v-col>
                <span v-bind:key="group.id" v-for="(group, index) in approval.groups">
                  <span
                    class="bg-[#E5E9F7] text-base mb-2 text-[#0028B3]  px-2.5 py-1 rounded-full truncate select-none inline-flex items-center gap-2">
                    <span v-text="group.name"></span>
                  </span>
                  <span v-if="index != approval.groups.length - 1">, </span>
                </span>
              </v-col>
            </v-row>
            <v-row v-if="allowEditing">
              <v-btn class="rounded-full mt-0.5 max-w-none w-full mb-3" large color="primary" outlined
                @click="newHookDialog = true">
                <span class="flex w-full items-center gap-2 justify-between">


                  <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M8.66667 1.33325L2 9.33325H8L7.33333 14.6666L14 6.66658H8L8.66667 1.33325Z"
                      stroke="#5E45FF" stroke-linecap="round" stroke-linejoin="round" />
                  </svg>

                  <span class="font-bold capitalize">

                    Add Transition Hook
                  </span>
                  <span></span>
                </span>
              </v-btn>
            </v-row>
            <v-row>
              <v-container class="border border-[#E4E4E4] rounded-lg mb-3 approval-shadow"
                v-if="approval.hooks.length > 0" fluid style="box-shadow: -10px 27px 29px 0px #BFBFBF17;
">
                <span class="flex items-center justify-start gap-2 text-[#595D64] text-base ">
                  <svg width="14" height="16" viewBox="0 0 14 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7.66667 1.33325L1 9.33325H7L6.33333 14.6666L13 6.66658H7L7.66667 1.33325Z"
                      stroke="#595D64" stroke-linecap="round" stroke-linejoin="round" />
                  </svg>

                  After approval...
                </span>
                <div class="my-2" v-for="hook in approval.hooks" :key="hook.id">
                  <HookDetail :hook="hook" :editable="editable && allowEditing"
                    @on-delete="() => on_hook_deleted(hook)" />
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
    newHookDialog: false,
    allowEditing: false
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


<style>
.approval-shadow {
  box-shadow: -10px 27px 29px 0px #BFBFBF17;
}
</style>
