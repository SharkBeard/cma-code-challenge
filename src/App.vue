<template>
  <div id="app">
    <el-row>
      <el-col v-for="artwork in artworks" :key="artwork.accession_number" :span="4">
        <Artwork :data="artwork"/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Artwork from './components/Artwork.vue';
import jsonData from '../public/artwork.json';

export default {
  // name: 'app',
  data: function() {
    return { artworks: [] }
  },
  created: function() {
    this.artworks = jsonData;
  },
  components: {
    Artwork,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
