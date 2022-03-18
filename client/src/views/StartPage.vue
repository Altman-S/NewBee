<template>
  <img src="../../public/logos/logo.png" class="logo" />
  <search-bar></search-bar>
  <!-- <dropdown></dropdown> -->
</template>

<script>
import SearchBar from "../components/SearchBar.vue";
import Dropdown from "../components/Dropdown.vue";

export default {
  name: "Start Page",
  components: {
    SearchBar,
    Dropdown,
  },
};
</script>

<style scoped>
.block {
  width: 10em;
  height: 2em;
  background-color: #343a40;
  border-radius: 0.25rem;
}

.logo {
  margin: 0 auto;
  left: 39%;
  top: 27%;
  position: fixed;
  width: 300px;
  height: 225px;
  alt: "logo";
}

</style>