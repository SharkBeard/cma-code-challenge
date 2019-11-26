<template>
  <div class="artwork">
    <el-card body-style="padding: 0; height: 150px">
      <el-image :lazy="true" :src="img_path" style="min-width:100%; max-height:100px" class="image" fit="cover" />
      <div class="card-details small" @click="opened = true">
          {{data.title}}
      </div>
    </el-card>
    <el-drawer :title="data.title" :visible.sync="opened" direction="btt">
      <li><i class="el-icon-collection-tag"></i> {{ data.accession_number }}</li>
      <li><i class="el-icon-brush"></i> {{ data.department }}</li>
      <li class="small"><i class=""></i> {{ data.tombstone }}</li>
      <el-divider>
        <span v-if="data.creator_role != ''" class="creator-role"> {{ data.creator_role }}: </span>
      </el-divider>
      <li class="small">
        <i class="el-icon-user"></i>
        {{ data.creator_description }}
      </li>
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
}
.small {
  font-size: 80%;
}
</style>
