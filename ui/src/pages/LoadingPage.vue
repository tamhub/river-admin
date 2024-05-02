<template>
    <SplashScreen />
</template>

<script>
import SplashScreen from '@/components/SplashScreen';
import { auth, WORKFLOW } from "@/helpers/auth";
import { emit_error } from "@/helpers/event_bus";
import axios from "axios";
import { TENANT } from "@/helpers/constants";
export default {
    props: {
        refetch: Function
    },
    mounted() {
        const urlParams = new URLSearchParams(window.location.search);
        const params = Object.fromEntries(urlParams.entries());
        const tokenParam = params.t;
        if (tokenParam) {
            const token = JSON.parse(tokenParam.replaceAll("'", '"'));
            // Cookies.set("access_token", token.access);
            // Cookies.set("refresh_token", token.refresh);
            console.log(token);

            if (token.access) {

                this.$store.commit("setAuthToken", token.access);
                auth.has_view_permission(WORKFLOW, yes => {
                    if (yes) {
                        if (this.$route.params.nextUrl) {
                            window.location.href = `${window.location.origin}/${TENANT}`;
                        } else {
                            window.location.href = `${window.location.origin}/${TENANT}`;
                        }
                    } else {
                        this.$store.commit("initLogout");
                        emit_error(["You must have the permission to view the workflows!"], 10000);
                    }
                    console.log(yes);
                });
            }
            else {
                this.$store.commit("initLogout");
            }
        }


        setTimeout(() => {
            window.location.href = `${window.location.origin}/${TENANT}`;
        }, 1000);

    },
    components: {
        SplashScreen
    }
};
</script>
