<template>
  <div id="menu">
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
      background-color="#4a4a4a"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item
        v-for="(item, index) in menus"
        @click="handleMenuClick(item, index, null)"
        :key="index"
        :class="{ active: index == menuIndex }"
        ><span v-if="index < 2">{{ item.text }}</span>
        <span v-else-if="index > 2 && username !== ''">{{ username }}</span>
        <span v-else>{{ item.text }}</span>
      </el-menu-item>
    </el-menu>
    <router-view></router-view>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { State, Action, namespace, Getter } from 'vuex-class'
let menuStore = namespace('login')
@Component
export default class Menu extends Vue {
  @menuStore.State(state => state.username) username: any
  public menuIndex: any = 0
  menus: Array<any> = [
    {
      level: 1,
      text: '首页',
      path: '/'
    },
    {
      level: 1,
      text: '关于',
      path: '/about'
    },
    {
      level: 1,
      text: '登录',
      path: '/login'
    },
    {
      level: 1,
      text: '注册',
      path: '/register'
    }
  ]
  handleMenuClick(item: any, index: number, i: any) {
    this.menuIndex = index
    this.$router.push({
      path: item.path
    })
  }
  // i ? (this.subI = i) : ''
}
</script>
