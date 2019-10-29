<template>
  <div id="login">
    <el-form
      class="login-form"
      :model="form"
      ref="form"
      :rules="rules"
      status-icon
    >
      <el-form-item prop="username">
        <el-input
          placeholder="用户名/手机号/邮箱"
          v-model="form.username"
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
      <el-form-item prop="validcode">
        <el-input
          placeholder="验证码"
          v-model="form.validcode"
          prefix-icon="el-icon-key"
        >
        </el-input>
        <img
          :src="validcode.images"
          class="login-valicode"
          @click="changeValicode"
        />
      </el-form-item>
      <el-form-item>
        <el-checkbox>记住我</el-checkbox>
        <a class="login-form-forgot">忘记密码？</a>
        <el-button
          type="primary"
          html-type="submit"
          class="login-form-button"
          @click="submitForm('form')"
          >登录</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { State, Action, namespace, Getter } from 'vuex-class'
let loginStore = namespace('login')
@Component
export default class Login extends Vue {
  @loginStore.State(state => state.validcode) validcode: any
  @loginStore.Action('GET_VALIDCODE') GET_VALIDCODE: any
  form: any = {
    username: '',
    password: '',
    validcode: ''
  }
  imageCodeId: string = ''
  // 表单验证
  rules: object = {
    username: {
      message: '请输入用户名/手机号/邮箱',
      trigger: 'blur',
      required: true
    },
    password: { message: '请输入密码', trigger: 'blur', required: true },
    validcode: {
      validator: this.checkValicode,
      trigger: 'blur',
      required: true
    }
  }
  mounted() {
    this.imageCodeId = this.generateUUID()
    this.GET_VALIDCODE({ image_code_id: this.imageCodeId })
  }
  // 验证码验证
  checkValicode(rule: any, value: string, callback: any) {
    if (value === '') {
      return callback(new Error('请输入验证码'))
    } else {
      callback()
    }
  }
  // 登录
  submitForm(formName: any) {
    ;(this.$refs[formName] as any).validate((valid: boolean) => {
      if (valid) {
        let form: any = {
          username: this.form.username,
          password: this.form.password,
          validcode: this.form.validcode
          //   validcode_img: this.validcode.image
        }
        // this.GET_USER(form)
      } else {
        return false
      }
    })
  }
  // 改变验证码
  changeValicode() {
    this.imageCodeId = this.generateUUID()
    this.GET_VALIDCODE({ image_code_id: this.imageCodeId })
  }
  // 生成验证码的随机uuid
  generateUUID() {
    let d = new Date().getTime()
    if (window.performance && typeof window.performance.now === 'function') {
      d += performance.now() //use high-precision timer if available
    }
    let uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(
      c
    ) {
      var r = (d + Math.random() * 16) % 16 | 0
      d = Math.floor(d / 16)
      return (c == 'x' ? r : (r & 0x3) | 0x8).toString(16)
    })
    return uuid
  }
}
</script>
<style>
#login .login-form {
  max-width: 300px;
  margin-top: 100px;
  margin-left: 40%;
}
#login .login-form-forgot {
  float: right;
}
#login .login-form-button {
  width: 100%;
}
#login .login-valicode {
  height: 40px;
  float: left;
  position: absolute;
  right: 0;
  top: 0;
  cursor: pointer;
}
</style>
