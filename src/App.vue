<template>
  <div id="app">
    <el-row :gutter="0">
      <el-col v-for="(artwork, index) in artworks" :key="index" :span="4">
        <Artwork :data="artwork"/>
      </el-col>
    </el-row>
    <el-button @click="console.log(artworks);">Test</el-button>
  </div>
</template>

<script>
import Artwork from './components/Artwork.vue';
// const axios = require('axios').default;
// export function readFile(file) {
//   return new Promise((resolve) => {
//     let reader = new FileReader();
//     reader.onLoad = () => resolve(reader.result);
//     reader.readAsText(file);
//   });
// }
// export async function getInput(instance) {
//   instance.artworks = await readFile('./artwork.json');
// }
let artworks = [];
import(
        /* webpackChunkName: "jsonArtwork" */
        '../public/artwork.json')
        .then(({default: jsonArtwork}) => jsonArtwork);
        // .then(({default: jsonArtwork}) => {
        //     artworks = jsonArtwork;
        // });
import jsonData from '../public/artwork.json';
artworks = jsonData;
export default {
  // name: 'app',
  data: function() {
    return { artworks: [] }
  },
  created: function()
  {
    this.artworks = [{
      "accession_number": "2015.584",
      "creator_description": "John Taylor Arms (American, 1887-1953)",
      "creator_role": "artist",
      "department": "Prints",
      "id": "86508",
      "title": "Gates of the City",
      "tombstone": "New York Series: Gates of the City, 1922. John Taylor Arms (American, 1887-1953). Color etching and aquatint; platemark: 21.5 x 20.2 cm (8 7/16 x 7 15/16 in.); sheet: 31.1 x 26.2 cm (12 1/4 x 10 5/16 in.). The Cleveland Museum of Art, Gift of Carole W. and Charles B. Rosenblatt 2015.584 Courtesy of John Taylor Arms/ \u00a9 Suzanne Arms Hawkins"
    }];
    this.artworks = artworks;
    // this.artworks = jsonArtwork;
    // this.artworks = Array(9).fill(this.artworks[0])
    // let instance = this;
    // axios.get('/artwork.json')
    //   .then(function(response) {
    //     instance.artworks = response.body;
    //   });
    // getInput(this);
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
