<template>
  <div class="container">
    <div class="canvas" v-show="loading">
      <div class="spinner"></div>
    </div>
    <h1 class="title">{{ movie.Title }} ({{ movie.Year }})</h1>
    <div class="box">
      <div class="left">
        <img
            :src="movie.Poster"
            class="img-fluid rounded-start"
            :alt="movie.Title"
        />
      </div>

      <div class="info">
        <div class="director">Director: {{ movie.Director }}</div>
        <div class="actors">Actors: {{ movie.Actors }}</div>
        <div class="gerne">Gerne: {{ movie.Genre }}</div>

        <div class="rating">Rating: {{ movie.imdbRating }}</div>
        <div class="votes">Votes: {{ movie.imdbVotes }}</div>

        <div class="runtime">Runtime: {{ movie.Runtime }}</div>
        <div class="imdbid">imdbID: {{ movie.imdbID }}</div>

        <div>
          <h3 class="plot-title">Plot of {{ movie.Title }}</h3>
          <h4>{{ movie.Plot }}</h4>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name:'MovieInfoPage',
  props: {
    id: String,
  },

  data: function() {
    return {
      api: "api/movies/id/",
      movie: Object,
    };
  },

  created: function () {
    console.log("MovieInfoPage created");
    const movie_id = this.id;
    // fetch(`${this.api}${movie_id}`)
    fetch(`http://127.0.0.1:5000/api/movies/id/${movie_id}`)
      .then((response) => response.json())
      .then((data) => {
      console.log(data.response);
      this.movie = data.movie;
    })
  },

  mounted: function () {
    console.log("Mounted")
  },
};
</script>


<style>
.director {
  font-size: 25px;
  color: aqua;
}

.actors {
  font-size: 25px;
  color: aqua;
}

.gerne {
  font-size: 25px;
  color: aqua;
}

.rating {
  font-size: 25px;
  color: khaki;
}

.votes {
  font-size: 25px;
  color: khaki;
}

.imdbid {
  font-size: 25px;
  color: pink;
}

.runtime {
  font-size: 25px;
  color: pink;
}

.title {
  margin-top: 100px;
  color: greenyellow;
}

.box {
  display: flex;
  flex-flow: row;
  justify-content: space-between;
}

.left {
  width: 300px;
  height: 300px;
}

.left img {
  width: 150%;
  height: 150%;
}

.info {
  margin-left: 36px;
  flex: 1;
  color: white;
}

.plot-title {
  margin-top: 30px;
  color: gold;
}

</style>