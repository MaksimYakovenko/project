<script setup>
import {installInterceptors} from "@/utils/interseptors.js";
import {onMounted} from "vue";
import {useAuthStore} from "@/stores/authStore.js";

installInterceptors();

const authStore = useAuthStore();
onMounted(async () => {
  try {
    await authStore.refreshAccessToken();
    if (authStore.access) {
      await authStore.loadUser();
    }
  } catch (e) {
    console.error("Error during initialization:", e);
  }
});
</script>

<template>
  <router-view />
</template>

<style scoped>
</style>
