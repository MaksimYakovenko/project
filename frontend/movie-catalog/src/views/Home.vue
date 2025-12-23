<template>
  <div class="home">
    <div class="header">
      <div class="header-content">
        <h1>Каталог фільмів</h1>
        <div class="header-actions">
          <div v-if="authStore.user" class="user-info">
            <span class="username">Привіт, {{ authStore.user.username }}!</span>
            <button @click="handleLogout" class="btn btn-danger">Вийти</button>
          </div>
          <div v-else>
            <router-link to="/login" class="btn btn-primary">Увійти</router-link>
          </div>
        </div>
      </div>
          <div v-else>
            <router-link to="/login" class="btn btn-primary">Увійти</router-link>
    <div class="container">
      <div class="movies-list">
        <p>Тут буде список фільмів...</p>
      </div>
      </div>
          </div>
          <div v-else>
    <div class="container">
      <div class="movies-list">
        <p>Тут буде список фільмів...</p>
      </div>
        </div>
      </div>
    </div>

    <div class="container">
      <MovieFilters @filter-change="loadMovies" />

      <div v-if="moviesStore.loading" class="loading">
        <p>⏳ Завантаження фільмів...</p>
      </div>

      <div v-else-if="moviesStore.error" class="error">
        <p>❌ {{ moviesStore.error }}</p>
      </div>

      <div v-else-if="moviesStore.movies.length === 0" class="empty">
  min-height: 100vh;
  background: #f5f5f5;
}

.header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 24px 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
}

.header h1 {
  margin: 0;
  font-size: 2em;
}

.header-actions {
  display: flex;
  gap: 12px;
  align-items: center;
      </div>

      <div v-else class="movies-grid">
  display: flex;
  gap: 12px;
  align-items: center;
}

.username {
  font-weight: 500;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px 20px;
}

.movies-list {
  margin-top: 30px;
  background: #f5f5f5;
}

.header {
  color: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-size: 0.95em;
}

  transition: all 0.3s;
  font-weight: 500;
.header-content {
  max-width: 1200px;
  margin: 0 auto;
  background: white;
  color: #667eea;
}

.btn-primary:hover {
  background: #f0f0f0;
}

.btn-success {
  background: #4caf50;
  display: flex;
  justify-content: space-between;
  align-items: center;
.btn-success:hover {
  background: #45a049;
}

  flex-wrap: wrap;
  background: #f44336;
}

.header h1 {
.btn-danger:hover {
  background: #d32f2f;
}

.loading,
.error,
.empty {
  text-align: center;
  padding: 48px 20px;
  font-size: 1.2em;
  color: #666;
}

.error {
  color: #f44336;
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    text-align: center;
  }

  .movies-grid {
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 16px;
  }
}

.header-actions {
  display: flex;
  gap: 12px;
  align-items: center;
        />
      </div>
    </div>
  display: flex;
  gap: 12px;
  align-items: center;
}

.username {
  font-weight: 500;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px 20px;
}

.movies-list {
  margin-top: 30px;
}

.movies-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
import { onMounted } from 'vue';
import { useAuthStore } from '@/stores/authStore.js';
import { useMoviesStore } from '@/stores/moviesStore.js';
import { useRouter } from 'vue-router';
import MovieFilters from '@/components/MovieFilters.vue';
  border-radius: 8px;
const authStore = useAuthStore();
  font-size: 0.95em;
const moviesStore = useMoviesStore();
const router = useRouter();
  transition: all 0.3s;
  font-weight: 500;

onMounted(async () => {
  await loadMovies();
  background: white;
  color: #667eea;
}

.btn-primary:hover {
  background: #f0f0f0;
}

.btn-success {
  background: #4caf50;

async function loadMovies() {
  await moviesStore.fetchMovies();
.btn-success:hover {
  background: #45a049;
}

}
  background: #f44336;
async function handleLogout() {
  try {
    await authStore.logout();
.btn-danger:hover {
  background: #d32f2f;
}

.loading,
.error,
.empty {
  text-align: center;
  padding: 48px 20px;
  font-size: 1.2em;
  color: #666;
}

.error {
  color: #f44336;
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    text-align: center;
  }

  .movies-list {
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 16px;
  }
    console.error("Помилка при виході:", e);
  }
}
</script>

<style scoped>
.home {
  min-height: 100vh;
  background: #f5f5f5;
}

.header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 24px 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
}

.header h1 {
  margin: 0;
  font-size: 2em;
}

.header-actions {
  display: flex;
  gap: 12px;
  align-items: center;
}

.user-info {
  display: flex;
  gap: 12px;
  align-items: center;
}

.username {
  font-weight: 500;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px 20px;
}

.movies-list {
  margin-top: 30px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.95em;
  text-decoration: none;
  display: inline-block;
  transition: all 0.3s;
  font-weight: 500;
}

.btn-primary {
  background: white;
  color: #667eea;
}

.btn-primary:hover {
  background: #f0f0f0;
}

.btn-success {
  background: #4caf50;
  color: white;
}

.btn-success:hover {
  background: #45a049;
}

.btn-danger {
  background: #f44336;
  color: white;
}

.btn-danger:hover {
  background: #d32f2f;
}

.loading,
.error,
.empty {
  text-align: center;
  padding: 48px 20px;
  font-size: 1.2em;
  color: #666;
}

.error {
  color: #f44336;
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    text-align: center;
  }

  .movies-list {
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 16px;
  }
}
</style>

