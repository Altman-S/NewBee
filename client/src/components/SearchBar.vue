<template>
  <div
    :class="{
      startPage: this.$parent.$options.name == 'Start Page',
      homePage: this.$parent.$options.name == 'Home',
    }"
  >
    <div class="container d-flex justify-content-center">
      <div class="input-group mb-3" v-clickOutside="toggle_droplist">
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
        <ul class="list-group" id="list-group">
          <li class="list-group-item" v-for="data in myData" @click="caa(data)">
            {{ data }}
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

const clickOutside = {
  beforeMount: (el, binding) => {
    el.clickOutsideEvent = (event) => {
      // here I check that click was outside the el and his children
      if (!(el == event.target || el.contains(event.target))) {
        // and if it did, call method provided in attribute value
        binding.value(false);
      } else {
        binding.value(true);
      }
    };
    document.addEventListener("click", el.clickOutsideEvent);
  },
  unmounted: (el) => {
    document.removeEventListener("click", el.clickOutsideEvent);
  },
};

export default {
  name: "Search Bar",
  directives: {
    clickOutside,
  },
  data: function () {
    return {
      api: "api/movies/check",
      v$: useValidate(),
      searchText: "",
      searchFilter: "All",
      filter_list: ["All", "Title", "Year", "Genre", "Celebrity"],
      myData: [],
      tt: "",
      now: -1,
      listgroup: null,
    };
  },
  mounted: function () {
    // console.log("mounteded search bar");
    this.listgroup = document.getElementById("list-group");
  },
  methods: {
    toggle_droplist(show) {
      if (!show) {
        this.listgroup.style.display = "none";
      } else {
        this.listgroup.style.display = "block";
      }
    },
    caa(data) {
      this.searchText = data;
    },
    async search() {
      const searchURL =
        "/home/search?" + this.searchFilter + "=" + this.searchText;
      const result = await this.v$.$validate();
      if (result == false) {
        alert("Wrong input");
      } else {
        if (this.searchFilter == "All") {
          console.log("search All");
          this.$router.push({
            path: "/searchAll",
            query: { [this.searchFilter]: this.searchText },
          });
        } else {
          console.log("search category");
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
      this.listgroup.style.display = "block";
      // 请求限制 按了上下箭头
      if (e.keyCode === 38 || e.keyCode === 40) {
        return;
      }
      this.myData = [];
      // 限制频繁请求
      this.throttle(this.getData, window);
    },
    getData() {
      this.searchText = this.searchText.trim();
      fetch(`${this.api}?input=${this.searchText}`)
        .then((response) => response.json())
        .then((data) => {
          if (data.response == "success") {
            this.myData = data.promp;
          }
        });
    },
    throttle(method, context) {
      clearTimeout(method.tId);
      method.tId = setTimeout(function () {
        method.call(context);
      }, 1000);
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
  width: 60%;
  left: 15%;
  top: 40px;
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
  z-index: 2;
}

.list-group > li {
  /* border-color: gray; */
  border-image: none;
  border-style: solid solid none;
  border-width: 1px 1px 0;
  padding-left: 5px;
}

.list-group > li:hover {
  background-color: grey;
}

/*.form-control:focus + .list-group {
  display: block;
} */
</style>