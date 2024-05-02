<template>
  <component :is="layout" id="app">
    <v-row align="center">
      <v-col>
        <router-view />
      </v-col>
    </v-row>

    <v-snackbar class="mt-10" v-model="show_snackbar" :color="snackbar_color" :top="true" :timeout="snackbar_timeout">
      <v-icon color="white" left>{{ snackbar_icon }}</v-icon>
      <v-container>
        <v-row v-for="(snackbar_text, index) in snackbar_texts" v-bind:key="index">
          <v-col>{{ snackbar_text }}</v-col>
        </v-row>
      </v-container>
      <v-btn dark text @click="show_snackbar = false">Close</v-btn>
    </v-snackbar>
  </component>
</template>

<script>
import NotLoggedInLayout from "@/layouts/NotLoggedInLayout.vue";
import LoggedInLayout from "@/layouts/LoggedInLayout.vue";
import { on_logout, on_error, on_success } from "@/helpers/event_bus";

const defaultLayout = "LoggedInLayout";

export default {
  name: "app",
  components: {
    LoggedInLayout,
    NotLoggedInLayout
  },
  computed: {
    layout() {
      return this.$route.meta.layout || defaultLayout;
    }
  },
  mounted() {
    var that = this;

    on_logout(() => {
      this.$store.commit("initLogout");
    });

    on_error((errors, timeout) => {
      if (timeout) {
        this.snackbar_timeout = timeout;
      } else {
        this.snackbar_timeout = this.default_snackbar_timeout;
      }
      that.error(errors);
    });

    on_success((message, timeout) => {
      if (timeout) {
        this.snackbar_timeout = timeout;
      } else {
        this.snackbar_timeout = this.default_snackbar_timeout;
      }
      that.success([message]);
    });
  },
  data: () => ({
    show_snackbar: false,
    snackbar_icon: null,
    snackbar_timeout: null,
    snackbar_color: "grey",
    snackbar_texts: null,
    default_snackbar_timeout: 4000
  }),
  methods: {
    success(messages) {
      this.snackbar_icon = "mdi-check-all";
      this.snackbar_texts = messages;
      this.snackbar_color = "success";
      this.show_snackbar = true;
    },

    error(messages) {
      this.snackbar_icon = "mdi-shield-half-full";
      this.snackbar_texts = messages;
      this.snackbar_color = "error";
      this.show_snackbar = true;
    },
  }
};
</script>

<style>
/* .row {
  width: 100%;
}*/
h1,
h2,
h3,
h4,
h5,
h6 {
  color: #121722;
}

.flex {
  flex-wrap: wrap;
}

.v-btn__content {
  display: flex;
  gap: 5px;
}

g.node-default>rect {
  fill: #fff !important;
  stroke: #D2D2D2 !important;
  stroke-width: 1px !important;
  border-radius: 50% !important;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

@media (min-width: 2000px) {
  .container {
    margin-left: 0px !important;
    max-width: 100% !important;

  }
}

/* For Chrome, Safari, and Edge */
::-webkit-scrollbar {
  width: 10px;
  /* Adjust the width of the scrollbar */
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
  /* The track (progress background) */
}

::-webkit-scrollbar-thumb {
  background: #888;
  /* Scroll handle */
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
  /* Scroll handle on hover */
}

::-moz-scrollbar-button:decrement,
::-moz-scrollbar-button:increment,
::-webkit-scrollbar-button:decrement,
::-webkit-scrollbar-button:increment {
  width: 0px;
}

::-moz-scrollbar-button,
::-webkit-scrollbar-button {
  width: 0px;
}

/* For Firefox */
* {
  scrollbar-width: thin;
  /* "auto" or "thin" */
  scrollbar-color: #888 #f1f1f1;
  /* thumb and track color */
}

.v-application .custom-data-table.elevation-1,
.v-application .v-data-table .elevation-1 {
  box-shadow: none !important;

}

.v-application .custom-data-table.elevation-1 {}

.custom-data-table {
  background-color: #f0f0f0;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.custom-row {
  background-color: #ffffff;
  color: #333333;
  border-radius: 16px !important;
  /* padding-inline-start: 48px; */

}

.custom-row td {
  border-top: 0.5px solid #e4e4e4;
  border-bottom: 0.5px solid #e4e4e4 !important;
  padding: 24px 24px;

}

.theme--light.v-data-table .v-data-footer {
  border-top: none !important;
}


.custom-row:last-child td:last-child {
  border-right: 0.5px solid #e4e4e4;
}

thead:after {
  content: "@";
  display: block;
  line-height: 24px;
  text-indent: -99999px;
}

.header-first-cell {
  /* padding-inline-start: 48px !important; */
}

.hidden-header-cell span {
  visibility: hidden;
}

.custom-row:hover {
  border-radius: 16px !important;
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

.v-text-field>.v-input__control>.v-input__slot:before {
  border: none;
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

table {
  border-collapse: collapse !important;
  border-spacing: 0 1em !important;
}

tr td {
  border: 0px solid transparent !important;
  padding: 10px !important;
}

tr th:first-child {
  border-top-left-radius: 16px;
  border-bottom-left-radius: 16px;
}

tr th:last-child {
  border-top-right-radius: 16px;
  border-bottom-right-radius: 16px;
}
</style>
