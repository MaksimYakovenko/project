<template>
  <div class="movie-card" @click="goToMovie">
    <div class="movie-poster">
      <div class="movie-year">{{ movie.year }}</div>
    </div>
    <div class="movie-info">
      <h3 class="movie-title">{{ movie.title }}</h3>
      <p class="movie-meta">
        <span class="genre">{{ movie.genre_name }}</span>
        <span class="director">{{ movie.director_name }}</span>
      </p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
});

const router = useRouter();

function goToMovie() {
  router.push({ name: 'MovieDetail', params: { id: props.movie.id } });
}
</script>

<style scoped>
.movie-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  overflow: hidden;
}

.movie-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.movie-poster {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  height: 200px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.movie-year {
  background: rgba(255, 255, 255, 0.9);
  padding: 8px 16px;
  border-radius: 20px;
  font-weight: bold;
  font-size: 1.2em;
  color: #667eea;
}

.movie-info {
  padding: 16px;
}

.movie-title {
  margin: 0 0 8px 0;
  font-size: 1.2em;
  color: #333;
}

.movie-meta {
  display: flex;
  gap: 12px;
  margin: 0;
  font-size: 0.9em;
  color: #666;
}

.genre {
  background: #e3f2fd;
  padding: 4px 8px;
  border-radius: 4px;
  color: #1976d2;
}

.director {
  color: #666;
}
</style>

