<template>
  <movie-card-container :movies="movies"></movie-card-container>
  <!-- <MovieCard :title="title" :imgurl="imgurl"></MovieCard> -->
</template>

<script>
import MovieCardContainer from "./components/MovieCardContainer.vue";
import MovieCard from "./components/MovieCard.vue";

export default {
  name: "App",
  components: {
    MovieCardContainer,
    MovieCard,
  },
  created: function () {
    fetch("/api/movies/")
      .then((response) => response.json())
      .then((data) => {
        const movies = data.movies;
        console.log(movies.length);
        this.movies = movies;
      });
  },
  data: function () {
    return {
      movies: null,
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
