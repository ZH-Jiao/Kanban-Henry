<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <h1>Kanban</h1>
    <!-- <router-link to="/detail">detail</router-link> -->
    <router-view />
    
    <!-- <Kanban/> -->
  </div>
</template>

<script>
// import Kanban from './components/Kanban.vue'

export default {
  name: 'App',
  components: {
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
