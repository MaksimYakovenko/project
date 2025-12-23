<!-- views/Login.vue -->
<script setup>
import {ref} from "vue";
import {useAuthStore} from "@/stores/authStore.js";
import router from "@/utils/routers.js";

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
  <div class="login-page">
    <div class="login-container">
      <h1>Вхід</h1>

      <div v-if="error" class="alert alert-danger">
        {{ error }}
      </div>

      <form @submit.prevent="handleLogin" class="login-form">
        <div class="form-group">
          <label for="username">Логін</label>
          <input
            id="username"
            v-model="form.username"
            type="text"
            class="form-control"
            required
          />
        </div>

        <div class="form-group">
          <label for="password">Пароль</label>
          <input
            id="password"
            v-model="form.password"
            type="password"
            class="form-control"
            required
          />
        </div>

        <button
          type="submit"
          class="btn btn-primary"
          :disabled="loading"
        >
          {{ loading ? 'Зачекайте...' : 'Увійти' }}
        </button>
      </form>

      <div class="register-link">
        Немає акаунту?
        <router-link to="/register">Зареєструватися</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.login-container {
  background: white;
  border-radius: 12px;
  padding: 40px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 400px;
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
  font-size: 2em;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 500;
  color: #555;
  font-size: 0.95em;
}

.form-control {
  padding: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1em;
  transition: border-color 0.3s;
  width: 100%;
}

.form-control:focus {
  outline: none;
  border-color: #667eea;
}

.btn {
  padding: 14px;
  border: none;
  border-radius: 8px;
  font-size: 1em;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
  width: 100%;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.alert {
  padding: 12px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.alert-danger {
  background-color: #fee;
  color: #c33;
  border: 1px solid #fcc;
}

.register-link {
  text-align: center;
  margin-top: 20px;
  color: #666;
}

.register-link a {
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
}

.register-link a:hover {
  text-decoration: underline;
}

@media (max-width: 480px) {
  .login-container {
    padding: 30px 20px;
  }

  h1 {
    font-size: 1.5em;
  }
}
</style>
