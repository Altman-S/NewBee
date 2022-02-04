<template>
  <div class="container">
    <nav class="navbar navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand">Navbar</a>
        <form class="d-flex">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Search"
            aria-label="Search"
          />
          <button class="btn btn-outline-success">Search</button>
        </form>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Header",
};
</script>