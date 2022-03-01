<template>
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
      />
      <div class="input-group-append">
        <button class="btn btn-primary" @click="search">
          <i class="fas fa-search"></i>
        </button>
      </div>
    </div>
  </div>
</template>


<script>
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";

export default {
  name: "Search Bar",
  data: function () {
    return {
      v$: useValidate(),
      searchText: "",
      searchFilter: "All",
      filter_list: ["All", "Title", "Year", "Genre", "Celebrity"],
    };
  },
  methods: {
    search() {
    //   console.log(this.v$);
      const searchURL =
        "/home/search?" + this.searchFilter + "=" + this.searchText;
      this.$router.push({
        path: "/home/search",
        query: { [this.searchFilter]: this.searchText },
      });
    },
    changeFilter(filter) {
      this.searchFilter = filter;
      this.searchText = "";
    },
  },
  validations: function () {
    return { searchText: { required } };
  },
};
</script>

<style scoped>
#searchBar {
  width: 100px !important;
}
</style>