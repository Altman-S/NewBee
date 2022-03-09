<template>
  <div class="container overflow-hidden">
    <div class="row gy-5">
      <div class="col-10">
        <div class="bg-grey">
          <h4 class="abc">Title</h4>
          <div class="rightright">
            <h4 class="def">More</h4>
          </div>
          <movie-card-container :movies="title_movies"></movie-card-container>
        </div>
      </div>
      <div class="col-10">
        <div class="bg-grey">
          <h4 class="abc">Celebrity</h4>
          <div class="rightright">
            <h4 class="def">More</h4>
          </div>
          <movie-card-container :movies="celes_movies"></movie-card-container>
        </div>
      </div>
      <div class="col-10">
        <div class="bg-grey">
          <h4 class="abc">Genre</h4>
          <div class="rightright">
            <h4 class="def">More</h4>
          </div>
          <movie-card-container :movies="genre_movies"></movie-card-container>
        </div>
      </div>
      <div class="col-10">
<!--        <div class="p-3 border bg-grey">-->
        <div class="bg-grey">
          <h4 class="abc">Year</h4>
          <div class="rightright">
            <h4 class="def">More</h4>
          </div>
          <movie-card-container :movies="year_movies"></movie-card-container>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardContainer from "../components/MovieCardContainer.vue";
import MovieCard from "../components/MovieCard.vue";

export default {
  name: "MovieAllPage",
  components: {
    MovieCardContainer,
    MovieCard,
  },
  created: function () {
    console.log("MovieAllPage created");
    this.$watch(
        () => this.$route.query,
        (newQuery, oldQuery) => {
          this.search_params = {};
          const query = this.$route.query;
          if (Object.keys(query).length != 0) {
            for (let key in query) {
              this.search_params[key] = query[key];
            }
            this.search();
          }
        },
        { immediate: true }
    );

    // To be deleted
    this.search();
  },
  data: function () {
    return {
      api: "api/movies/search",
      title_movies: null,
      celes_movies: null,
      genre_movies: null,
      year_movies: null,
      search_params: {},

    };
  },
  methods: {
    search() {
      console.log("Search");
      // const searchURL = new URLSearchParams(this.search_params);
      const searchURL = "Title=galaxy"
      //   console.log(`${this.api}?${searchURL}`);
      // fetch(`${this.api}?${searchURL}`)
      window.scrollTo(0, 0);

      // get title_movies
      fetch(`http://127.0.0.1:5000/api/movies/search?Title=galaxy`)
          .then((response) => response.json())
          .then((data) => {
            if (data.response == "success") {
              this.title_movies = data.movies.slice(0, 3);

            }
          });

      // get celes_movies
      fetch(`http://127.0.0.1:5000/api/movies/search?Celebrity=galaxy`)
          .then((response) => response.json())
          .then((data) => {
            if (data.response == "success") {
              this.celes_movies = data.movies.slice(0, 3);

            }
          });

      // get celes_movies
      fetch(`http://127.0.0.1:5000/api/movies/search?Genre=galaxy`)
          .then((response) => response.json())
          .then((data) => {
            if (data.response == "success") {
              this.genre_movies = data.movies.slice(0, 3);

            }
          });

      // get year_movies
      fetch(`http://127.0.0.1:5000/api/movies/search?Year=galaxy`)
          .then((response) => response.json())
          .then((data) => {
            if (data.response == "success") {
              this.year_movies = data.movies.slice(0, 3);

            }
          });

    },
  }
}
</script>

<style scoped>
.abc {
  color: gold;
}

.def {
  color: white;
}

.leftleft {
  float: left;
  display: inline;
}

.rightright {
  float: right;
  display: inline;
}
</style>