<template>
  <div class="register-page">
    <div class="register-container">
      <h1>Реєстрація</h1>

      <div v-if="error" class="alert alert-danger">
        {{ error }}
      </div>

      <form @submit.prevent="handleRegister" class="register-form">
        <div class="form-group">
          <label for="username">Логін</label>
          <input
            id="username"
            v-model="form.username"
            type="text"
            class="form-control"
            required
            minlength="3"
          />
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
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
            minlength="6"
          />
        </div>

        <div class="form-group">
          <label for="password2">Підтвердіть пароль</label>
          <input
            id="password2"
            v-model="form.password2"
            type="password"
            class="form-control"
            required
            minlength="6"
          />
        </div>

        <button
          type="submit"
          class="btn btn-primary"
          :disabled="loading"
        >
          {{ loading ? 'Зачекайте...' : 'Зареєструватися' }}
        </button>
      </form>

      <div class="login-link">
        Вже є акаунт?
        <router-link to="/login">Увійти</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/authStore.js';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();

const form = ref({
  username: '',
  email: '',
  password: '',
  password2: ''
});

const error = ref(null);
const loading = ref(false);

async function handleRegister() {
  error.value = null;

  // Перевірка паролів
  if (form.value.password !== form.value.password2) {
    error.value = 'Паролі не співпадають';
    return;
  }

  loading.value = true;

  try {
    await authStore.register(
      form.value.username,
      form.value.email,
      form.value.password
    );
    // Після успішної реєстрації перенаправляємо на головну
    router.push({ name: 'Home' });
  } catch (e) {
    console.error(e);
    if (e.response?.data) {
      // Показуємо помилки з бекенду
      const errors = e.response.data;
      if (errors.username) {
        error.value = `Логін: ${errors.username[0]}`;
      } else if (errors.email) {
        error.value = `Email: ${errors.email[0]}`;
      } else if (errors.password) {
        error.value = `Пароль: ${errors.password[0]}`;
      } else {
        error.value = 'Помилка реєстрації. Спробуйте ще раз.';
      }
    } else {
      error.value = 'Помилка реєстрації. Спробуйте ще раз.';
    }
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.register-container {
  background: white;
  border-radius: 12px;
  padding: 40px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 450px;
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
  font-size: 2em;
}

.register-form {
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

.login-link {
  text-align: center;
  margin-top: 20px;
  color: #666;
}

.login-link a {
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
}

.login-link a:hover {
  text-decoration: underline;
}

@media (max-width: 480px) {
  .register-container {
    padding: 30px 20px;
  }

  h1 {
    font-size: 1.5em;
  }
}
</style>

