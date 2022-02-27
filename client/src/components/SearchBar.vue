<template>
  <div class="abc">
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
          <li>
            <button class="dropdown-item" @click="this.searchFilter = 'All'">
              All
            </button>
          </li>
          <li>
            <button class="dropdown-item" @click="this.searchFilter = 'Title'">
              Title
            </button>
          </li>
          <li>
            <button class="dropdown-item" @click="this.searchFilter = 'Genre'">
              Genre
            </button>
          </li>
          <li>
            <button class="dropdown-item" @click="this.searchFilter = 'Celebrity'">
              Celebrity
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
      />
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
export default {
  name: "Search Bar",
  data: function () {
    return {
      searchText: "",
      searchFilter: "All",
    };
  },
  methods: {
    search() {
      const searchURL = "/home?" + this.searchFilter + "=" + this.searchText;
      this.$router.push(searchURL);
    },
  },
};
</script>

<style scoped>
/*#searchBar {*/
/*  width: 400px !important;*/
/*}*/

.abc {
  left: 28%;
  top:50%;
  height: 20%;
  width: 44%;
  z-index: 1;
  position: fixed;
}

</style>