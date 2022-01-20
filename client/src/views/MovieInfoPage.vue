<template>
  <div>
    <h1>Info page for movie {{ id }}</h1>
  </div>
</template>

<script>
export default {
  props: {
    id: String,
  },
  mounted: function () {
    console.log("Mounted")
  },
};
</script>