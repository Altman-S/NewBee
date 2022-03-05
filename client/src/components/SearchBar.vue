<template>
  <div
    :class="{
      startPage: this.$parent.$options.name == 'Start Page',
      homePage: this.$parent.$options.name == 'Home',
    }"
  >
    <div class="container d-flex justify-content-center">
      <div class="input-group mb-3">
        <div class="dropdown">
          <button
            class="btn btn-secondary dropdown-toggle"
            type="button"
            id="dropdownMenuButton1"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            {{ searchFilter }}
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
            <li v-for="filter in filter_list">
              <button class="dropdown-item" @click="changeFilter(filter)">
                {{ filter }}
              </button>
            </li>
          </ul>
        </div>
        <input
          type="text"
          class="form-control"
          id="searchBar"
          placeholder="search"
          v-model="searchText"
          @keydown.enter="search"
          @keyup="get($event)"
        />
        <div class="input-group-append">
          <button class="btn btn-primary" @click="search">
            <i class="fas fa-search"></i>
          </button>
        </div>
      </div>
      <ul>
        <li v-for="(item, index) in myData" :class="{ gray: index === now }">
          {{ item }}
        </li>
      </ul>
    </div>
  </div>
</template>


<script>
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";
import { validate_year } from "./Validators.js";

export default {
  name: "Search Bar",
  data: function () {
    return {
      v$: useValidate(),
      searchText: "",
      searchFilter: "All",
      filter_list: ["All", "Title", "Year", "Genre", "Celebrity"],
      myData: [],
      tt: "",
      now: -1,
    };
  },
  methods: {
    async search() {
      const searchURL =
        "/home/search?" + this.searchFilter + "=" + this.searchText;
      const result = await this.v$.$validate();
      if (result == false) {
        alert("Wrong input");
      } else {
        this.$router.push({
          path: "/home/search",
          query: { [this.searchFilter]: this.searchText },
        });
      }
    },
    changeFilter(filter) {
      this.searchFilter = filter;
      this.searchText = "";
    },
    get(e) {
      // 请求限制 按了上下箭头
      if (e.keyCode === 38 || e.keyCode === 40) {
        return;
      }
      // 限制频繁请求
      this.throttle(this.getData, window);
    },
    getData() {
      console.log("get data");
      this.myData = ["a", "b", "c"];
    },
    throttle(method, context) {
      clearTimeout(method.tId);
      method.tId = setTimeout(function () {
        method.call(context);
      }, 300);
    },
  },
  validations: function () {
    switch (this.searchFilter) {
      case "All":
        return { searchText: { required } };
        break;
      case "Title":
        return { searchText: { required } };
        break;
      case "Genre":
        return { searchText: { required } };
        break;
      case "Celebrity":
        return { searchText: { required } };
        break;
      case "Year":
        return { searchText: { required, validate_year } };
        break;
    }
  },
};
</script>

<style scoped>
.startPage {
  left: 28%;
  top: 50%;
  height: 20%;
  width: 44%;
  z-index: 0;
  position: fixed;
}
.homePage {
  left: 28%;
  top: 5%;
  width: 40%;
  /* need fix this bug */
  /* position: absolute; */ 
}
</style>