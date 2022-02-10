<template>
  <nav aria-label="Page navigation example">
    <ul class="pagination justify-content-center">
      <li class="page-item" v-if="page_number > 1">
        <button class="page-link" @click="change_page(page_number - 1)">
          Previous
        </button>
      </li>
      <li
        v-for="i in total_page"
        class="page-item"
        :class="{ active: page_number == i }"
      >
        <button class="page-link" @click="change_page(i)">{{ i }}</button>
      </li>
      <li class="page-item" v-if="page_number < total_page">
        <button class="page-link" @click="change_page(page_number + 1)">
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
    page_number: Number,
  },
  methods: {
    change_page(i) {
      this.$emit("changePage", i);
    },
  },
  computed: {},
};
</script>
