<template>
  <div id="box">
    <input
      type="text"
      v-model="tt"
      name=""
      @keyup="get($event)"
      @keydown.down="changeDown()"
      @keydown.up="changeUp()"
    />
    <ul>
      <li v-for="(item, index) in myData" :class="{ gray: index === now }">
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script>
import { url } from '@vuelidate/validators';
// import jsonp from "../main.js"

export default {
  name: "searchBar with dropdown",
  data: function () {
    return {
      myData: [],
      tt: "",
      now: -1,
    };
  },
  methods: {
    get: function (e) {
      // 请求限制 按了上下箭头
      if (e.keyCode === 38 || e.keyCode === 40) {
        return;
      }
      // enter跳转
      if (e.keyCode === 13) {
        window.open("https://www.baidu.com/s?wd=" + this.tt);
        this.tt = "";
      }
      // 限制频繁请求
      this.throttle(this.getData, window);
    },
    changeDown: function () {
      this.now++;
      // 到了最后一个选项
      if (this.now === this.myData.length) {
        this.now = -1;
      }
      this.tt = this.myData[this.now];
    },
    changeUp: function () {
      this.now--;
      // 到了第一个选项
      if (this.now === -2) {
        this.now = this.myData.length - 1;
      }
      this.tt = this.myData[this.now];
    },
    // 把请求单独拿出来
    getData() {
    //   opt = { param: `wd=${this.tt}` };
    //   jsonp("https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su")
    //   this.$originJsonp("https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su", opt,
    //     (err, data) => {
    //       console.log(err);
    //       console.log(data);
    //     }
    //   );
    },
    // 节流函数
    throttle(method, context) {
      clearTimeout(method.tId);
      method.tId = setTimeout(function () {
        method.call(context);
      }, 300);
    },
  },
};
</script>

<style scoped>
.gray {
  background: gray;
}
</style>