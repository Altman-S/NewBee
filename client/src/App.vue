<template>
  <router-view></router-view>
</template>

<script>
import StartPage from "./views/StartPage.vue";

export default {
  name: "App",
  components: {
    StartPage,
  },
  data: function () {
    return {};
  },
};
</script>

