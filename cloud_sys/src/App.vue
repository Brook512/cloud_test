<template>
  <div id="app">
    <router-view></router-view> 
  </div>
</template>

<script>
export default {
  name: 'App',
  mounted() {
    console.log('App component mounted');
  },
};
</script>

<style scoped>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
}

router-view {
  display: block;
  height: 100vh;  /* 使得页面内容充满整个视口 */
}
</style>
