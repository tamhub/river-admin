<template>
    <section class="w-screen h-screen flex items-center justify-center">
        <SplashScreen />
    </section>
</template>

<script>
import { onMounted } from 'vue';
import SplashScreen from '@/components/SplashScreen';

export default {
    setup(props) {

        onMounted(() => {
        });

        return {};
    },
    components: {
        SplashScreen,
    },
    mounted() {
        if (this.$route.query.success) {
            this.$store.commit("unSetAuthToken");
        }
        this.$router.push({ name: "home" });
    },
};
</script>