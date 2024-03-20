<template>
  <v-container fluid>
    <v-row justify="center" align="center">
      <div class="w-full">
        <v-row justify="center" align="center">
          <v-icon style="font-size:150px">
            <slot name="icon"></slot>
          </v-icon>
        </v-row>

        <v-row justify="center" align="center">
          <slot name="customIcon"></slot>
        </v-row>

        <v-row v-if="label" justify="center" align="center">
          <v-col justify="center" align="center">
            <p class="subtitle-1">{{ label }}</p>
          </v-col>
        </v-row>
        <v-row v-if="description" justify="center" align="center">
          <v-col justify="center" align="center">
            <p class="subtitle-3">{{ description }}</p>
          </v-col>
        </v-row>
        <v-row justify="center" align="center">
          <v-col justify="center" align="center">
            <slot name="content"></slot>
          </v-col>
        </v-row>
      </div>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "EmptyState",
  props: ["label", "description"]
};
</script>