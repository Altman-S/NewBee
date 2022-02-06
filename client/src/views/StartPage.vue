<template>
  <div class="start-page">
    <div class="">Logo</div>
    <div class="position-absolute top-50 start-50 translate-middle">
      <search-bar></search-bar>
    </div>
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
.position-relative-example div {
  width: 2em;
  height: 2em;
  background-color: #343a40;
  border-radius: 0.25rem;
}
</style>