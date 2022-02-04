<template>
  <a :href="href" class="card-text">
    <div class="card h-100 w-100">
      <img :src="movie.Poster" class="card-img-top" :alt="movie.Title" />
      <div class="card-body">
        <h5 class="card-title">{{ movie.Title }}</h5>
        <p class="card-text">
          {{ movie.Year }}
        </p>
      </div>
    </div>
  </a>
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
/* img {
  vertical-align: middle;
  border-style: none;
  width: 100%;
  height: 100%;
  object-fit: cover;
} */
.card-text {
  text-decoration: none;
}

.card-img-top {
  width: 100%;
  height: 20vw;
  object-fit: cover;
}
</style>