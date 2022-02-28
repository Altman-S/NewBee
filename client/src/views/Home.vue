<template>
  <div id="home">
<<<<<<< HEAD
    <div class="background">
      <img
        class="unselectable"
        src="../../public/logos/background.jpg"
        width="2000"
        height="1000"
        alt=""
      />
=======
    <div class="bg">
      <img src="../../public/logos/background.jpg" width="100%" height="100%" alt="" />
>>>>>>> 7ac582f659507b6eb019d470416b2f99c25484f1
    </div>
    <div class="header">
      <img
        src="../../public/logos/logo.png"
        width="100px"
        height="100px"
        alt=""
      />
      <search-bar></search-bar>
    </div>
    <div class="container">
      <router-view v-slot="{ Component, route }">
        <keep-alive>
          <component
            :is="Component"
            :key="route.name"
            v-if="route.meta.keepAlive"
          />
        </keep-alive>
        <component
          :is="Component"
          :key="route.name"
          v-if="!route.meta.keepAlive"
        />
      </router-view>
    </div>
  </div>
</template>

<script>
import SearchBar from "../components/SearchBar.vue";

export default {
  name: "Home",
  components: {
    SearchBar,
  },
};
</script>

<<<<<<< HEAD
<style>
=======
<style scoped>
/*#home {*/
/*  background-color: blue;*/
/*}*/

.container {
  padding-bottom: 20px;
  background-color: white;
}

.bg {
  width: 100%;
  height: 100%;
  z-index: -1;
  position: fixed;
}
>>>>>>> 7ac582f659507b6eb019d470416b2f99c25484f1
</style>
