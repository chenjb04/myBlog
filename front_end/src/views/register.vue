<template>
  <div id="register">
    <el-form class="register-form" :model="form" ref="form" status-icon>
      <el-form-item prop="username">
        <el-input
          placeholder="用户名"
          v-model="form.username"
          prefix-icon="el-icon-user"
        ></el-input>
      </el-form-item>
      <el-form-item prop="email">
        <el-input
          placeholder="邮箱"
          v-model="form.email"
          prefix-icon="el-icon-user"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          type="password"
          placeholder="密码"
          v-model="form.password"
          prefix-icon="el-icon-lock"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          type="password"
          placeholder="重复密码"
          v-model="form.password"
          prefix-icon="el-icon-lock"
        ></el-input>
      </el-form-item>
      <el-form-item prop="validcode">
        <el-input
          placeholder="验证码"
          v-model="form.validcode"
          prefix-icon="el-icon-key"
        >
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-button
          type="primary"
          html-type="submit"
          class="register-form-button"
          @click="submitForm('form')"
          >注册</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { State, Action, namespace, Getter } from 'vuex-class'
@Component
export default class Register extends Vue {
  form: any = {
    username: '',
    email: '',
    password: '',
    validcode: ''
  }
}
</script>
