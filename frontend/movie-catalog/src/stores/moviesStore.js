import { defineStore } from 'pinia';
import apiPrivate from '@/utils/apiPrivate.js';
import apiPublic from '@/utils/apiPublic.js';

export const useMoviesStore = defineStore('movies', {
    state: () => ({
        movies: [],
        currentMovie: null,
        genres: [],
        directors: [],
        loading: false,
        error: null,
        filters: {
            search: '',
            genre: null,
            director: null,
            year: null,
        }
    }),

    actions: {
        async fetchMovies() {
            this.loading = true;
            this.error = null;
            try {
                const params = {};
                if (this.filters.search) params.search = this.filters.search;
                if (this.filters.genre) params.genre = this.filters.genre;
                if (this.filters.director) params.director = this.filters.director;
                if (this.filters.year) params.year = this.filters.year;

                const { data } = await apiPublic.get('/movies/', { params });
                this.movies = data;
            } catch (error) {
                this.error = 'Помилка завантаження фільмів';
                console.error('Error fetching movies:', error);
            } finally {
                this.loading = false;
            }
        },

        async fetchMovie(id) {
            this.loading = true;
            this.error = null;
            try {
                const { data } = await apiPublic.get(`/movies/${id}/`);
                this.currentMovie = data;
            } catch (error) {
                this.error = 'Помилка завантаження фільму';
                console.error('Error fetching movie:', error);
            } finally {
                this.loading = false;
            }
        },

        async createMovie(movieData) {
            try {
                const { data } = await apiPrivate.post('/movies/', movieData);
                this.movies.unshift(data);
                return data;
            } catch (error) {
                this.error = 'Помилка створення фільму';
                throw error;
            }
        },

        async updateMovie(id, movieData) {
            try {
                const { data } = await apiPrivate.put(`/movies/${id}/`, movieData);
                const index = this.movies.findIndex(m => m.id === id);
                if (index !== -1) {
                    this.movies[index] = data;
                }
                this.currentMovie = data;
                return data;
            } catch (error) {
                this.error = 'Помилка оновлення фільму';
                throw error;
            }
        },

        async deleteMovie(id) {
            try {
                await apiPrivate.delete(`/movies/${id}/`);
                this.movies = this.movies.filter(m => m.id !== id);
            } catch (error) {
                this.error = 'Помилка видалення фільму';
                throw error;
            }
        },

        async fetchGenres() {
            try {
                const { data } = await apiPublic.get('/genres/');
                this.genres = data;
            } catch (error) {
                console.error('Error fetching genres:', error);
            }
        },

        async fetchDirectors() {
            try {
                const { data } = await apiPublic.get('/directors/');
                this.directors = data;
            } catch (error) {
                console.error('Error fetching directors:', error);
            }
        },

        setFilter(key, value) {
            this.filters[key] = value;
        },

        clearFilters() {
            this.filters = {
                search: '',
                genre: null,
                director: null,
                year: null,
            };
        }
    }
});

