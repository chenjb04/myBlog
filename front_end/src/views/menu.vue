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
      <el-menu-item style="float:right" v-show="isLogin === 0">
        <span
          ><el-button @click="login">登录</el-button>
          <el-button @click="register">注册</el-button></span
        >
      </el-menu-item>
      <el-submenu style="float:right" v-show="isLogin === 1" index="3">
        <template slot="title">
          <el-avatar :src="avatarUrl"></el-avatar>
          {{ username }}
        </template>
        <el-menu-item index="3-1"
          ><router-link :to="{ name: 'userinfo' }"
            >个人中心</router-link
          ></el-menu-item
        >
        <el-menu-item index="3-2"
          ><span @click="logout()">退出登录</span></el-menu-item
        >
      </el-submenu>
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
  @menuStore.State(state => state.isLogin) isLogin: any
  @menuStore.State(state => state.avatarUrl) avatarUrl: any
  @menuStore.State(state => state.loading) loading: any
  @menuStore.State(state => state.username) username: any
  @menuStore.Action('GET_USER_INFO') GET_USER_INFO: any
  @menuStore.Mutation('SET_USER_INFO') SET_USER_INFO: any
  public menuIndex: any = 0
  public flgI: any = -1
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
  handleMenuClick(item: any, index: number, i: any) {
    if (item.path) {
      this.menuIndex = index
      this.$router.push({
        path: item.path
      })
    }
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
  logout() {
    localStorage.removeItem('token')
    localStorage.setItem('_a', '0')
    this.SET_USER_INFO({ username: '', isLogin: 0, avatarUrl: '' })
    this.$router.push({
      path: '/'
    })
  }
}
</script>
