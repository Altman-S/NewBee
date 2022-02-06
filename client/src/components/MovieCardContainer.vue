<template>
  <div class="row row-cols-1 row-cols-md-4 g-4">
    <div class="col" v-for="movie in movies" :key="movie.imdbID">
      <router-link :to="'/movie/' + movie.imdbID" custom v-slot="{ href }">
        <movie-card :movie="movie" :href="href"></movie-card>
      </router-link>
    </div>
  </div>
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
    return {};
  },
};
</script>