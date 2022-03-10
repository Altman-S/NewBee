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
        <ul class="list-group">
          <li class="list-group-item" v-for="data in myData">
            {{ data.category }} | {{ data.title }}
          </li>
        </ul>
        <div class="input-group-append">
          <button class="btn btn-primary" @click="search">
            <i class="fas fa-search"></i>
          </button>
        </div>
      </div>
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
        if (this.searchFilter == "All") {
          this.$router.push({
            path: "/searchAll",
            query: { [this.searchFilter]: this.searchText },
          });
        }else{
            this.$router.push({
            path: "/search",
            query: { [this.searchFilter]: this.searchText },
          });
        }
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
      this.myData = [];
      // 限制频繁请求
      //   this.throttle(this.getData, window);
    },
    getData() {
      fetch(`http://127.0.0.1:5000/api/movies/prompt?${this.searchText}`)
        .then((response) => response.json())
        .then((data) => {
          for (const [key, value] of Object.entries(data.prompt)) {
            console.log(key);
            this.myData.push({
              category: key,
              title: value[0].Title,
              year: value[0].Year,
              actors: value[0].Actors,
            });
          }
        });
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
  left: 20%;
  top: 3%;
  width: 50%;
  /* need fix this bug */
  position: absolute;
}
.list-group {
  background-color: white;
  /* display: none; */
  list-style-type: none;
  top: 100%;
  margin: 0 0 0 10px;
  padding: 0;
  position: absolute;
  width: 100%;
}

.list-group > li {
  border-color: gray;
  border-image: none;
  border-style: solid solid none;
  border-width: 1px 1px 0;
  padding-left: 5px;
}

.list-group > li:last-child {
  border-bottom: 1px solid gray;
}

/*.form-control:focus + .list-group {
  display: block;
} */
</style>