<template>
  <el-menu
    :default-active="activeIndex2"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    background-color="#4a4a4a"
    text-color="#fff"
    active-text-color="#ffd04b"
  >
    <el-menu-item index="1">首页</el-menu-item>
    <el-submenu index="2">
      <template slot="title"
        >我的工作台</template
      >
      <el-menu-item index="2-1">选项1</el-menu-item>
      <el-menu-item index="2-2">选项2</el-menu-item>
      <el-menu-item index="2-3">选项3</el-menu-item>
      <el-submenu index="2-4">
        <template slot="title"
          >选项4</template
        >
        <el-menu-item index="2-4-1">选项1</el-menu-item>
        <el-menu-item index="2-4-2">选项2</el-menu-item>
        <el-menu-item index="2-4-3">选项3</el-menu-item>
      </el-submenu>
    </el-submenu>
    <el-menu-item index="3" disabled>消息中心</el-menu-item>
    <el-menu-item index="4" style="float:right">
      <el-button type="primary">主要按钮</el-button></el-menu-item
    >
    <el-menu-item index="4" style="float:right"
      ><el-button type="primary">主要按钮</el-button></el-menu-item
    >
  </el-menu>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { State, Action, namespace, Getter } from 'vuex-class'
@Component
export default class Layout extends Vue {}
</script>
