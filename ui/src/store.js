import Vuex from "vuex";
import Vue from "vue";
import { BASE_URL, TENANT } from "@/helpers/constants";
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user: {},
  },
  mutations: {
    initialiseStore(state) {
      if (localStorage.getItem("store")) {
        this.replaceState(
          Object.assign(state, JSON.parse(localStorage.getItem("store")))
        );
      }
    },
    setAuthToken(state, token) {
      state.user.token = token;
    },
    unSetAuthToken(state) {
      state.user.token = null;
    },
    initLogout(state) {
      const extra = `/${TENANT}`;
      const logoutUrl = `${BASE_URL}/auth/logout?next=${window.location.origin}${extra}/logout?success=true`;

      window.location.replace(logoutUrl);
    },
  },
});

store.subscribe((mutation, state) => {
  localStorage.setItem("store", JSON.stringify(state));
});

export default store;
