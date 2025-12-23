<template>
  <div class="movie-detail">
    <div class="container">
      <button @click="goBack" class="btn-back">← Назад до каталогу</button>

      <div v-if="moviesStore.loading" class="loading">
        <p>⏳ Завантаження...</p>
      </div>

      <div v-else-if="moviesStore.error" class="error">
        <p>❌ {{ moviesStore.error }}</p>
      </div>

      <div v-else-if="movie" class="movie-content">
        <div class="movie-header">
          <div class="movie-poster-large">
            <div class="movie-year-large">{{ movie.year }}</div>
          </div>

          <div class="movie-info-main">
            <h1>{{ movie.title }}</h1>

            <div class="movie-meta">
              <span class="meta-item">
                <strong>Жанр:</strong> {{ movie.genre_name }}
              </span>
              <span class="meta-item">
                <strong>Режисер:</strong> {{ movie.director_name }}
              </span>
              <span class="meta-item">
                <strong>Рік:</strong> {{ movie.year }}
              </span>
            </div>

            <div v-if="authStore.user && authStore.user.username === 'admin'" class="actions">
              <router-link :to="`/movies/${movie.id}/edit`" class="btn btn-warning">
                ✏️ Редагувати
              </router-link>
              <button @click="confirmDelete" class="btn btn-danger">
                🗑️ Видалити
              </button>
            </div>
          </div>
        </div>

        <div class="movie-description">
          <h2>Опис</h2>
          <p>{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useMoviesStore } from '@/stores/moviesStore.js';
import { useAuthStore } from '@/stores/authStore.js';

const route = useRoute();
const router = useRouter();
const moviesStore = useMoviesStore();
const authStore = useAuthStore();

const movie = computed(() => moviesStore.currentMovie);

onMounted(async () => {
  await moviesStore.fetchMovie(route.params.id);
});

function goBack() {
  router.push({ name: 'Home' });
}

async function confirmDelete() {
  if (confirm(`Ви впевнені, що хочете видалити фільм "${movie.value.title}"?`)) {
    try {
      await moviesStore.deleteMovie(movie.value.id);
      router.push({ name: 'Home' });
    } catch (error) {
      alert('Помилка при видаленні фільму');
    }
  }
}
</script>

<style scoped>
.movie-detail {
  min-height: 100vh;
  background: #f5f5f5;
  padding: 24px 0;
}

.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
}

.btn-back {
  background: white;
  border: 2px solid #e0e0e0;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1em;
  margin-bottom: 24px;
  transition: all 0.3s;
}

.btn-back:hover {
  background: #f5f5f5;
  border-color: #667eea;
}

.movie-content {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.movie-header {
  display: flex;
  gap: 32px;
  padding: 32px;
  flex-wrap: wrap;
}

.movie-poster-large {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  width: 300px;
  height: 400px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.movie-year-large {
  background: rgba(255, 255, 255, 0.95);
  padding: 16px 32px;
  border-radius: 50px;
  font-size: 2em;
  font-weight: bold;
  color: #667eea;
}

.movie-info-main {
  flex: 1;
  min-width: 300px;
}

.movie-info-main h1 {
  margin: 0 0 24px 0;
  font-size: 2.5em;
  color: #333;
}

.movie-meta {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 24px;
}

.meta-item {
  font-size: 1.1em;
  color: #666;
}

.meta-item strong {
  color: #333;
  margin-right: 8px;
}

.actions {
  display: flex;
  gap: 12px;
  margin-top: 24px;
}

.movie-description {
  padding: 32px;
  border-top: 1px solid #e0e0e0;
}

.movie-description h2 {
  margin: 0 0 16px 0;
  color: #333;
}

.movie-description p {
  font-size: 1.1em;
  line-height: 1.8;
  color: #666;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1em;
  text-decoration: none;
  display: inline-block;
  transition: all 0.3s;
  font-weight: 500;
}

.btn-warning {
  background: #ff9800;
  color: white;
}

.btn-warning:hover {
  background: #f57c00;
}

.btn-danger {
  background: #f44336;
  color: white;
}

.btn-danger:hover {
  background: #d32f2f;
}

.loading,
.error {
  text-align: center;
  padding: 48px 20px;
  font-size: 1.2em;
  color: #666;
}

.error {
  color: #f44336;
}

@media (max-width: 768px) {
  .movie-header {
    flex-direction: column;
    align-items: center;
  }

  .movie-poster-large {
    width: 100%;
    max-width: 300px;
  }

  .movie-info-main h1 {
    font-size: 1.8em;
  }
}
</style>

