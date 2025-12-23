<template>
  <div class="movie-form-page">
    <div class="container">
      <button @click="goBack" class="btn-back">← Назад</button>

      <div class="form-container">
        <h1>{{ isEdit ? 'Редагувати фільм' : 'Додати новий фільм' }}</h1>

        <form @submit.prevent="handleSubmit" class="movie-form">
          <div class="form-group">
            <label for="title">Назва фільму *</label>
            <input
              id="title"
              type="text"
              v-model="form.title"
              required
              placeholder="Введіть назву фільму"
              class="form-input"
            />
          </div>

          <div class="form-group">
            <label for="description">Опис *</label>
            <textarea
              id="description"
              v-model="form.description"
              required
              placeholder="Введіть опис фільму"
              class="form-textarea"
              rows="6"
            ></textarea>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="year">Рік виходу *</label>
              <input
                id="year"
                type="number"
                v-model.number="form.year"
                required
                min="1900"
                max="2100"
                placeholder="2024"
                class="form-input"
              />
            </div>

            <div class="form-group">
              <label for="genre">Жанр *</label>
              <select
                id="genre"
                v-model.number="form.genre"
                required
                class="form-select"
              >
                <option value="">Оберіть жанр</option>
                <option v-for="genre in genres" :key="genre.id" :value="genre.id">
                  {{ genre.name }}
                </option>
              </select>
            </div>

            <div class="form-group">
              <label for="director">Режисер *</label>
              <select
                id="director"
                v-model.number="form.director"
                required
                class="form-select"
              >
                <option value="">Оберіть режисера</option>
                <option v-for="director in directors" :key="director.id" :value="director.id">
                  {{ director.name }}
                </option>
              </select>
            </div>
          </div>

          <div v-if="error" class="error-message">
            {{ error }}
          </div>

          <div class="form-actions">
            <button type="submit" class="btn btn-success" :disabled="loading">
              {{ loading ? '⏳ Збереження...' : (isEdit ? '💾 Зберегти зміни' : '➕ Додати фільм') }}
            </button>
            <button type="button" @click="goBack" class="btn btn-secondary">
              Скасувати
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useMoviesStore } from '@/stores/moviesStore.js';

const route = useRoute();
const router = useRouter();
const moviesStore = useMoviesStore();

const isEdit = computed(() => !!route.params.id);

const form = ref({
  title: '',
  description: '',
  year: new Date().getFullYear(),
  genre: '',
  director: ''
});

const genres = ref([]);
const directors = ref([]);
const loading = ref(false);
const error = ref(null);

onMounted(async () => {
  await moviesStore.fetchGenres();
  await moviesStore.fetchDirectors();
  genres.value = moviesStore.genres;
  directors.value = moviesStore.directors;

  if (isEdit.value) {
    await moviesStore.fetchMovie(route.params.id);
    const movie = moviesStore.currentMovie;
    if (movie) {
      form.value = {
        title: movie.title,
        description: movie.description,
        year: movie.year,
        genre: movie.genre,
        director: movie.director
      };
    }
  }
});

async function handleSubmit() {
  loading.value = true;
  error.value = null;

  try {
    if (isEdit.value) {
      await moviesStore.updateMovie(route.params.id, form.value);
    } else {
      await moviesStore.createMovie(form.value);
    }
    router.push({ name: 'Home' });
  } catch (e) {
    error.value = isEdit.value
      ? 'Помилка при оновленні фільму. Перевірте дані та спробуйте ще раз.'
      : 'Помилка при створенні фільму. Перевірте дані та спробуйте ще раз.';
    console.error('Error saving movie:', e);
  } finally {
    loading.value = false;
  }
}

function goBack() {
  router.back();
}
</script>

<style scoped>
.movie-form-page {
  min-height: 100vh;
  background: #f5f5f5;
  padding: 24px 0;
}

.container {
  max-width: 800px;
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

.form-container {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 32px;
}

.form-container h1 {
  margin: 0 0 32px 0;
  color: #333;
}

.movie-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 500;
  color: #333;
  font-size: 1em;
}

.form-input,
.form-textarea,
.form-select {
  padding: 12px 16px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1em;
  font-family: inherit;
  transition: border-color 0.3s;
}

.form-input:focus,
.form-textarea:focus,
.form-select:focus {
  outline: none;
  border-color: #667eea;
}

.form-textarea {
  resize: vertical;
}

.form-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}

.error-message {
  padding: 12px 16px;
  background: #ffebee;
  border: 1px solid #f44336;
  border-radius: 8px;
  color: #c62828;
}

.form-actions {
  display: flex;
  gap: 12px;
  margin-top: 16px;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1em;
  font-weight: 500;
  transition: all 0.3s;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-success {
  background: #4caf50;
  color: white;
  flex: 1;
}

.btn-success:hover:not(:disabled) {
  background: #45a049;
}

.btn-secondary {
  background: #9e9e9e;
  color: white;
}

.btn-secondary:hover {
  background: #757575;
}

@media (max-width: 768px) {
  .form-container {
    padding: 24px 16px;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .form-actions {
    flex-direction: column;
  }
}
</style>

