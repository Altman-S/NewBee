<template>
  <div>
    <div class="content1">
      <h1>Sorry, no result for it.</h1>
    </div>
    <div class="content2">
      <h1>We are working hard to enlarge our database.</h1>
      <h1>Please try another keywords in the searching box.</h1>
      <h1>Thanks for your patience.</h1>
    </div>
  </div>
</template>


<script>
export default {
  name: "ErrorPage",
};
</script>


<style scoped>
/* .background {
  width: 100%;
  height: 100%;
  z-index: -1;
  position: fixed;
  background: rgba(255, 255, 255, .);
} */
.content1 {
  text-align: center; /*让div内部文字居中*/
  color: red;
  width: 500px;
  margin: auto;
  position: relative;
  top: 140px;
  left: 0;
  right: 0;
  bottom: 0;
}
.content2 {
  text-align: center; /*让div内部文字居中*/
  color: white;
  width: 1000px;
  margin: auto;
  position: relative;
  top: 160px;
  left: 0;
  right: 0;
  bottom: 0;
}
</style>