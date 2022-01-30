<template>
  <div>
    <h1>Info page for movie {{ id }}</h1>
  </div>
</template>

<script>
export default {
  name:'MovieInfoPage',
  props: {
    id: String,
  },
  mounted: function () {
    console.log("Mounted")
  },
};
</script>