<template>
  <div id="home">
    <div class="header">
      <search-bar></search-bar>
    </div>
    <div class="container">
      <movie-card-container :movies="movies"></movie-card-container>
      <pagination
        :total_page="total_page"
        :current_page="current_page"
        @changePage="change_page($event)"
      ></pagination>
    </div>
  </div>
</template>

<script>
import MovieCardContainer from "../components/MovieCardContainer.vue";
import MovieCard from "../components/MovieCard.vue";
import Pagination from "../components/Pagination.vue";
import SearchBar from "../components/SearchBar.vue";

export default {
  name: "Home",
  components: {
    MovieCardContainer,
    MovieCard,
    Pagination,
    SearchBar,
  },
  created: function () {
    this.$watch(
      () => this.$route.query,
      (newQuery, oldQuery) => {
        console.log(newQuery, oldQuery);
        this.search_params = {};
        const query = this.$route.query;
        for (let key in query) {
          this.search_params[key] = query[key];
        }
        this.search();
      }
    );
    const query = this.$route.query;
    for (let key in query) {
      this.search_params[key] = query[key];
    }
    this.search();
  },
  data: function () {
    return {
      api: "api/movies/search",
      movies: null,
      total_number: null,
      current_page: null,
      search_params: {},
      movies_per_page: 20,
    };
  },
  methods: {
    change_page(page) {
      window.scrollTo(0, 0);
      this.search_params["page"] = page;
      const searchURL = new URLSearchParams(this.search_params);
      console.log(`${this.api}?${searchURL}`);
      fetch(`${this.api}?${searchURL}`)
        .then((response) => response.json())
        .then((data) => {
          const movies = data.movies;
          console.log(movies.length);
          this.movies = movies;
          this.current_page = data.current_page;
        });
    },
    search() {
      const searchURL = new URLSearchParams(this.search_params);
      console.log(`${this.api}?${searchURL}`);
      fetch(`${this.api}?${searchURL}`)
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
#home {
  background-color: blue;
}
.container {
  padding-bottom: 20px;
  background-color: white;
}
</style>
