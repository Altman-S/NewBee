<template>
  <div id="home">
    <router-link :to="'/'" custom v-slot="{ href }">
      <div class="logo">
        <a :href="href"
          ><img
            src="../../public/logos/logo.png"
            width="90"
            height="55"
            alt=""
            hre
        /></a>
      </div>
    </router-link>

    <div class="background">
      <img
        class="unselectable"
        src="../../public/logos/background.jpg"
        width="2000"
        height="1000"
        alt=""
      />
    </div>

    <!-- <div class="header"> -->
      <search-bar></search-bar>
    <!-- </div> -->

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

<style>
.logo {
  margin: 0 auto;
  left: 6%;
  top: 1.6%;
  position: fixed;
}
</style>
