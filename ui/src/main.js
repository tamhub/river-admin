import Vue from "vue";
import App from "@/App.vue";
import vuetify from "@/vuetify";
import store from "@/store";
import router from "@/routers";

// import "@/assets/css/main.css";

Vue.config.productionTip = false;

new Vue({
  store,
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
