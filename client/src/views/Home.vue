<template>
  <div class="container">
    <movie-card-container :movies="movies"></movie-card-container>
  </div>
  <pagination
    :total_page="total_page"
    :page_number="current_page"
    @changePage="change_page($event)"
  ></pagination>
</template>

<script>
import MovieCardContainer from "../components/MovieCardContainer.vue";
import MovieCard from "../components/MovieCard.vue";
import Pagination from "../components/Pagination.vue";

export default {
  name: "Home",
  components: {
    MovieCardContainer,
    MovieCard,
    Pagination,
  },
  created: function () {
    fetch("/api/movies/")
      .then((response) => response.json())
      .then((data) => {
        const movies = data.movies;
        console.log(movies.length);
        this.movies = movies;
        this.total_number = data.total_number;
        this.current_page = data.current_page;
      });
  },
  data: function () {
    return {
      movies: null,
      total_number: null,
      current_page: null,
      movies_per_page: 20,
    };
  },
  methods: {
    change_page(page) {
      window.scrollTo(0, 0);
      console.log(page);
      const url = "api/movies/?page=" + page;
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          const movies = data.movies;
          console.log(movies.length);
          this.movies = movies;
          this.total_number = data.total_number;
          this.current_page = data.current_page;
        });
    },
  },
  computed: {
    total_page() {
      return Math.ceil(this.total_number / this.movies_per_page);
    },
  },
};
</script>

<style scoped>
.container {
  padding-bottom: 20px;
}
</style>
