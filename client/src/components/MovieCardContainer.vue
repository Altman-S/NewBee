<template>
  <ul id="array-rendering">
    <li v-for="movie in movies" :key="movie.imdbID">
      <a :href="'/api/movies/id/'+movie._id">{{movie.Title}}</a>
    </li>
  </ul>
</template>

<script>
export default {
  name: "MovieCardContainer",
  props: {
    movies: Array,
  },
  data:function(){
    return {
      back_end_url:"http://127.0.0.1:5000/api/movies/"
    }
  }
};
</script>