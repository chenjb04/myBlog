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
        ><span>{{ item.text }}</span>
      </el-menu-item>
      <el-menu-item style="float:right">
        <span v-if="username === ''"
          ><el-button @click="login">登录</el-button>
          <el-button @click="register">注册</el-button></span
        >
        <span v-if="username !== ''">{{ username }}</span>
      </el-menu-item>
    </el-menu>
    <router-view></router-view>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { State, Action, namespace, Getter } from 'vuex-class'
let menuStore = namespace('menu')
@Component
export default class Menu extends Vue {
  // @menuStore.State(state => state.username) username: any
  @menuStore.Action('GET_USER_INFO') GET_USER_INFO: any
  username: string = ''
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
    }
    // {
    //   level: 1,
    //   text: '登录',
    //   path: '/login',
    //   menushow: true
    // },
    // {
    //   level: 1,
    //   text: '注册',
    //   path: '/register',
    //   menushow: true
    // }
  ]
  mounted() {
    if (localStorage.getItem('token')) {
      this.GET_USER_INFO()
    }
  }
  handleMenuClick(item: any, index: number, i: any) {
    this.menuIndex = index
    this.$router.push({
      path: item.path
    })
  }
  login() {
    this.$router.push({
      path: '/login'
    })
  }
  register() {
    this.$router.push({
      path: '/register'
    })
  }
  // i ? (this.subI = i) : ''
}
</script>
