<!-- views/Login.vue -->
<script setup>
import {ref} from "vue";
import {useAuthStore} from "@/stores/authStore.js";
import router from "@/utils/router.js";

const authStore = useAuthStore();

const form = ref({
  username: "",
  password: ""
});
const error = ref(null);
const loading = ref(false);

async function handleLogin() {
  error.value = null;
  loading.value = true;

  try {
    const ok = await authStore.login(form.value.username, form.value.password);
    if (ok)
      await router.push({name: "Home"});

  } catch (e) {
    console.log(e);
    error.value = "Хибне імʼя користувача або пароль!";
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <div v-if="error" v-text="error" class="alert alert-danger"></div>
  <h1>Вхід</h1>
  <form @submit.prevent="handleLogin" class="flex flex-col gap-4 max-w-md">
    <div class="form-group">
      <label>
        Логін
        <input class="form-control" type="text" v-model="form.username" required>
      </label>
    </div>
    <div class="form-group">
      <label>
        Пароль
        <input class="form-control" type="password" v-model="form.password" required>
      </label>
    </div>
    <div class="form-group">
      <input
          class="btn btn-success"
          type="button"
          :disabled="loading"
          :value="loading ? 'Зачекайте' : 'Увійти' "
          @click="handleLogin"
      >
    </div>

  </form>
</template>