<template>
  <span class="inline">
    <span :class="hook.is_executed ? 'executed' : (!editable ? 'not-editable' : '')">
      <span v-if="hook.is_executed" class="">

        <span
          class="bg-[#4caf4f21] inline-block text-base text-[#4caf4fab]  px-2.5 py-1 rounded-full truncate select-none">{{
      hook.callback_function.name }}</span>
      </span>

      <span v-else class="">

        <span
          class="bg-[#ECF5FB] inline-block text-base text-[#4397D8]  px-2.5 py-1 rounded-full truncate select-none ">
          <span class="flex items-center gap-2">
            {{ hook.callback_function.name }}
            <button v-show="editable && !hook.is_executed" @click="deleteStep()">
              <svg width="24" height="24" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M0.5 16C0.5 7.43959 7.43959 0.5 16 0.5C24.5604 0.5 31.5 7.43959 31.5 16C31.5 24.5604 24.5604 31.5 16 31.5C7.43959 31.5 0.5 24.5604 0.5 16Z"
                  stroke="#E33554" />
                <path d="M10 12H11.3333H22" stroke="#E33554" stroke-linecap="round" stroke-linejoin="round" />
                <path
                  d="M13.333 11.9999V10.6666C13.333 10.313 13.4735 9.97382 13.7235 9.72378C13.9736 9.47373 14.3127 9.33325 14.6663 9.33325H17.333C17.6866 9.33325 18.0258 9.47373 18.2758 9.72378C18.5259 9.97382 18.6663 10.313 18.6663 10.6666V11.9999M20.6663 11.9999V21.3333C20.6663 21.6869 20.5259 22.026 20.2758 22.2761C20.0258 22.5261 19.6866 22.6666 19.333 22.6666H12.6663C12.3127 22.6666 11.9736 22.5261 11.7235 22.2761C11.4735 22.026 11.333 21.6869 11.333 21.3333V11.9999H20.6663Z"
                  stroke="#E33554" stroke-linecap="round" stroke-linejoin="round" />
              </svg>

            </button>
          </span>

        </span>
      </span>

    </span>
  </span>
</template>


<script>
export default {
  name: "HookDetail",
  props: ["hook", "editable"],
  methods: {
    deleteStep() {
      this.$emit("on-delete", this.hook);
    }
  }
};
</script>

<style>
/* .executed {
  background-color: #4caf5069;
} */

/* .not-editable {
  background-color: aliceblue;
} */
</style>