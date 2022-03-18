<template>
  <div class="card">
    <div class="row">
      <div class="col-md-2">
        <img
          :src="movie.Poster"
          class="img-fluid rounded-start"
          :alt="movie.Title"
        />
      </div>
      <div class="col-md-10">
        <div class="card-body">
          <h5 class="card-title card-text">
            <a class="card-text" :href="href">{{ movie.Title }}</a>
            <span>({{ movie.Year }})</span>
          </h5>
          <p class="card-text">
            {{ movie.Runtime ? movie.Runtime : "N/A" }}
            <span v-for="genre in movie.Genre.split(',')"> | {{ genre }}</span>
          </p>
          <p class="card-text" style="color:khaki">
            Director: {{ movie.Director ? movie.Director : "N/A" }}
          </p>

          <p class="card-text" style="color:aqua">
            Actors: {{ movie.Actors ? movie.Actors : "N/A" }}
            <span v-for="actor in movie.Actors.split(',')"> | {{ actor }}</span>
          </p>
          <p class="card-text">
            {{ movie.Plot == "N/A" ? "No Plot" : movie.Plot }}
          </p>
        </div>
      </div>
    </div>
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
img {
  padding: 2ch;
  width: 100%;
  height: 8vm;
  object-fit: cover;
}
.card {
  background-color: rgba(150, 165, 179, 0.8);
}

.card-text {
  text-align: left;
  text-decoration: none !important;
}
p{
    width:100%;
}
.card-img-top {
  width: 80%;
  height: 20vw;
  object-fit: cover;
}
</style>