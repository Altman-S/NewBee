<template>
  <div class="home">
    <div class="header">
      <div class="logo">
        <router-link :to="'/'" custom v-slot="{ href }">
          <a :href="href"
            ><img
              src="../../public/logos/logo.png"
              width="150"
              height="112"
              alt=""
          /></a>
        </router-link>
      </div>
      <search-bar></search-bar>
    </div>
    <div
      :class="{
        resultpage:
          this.$route.path == '/search' || this.$route.path == '/searchAll',
        infopage:
          this.$route.path != '/search' && this.$route.path != '/searchAll',
      }"
    >
      <h3
        class="result"
        v-if="this.$route.path == '/search' || this.$route.path == '/searchAll'"
      >
        Results for '{{ Object.values(this.$route.query)[0] }}'
      </h3>
      <div
        :class="{
          container:
            this.$route.path == '/search' || this.$route.path == '/searchAll',
        }"
      >
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

<style scoped>
.header {
  background-color: aqua;
}
.resultpage {
  top: 100px;
  position: relative;
}
.logo {
  margin: 0 auto;
  left: 30px;
  top: 3px;
  position: absolute;
}
.result {
  color: aliceblue;
  left: 15%;
  position: absolute;
}
.container {
  left: 13%;
  top: 50px;
  position: absolute;
  margin: 0%;
}
</style>
