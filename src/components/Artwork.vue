<template>
  <div class="artwork">
    <el-card body-style="padding: 0; height: 150px">
      <el-image :lazy="true" :src="img_path" :preview-src-list="[img_path]" style="min-width:100%; height:100px; vertical-align:middle" class="image" fit="cover" />
      <div class="card-details small" @click="opened = true">
        <el-row style="max-height: 1.25em; overflow:hidden">
            <el-col :span="20">
              {{data.title}}
            </el-col>
          <el-col :span="4">
              <i class="el-icon-more-outline"></i>
          </el-col>
        </el-row>
      </div>
    </el-card>
    <el-drawer :title="data.title" :visible.sync="opened" direction="btt" size="50%">
      <ul class="details">
      <li><i class="el-icon-collection-tag"></i> {{ data.accession_number }}</li>
      <li><i class="el-icon-brush"></i> {{ data.department_name }}</li>
      <li class="small" v-for="(creator, index) in data.creators" :key="index">
        <i class="el-icon-user"></i>
        <span v-if="creator.role != '' && creator.role != 'NULL'" class="creator-role"> {{ creator.role }}: </span>
        <span v-if="creator.name != ''">{{ creator.name }}</span>
      </li>
      </ul>
      <el-divider> </el-divider>
      <el-row>
        <el-col :span="18">
          <div class="tombstone">
            <span class="small">{{ data.tombstone }}</span>
          </div>
        </el-col>
        <el-col :span="6" style="padding: 0 20px 20px 0">
          <el-image :src="img_path" :preview-src-list="[img_path]" class="drawer-image image" fit="cover" />
        </el-col>
      </el-row>
    </el-drawer>
  </div>
</template>

<script>

  export default {
    name: 'Artwork',
  props: {
    data: Object
  },
  data: function() { return {
    opened: false
  }},
  computed: {
    img_path: function() { return '/images/' + this.data.accession_number + '_reduced.jpg' }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.card-details {
  padding: 20px;
}
.creator-role {
  text-transform: capitalize;
  font-weight: bold;
}
.small {
  font-size: 80%;
}
  .tombstone {
    padding: 0 20px;
  }
  .drawer-image {
    width: 100%;
    height: 150px;
  }
  .details {
    height: 5em;
    overflow-y: scroll;
  }
</style>
