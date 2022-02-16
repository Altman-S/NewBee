<template>
  <div class="start-page">
    <div class="logo"><img src="../../public/logos/MIO.png" alt=""></div>
    <!-- <div class="position-absolute top-50 start-50 translate-middle"> -->
      <search-bar></search-bar>
    <!-- </div> -->
  </div>
</template>

<script>
import SearchBar from "../components/SearchBar.vue";

export default {
  name: "Start Page",
  components: {
    SearchBar,
  },
};
</script>

<style>
.block {
  width: 10em;
  height: 2em;
  background-color: #343a40;
  border-radius: 0.25rem;
}
.start-page{
  background-color: #1e3799 !important;
}
/* .position-relative-example div {
  width: 2em;
  height: 2em;
  background-color: #343a40;
  border-radius: 0.25rem;
} */
</style>