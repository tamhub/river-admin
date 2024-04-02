import Vue from "vue";
import App from "@/App.vue";
import vuetify from "@/vuetify";
import store from "@/store";
import router from "@/routers";
import VueMoment from "vue-moment";

// import "@/assets/css/main.css";

Vue.config.productionTip = false;

Vue.use(VueMoment);

new Vue({
  store,
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
