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
          style="width:53%"
        >
        </el-input>
        <el-button type="info" plain @click="sendCode()" v-if="!isDisabled">{{
          content
        }}</el-button>
        <el-button type="info" plain v-if="isDisabled">{{ content }}</el-button>
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
const registerStore = namespace('register')
@Component
export default class Register extends Vue {
  @registerStore.State(state => state.msg) msg: any
  @registerStore.Action('GET_USER') GET_USER: any
  @registerStore.Action('SEND_CODE') SEND_CODE: any
  @registerStore.Action('REGISTER') REGISTER: any
  form: any = {
    username: '',
    email: '',
    password: '',
    repeat_password: '',
    validcode: ''
  }
  content: string = '获取邮箱验证码'
  isDisabled: boolean = false
  $message: any
  count: number = 0
  timer: any

  mounted() {}
  // 表单验证
  rules: object = {
    username: {
      trigger: 'blur',
      required: true,
      validator: this.checkUsername
    },
    email: [
      { validator: this.checkEmail, trigger: 'blur', required: true },
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
  // 检查用户名是否存在
  checkUsername(rule: any, value: any, callback: any) {
    if (value === '') {
      callback(new Error('请输入用户名'))
    }
    this.GET_USER({ username: value, email: '' })
    setTimeout(() => {
      if (this.msg != 'ok') {
        callback(new Error(this.msg))
      } else {
        callback()
      }
    }, 1000)
  }
  // 检查邮箱是否存在
  checkEmail(rule: any, value: any, callback: any) {
    if (value === '') {
      callback(new Error('请输入邮箱'))
    }
    this.GET_USER({ username: this.form.username, email: value })
    setTimeout(() => {
      if (this.msg != 'ok') {
        callback(new Error(this.msg))
      } else {
        callback()
      }
    }, 1000)
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
          email: this.form.email,
          password: this.form.password,
          repeat_password: this.form.repeat_password,
          sms_code: this.form.validcode
        }
        this.REGISTER(form)
      } else {
        return false
      }
    })
  }
  sendCode() {
    let regEmail = /^([a-zA-Z0-9]+[_|_|.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|_|.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/
    if (this.form.email === '') {
      // ;(this as any).$message.error('请输入邮箱')
      this.$message.error('请输入邮箱')
    } else if (!regEmail.test(this.form.email)) {
      this.$message.error('请输入正确邮箱格式')
    } else {
      if (!this.timer) {
        this.SEND_CODE({ email: this.form.email })
        this.count = 60
        this.isDisabled = true
        this.timer = setInterval(() => {
          if (this.count > 0 && this.count <= 60) {
            this.count--
            this.content = this.count + 's后重新发送'
          } else {
            this.content = '获取邮箱验证码'
            this.isDisabled = false
            clearInterval(this.timer)
            this.timer = null
          }
        }, 1000)
      }
    }
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
