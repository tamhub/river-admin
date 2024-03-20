import Vue from "vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import "@mdi/font/css/materialdesignicons.css";

Vue.use(Vuetify);

const opts = {
  iconfont: "mdi",
  theme: {
    themes: {
      light: {
        primary: "#5E45FF",
      },
    },
  },
};

export default new Vuetify(opts);
