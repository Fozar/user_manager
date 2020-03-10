<template>
  <div id="app">
    <Wrapper />
  </div>
</template>

<script>
  import Wrapper from "./components/Wrapper";

  export default {
    name: "App",
    components: {
      Wrapper
    }
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Inter&display=swap&subset=cyrillic');
  body, html, #app {
    margin: 0;
    height: 100%;
    width: 100%;
    min-height: 100vh;
    overflow: hidden;
    min-width: 1250px;
    font-family: 'Inter', sans-serif;
  }
  body {
    position: fixed;
  }
</style>
