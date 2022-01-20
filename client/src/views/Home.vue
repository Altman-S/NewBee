<template>
  <div class="home">
    This is home page
    <movie-card-container :movies="movies"></movie-card-container>
  </div>
</template>

<script>
import MovieCardContainer from "../components/MovieCardContainer.vue";
import MovieCard from "../components/MovieCard.vue";

export default {
  name: "Home",
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
