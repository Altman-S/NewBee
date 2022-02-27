<template>
<!--  <div class="start-page">-->
<!--    <div class="background"><img src="../../public/logos/background.jpg" alt=""></div>-->
<!--    <div class="logo"><img src="../../public/logos/logo.png" alt=""></div>-->
<!--    &lt;!&ndash; <div class="position-absolute top-50 start-50 translate-middle"> &ndash;&gt;-->
<!--      <search-bar></search-bar>-->
<!--    &lt;!&ndash; </div> &ndash;&gt;-->
<!--  </div>-->
  <div>
    <div class="background">
      <img src="../../public/logos/background.jpg" width="100%" height="100%" alt="" />
    </div>
    <div class="logo">
      <img src="../../public/logos/logo.png" width="100%" height="100%" alt="">
    </div>
    <div class="abc">
      <div style="">
<!--        <search-bar></search-bar>-->
      </div>
    </div>
    <search-bar></search-bar>


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

.background{
  width: 100%;
  height: 100%;
  z-index: -1;
  position: fixed;
}

.logo{
  margin: 0 auto;
  left:35%;
  top: 23%;
  height: 26%;
  width: 28%;
  position: fixed;
}

.abc{
  left: 28%;
  top: 30%;
  height: 20%;
  width: 50%;
  z-index: 1;
  position: fixed;
}

/* .position-relative-example div {
  width: 2em;
  height: 2em;
  background-color: #343a40;
  border-radius: 0.25rem;
} */
</style>