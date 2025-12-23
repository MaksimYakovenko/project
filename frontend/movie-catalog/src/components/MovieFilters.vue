<template>
  <div class="filters">
    <div class="search-box">
      <input
        type="text"
        v-model="searchQuery"
        @input="onSearchChange"
        placeholder="🔍 Пошук за назвою..."
        class="search-input"
      />
    </div>

    <div class="filter-group">
      <select v-model="selectedGenre" @change="onFilterChange" class="filter-select">
        <option :value="null">Всі жанри</option>
        <option v-for="genre in genres" :key="genre.id" :value="genre.id">
          {{ genre.name }}
        </option>
      </select>

      <select v-model="selectedDirector" @change="onFilterChange" class="filter-select">
        <option :value="null">Всі режисери</option>
        <option v-for="director in directors" :key="director.id" :value="director.id">
          {{ director.name }}
        </option>
      </select>

      <input
        type="number"
        v-model.number="selectedYear"
        @input="onFilterChange"
        placeholder="Рік"
        class="filter-input"
        min="1900"
        max="2100"
      />

      <button @click="clearFilters" class="btn-clear">Очистити фільтри</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useMoviesStore } from '@/stores/moviesStore.js';

const moviesStore = useMoviesStore();

const searchQuery = ref('');
const selectedGenre = ref(null);
const selectedDirector = ref(null);
const selectedYear = ref(null);

const emit = defineEmits(['filter-change']);

const genres = ref([]);
const directors = ref([]);

onMounted(async () => {
  await moviesStore.fetchGenres();
  await moviesStore.fetchDirectors();
  genres.value = moviesStore.genres;
  directors.value = moviesStore.directors;
});

function onSearchChange() {
  moviesStore.setFilter('search', searchQuery.value);
  emit('filter-change');
}

function onFilterChange() {
  moviesStore.setFilter('genre', selectedGenre.value);
  moviesStore.setFilter('director', selectedDirector.value);
  moviesStore.setFilter('year', selectedYear.value);
  emit('filter-change');
}

function clearFilters() {
  searchQuery.value = '';
  selectedGenre.value = null;
  selectedDirector.value = null;
  selectedYear.value = null;
  moviesStore.clearFilters();
  emit('filter-change');
}
</script>

<style scoped>
.filters {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 24px;
}

.search-box {
  margin-bottom: 16px;
}

.search-input {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1em;
  transition: border-color 0.3s;
}

.search-input:focus {
  outline: none;
  border-color: #667eea;
}

.filter-group {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.filter-select,
.filter-input {
  padding: 10px 12px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 0.95em;
  background: white;
  cursor: pointer;
  transition: border-color 0.3s;
}

.filter-select:focus,
.filter-input:focus {
  outline: none;
  border-color: #667eea;
}

.filter-select {
  flex: 1;
  min-width: 150px;
}

.filter-input {
  width: 120px;
}

.btn-clear {
  padding: 10px 20px;
  background: #f44336;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.95em;
  transition: background 0.3s;
}

.btn-clear:hover {
  background: #d32f2f;
}
</style>

