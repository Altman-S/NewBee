<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: "App",
  components: {},
  data: function () {
    return {};
  },
};
</script>

<style>
html {
  background-image: url("../public/logos/background.jpg");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
#app {
  position: absolute;
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
}
</style>

