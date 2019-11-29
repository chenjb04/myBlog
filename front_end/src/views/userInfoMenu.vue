<template>
  <div id="userInfoMenu">
    <el-row>
      <el-col :span="6">
        <div class="grid-content bg-purple" style="margin-top: 20px">
          <el-menu default-active="2">
            <el-menu-item index="4">
              <i class="el-icon-setting"></i>
              <span slot="title">个人信息</span>
            </el-menu-item>
          </el-menu>
          <el-menu default-active="2">
            <el-menu-item index="4">
              <i class="el-icon-setting"></i>
              <span slot="title">个人信息</span>
            </el-menu-item>
          </el-menu>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { State, Action, namespace, Getter } from 'vuex-class'
let menuStore = namespace('menu')
@Component
export default class userInfoMenu extends Vue {}
</script>
<style>
#userInfoMenu .bg-purple {
  background-color: #fff;
}
#userInfoMenu .grid-content {
  min-height: 36px;
}
</style>
