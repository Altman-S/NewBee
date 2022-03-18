<template>
  <div class="list-group">
    <div v-for="movie in movies">
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