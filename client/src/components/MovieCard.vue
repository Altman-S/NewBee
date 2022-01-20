<template>
  <div class="movieCard">
    <a :href="href">
      <img :src="movie.Poster" :alt="movie.title" />
      {{movie.Title}}
    </a>
    <!-- <router-link :to="'/movie/'+movie.imdbID" tag="div">{{ movie.Title }}</router-link> -->
    <!-- <router-link :to="'/movie/' + movie.imdbID" custom>
      <button>
        {{ movie.Title }}
      </button>
    </router-link> -->
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    href: String,
    movie: Object,
  },
};
</script>

<style scoped>
.movieCard {
  background-color: aqua;
}
</style>