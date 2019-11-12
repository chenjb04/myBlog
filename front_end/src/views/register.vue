<template>
  <div id="register">
    <el-form
      class="register-form"
      :model="form"
      ref="form"
      status-icon
      :rules="rules"
    >
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
      <el-form-item prop="repeat_password">
        <el-input
          type="password"
          placeholder="重复密码"
          v-model="form.repeat_password"
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
    repeat_password: '',
    validcode: ''
  }
  // 表单验证
  rules: object = {
    username: {
      message: '请输入用户名',
      trigger: 'blur',
      required: true
    },
    email: [
      { message: '请输入邮箱', trigger: 'blur', required: true },
      { type: 'email', message: '请输入正确的邮箱地址', trigger: 'blur' }
    ],
    password: {
      validator: this.checkPasssword,
      trigger: 'blur',
      required: true
    },
    repeat_password: {
      validator: this.checkRepeatPasssword,
      trigger: 'blur',
      required: true
    },
    validcode: { message: '请输入邮箱验证码', trigger: 'blur', required: true }
  }
  // 检查密码
  checkPasssword(rule: any, value: any, callback: any): void {
    if (value === '') {
      callback(new Error('请输入密码'))
    }
    setTimeout(() => {
      if (String(value).length > 16 || String(value).length < 6) {
        callback(new Error('密码长度在 6 到 16 个字符'))
      } else {
        callback()
      }
    }, 1000)
  }
  //检查重复密码
  checkRepeatPasssword(rule: any, value: any, callback: any): void {
    if (value === '') {
      callback(new Error('请输入密码'))
    }
    setTimeout(() => {
      if (String(value).length > 16 || String(value).length < 6) {
        callback(new Error('密码长度在 6 到 16 个字符'))
      } else {
        if (value != this.form.password) {
          callback(new Error('两次输入的密码不一致'))
        } else {
          callback()
        }
      }
    }, 1000)
  }
  // 提交注册信息
  submitForm(formName: any) {
    ;(this.$refs[formName] as any).validate((valid: boolean) => {
      if (valid) {
        let form: any = {
          username: this.form.username,
          password: this.form.password,
          validcode: this.form.validcode
        }
        // this.GET_USER(form)
      } else {
        return false
      }
    })
  }
}
</script>
<style>
#register .register-form {
  max-width: 300px;
  margin-top: 100px;
  margin-left: 40%;
}
</style>
