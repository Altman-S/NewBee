<template>
  <ul>
    <li v-for="movie in movies" :key="movie.imdbID">
      <router-link :to="'/movie/' + movie.imdbID" custom v-slot="{href}">
        <movie-card :movie="movie" :href="href"></movie-card>
      </router-link>
    </li>
  </ul>
</template>

<script>
import MovieCard from "./MovieCard.vue";

export default {
  name: "MovieCardContainer",
  props: {
    movies: Array,
  },
  components: {
    MovieCard,
  },
  data: function () {
    return {
      back_end_url: "http://127.0.0.1:5000/api/movies/",
    };
  },
};
</script>