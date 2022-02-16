<template>
  <nav aria-label="Page navigation example">
    <ul class="pagination justify-content-center">
      <li class="page-item" v-if="current_page > 1">
        <button class="page-link" @click="change_page(current_page - 1)">
          Previous
        </button>
      </li>
      <li
        v-for="page in pages"
        class="page-item"
        :class="{ active: current_page == page }"
      >
        <button class="page-link" @click="change_page(page)">{{ page }}</button>
      </li>
      <li class="page-item" v-if="current_page < total_page">
        <button class="page-link" @click="change_page(current_page + 1)">
          Next
        </button>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    total_page: Number,
    current_page: {
      type: Number,
      required: true,
    },
    maxVisibleButtons: {
      type: Number,
      required: false,
      default: 10,
    },
    showItem: {
      type: Number,
      required: false,
      default: 5,
    },
  },
  methods: {
    change_page(i) {
      this.$emit("changePage", i);
    },
  },
  computed: {
    pages: function () {
      var pag = [];
      if (this.current_page < this.showItem) {
        var i = Math.min(this.showItem, this.total_page);
        while (i) {
          pag.unshift(i--);
        }
      } else {
        var middle = this.current_page - Math.floor(this.showItem / 2), 
          i = this.showItem;
        if (middle > this.total_page - this.showItem) {
          middle = this.total_page - this.showItem + 1;
        }
        while (i--) {
          pag.push(middle++);
        }
      }
      return pag;
    },
  },
};
</script>
