<template>
  <div id="home">
    <div class="background">
      <img
        class="unselectable"
        src="../../public/logos/background.jpg"
        width="2000"
        height="1000"
        alt=""
      />
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

<style>
</style>
