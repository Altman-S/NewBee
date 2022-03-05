<template>
  <div>
    <div class="background">
      <img
        class="unselectable"
        src="../../public/logos/background.jpg"
        width="100%"
        height="100%"
        alt=""
      />
    </div>
    <div class="logo">
      <img
        src="../../public/logos/logo.png"
        width="100%"
        height="100%"
        alt=""
      />
    </div>
    <div class="abc">
      <!-- <search-bar></search-bar> -->
    </div>
    <search-bar></search-bar>
    <!-- <dropdown></dropdown> -->
  </div>
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

.background {
  width: 100%;
  height: 100%;
  z-index: -1;
  position: fixed;
}

.logo {
  margin: 0 auto;
  left: 35%;
  top: 23%;
  height: 26%;
  width: 28%;
  position: fixed;
}

.unselectable {
  user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-drag: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}
</style>