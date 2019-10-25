<template>
  <div id="login">
    <el-form class="login-form" :model="form" ref="form" :rules='rules' status-icon>
      <el-form-item prop="username">
        <el-input
          placeholder="用户名/手机号/邮箱"
          v-model="form.username"
          prefix-icon='el-icon-user'
        >
        </el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input type="password" placeholder="密码" v-model="form.password"
        prefix-icon='el-icon-lock'>
        </el-input>
      </el-form-item>
      <el-form-item prop="validcode">
        <el-input placeholder="验证码" v-model="form.validcode" prefix-icon='el-icon-key'>
          <!-- <img src="validcode.image" class="valicode" @click="changeValicode" /> -->
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-checkbox>记住我</el-checkbox>
        <el class="login-form-forgot" href>忘记密码？</el>
        <el-button
          type="primary"
          html-type="submit"
          class="login-form-button"
          @click="submitForm('form')"
        >登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { State, Action, namespace, Getter } from 'vuex-class'
let loginStore = namespace('login')
@Component
export default class Login extends Vue {
  @loginStore.State(state => state.validcode) validcode: any
  form: any = {
    username: "",
    password: "",
    validcode: ""
  };

    rules: object = {
      username: {
        message: "请输入用户名/手机号/邮箱",
        trigger: "blur",
        required: true
      },
      password: { message: "请输入密码", trigger: "blur", required: true },
      validcode: {
        validator: this.checkValicode,
        trigger: "blur",
        required: true
      }
    };
  mounted() {
      console.log(this.validcode.images)
  }
  checkValicode(rule: any, value: string, callback: any) {
    if (value === "") {
      return callback(new Error("请输入验证码"));
    } else {
      callback();
    }
  }
  submitForm(formName: any) {
    (this.$refs[formName] as any).validate((valid: boolean) => {
      if (valid) {
        let form: any = {
          username: this.form.username,
          password: this.form.password,
          validcode: this.form.validcode
          //   validcode_img: this.validcode.image
        };
        // this.GET_USER(form)
      } else {
        return false;
      }
    });
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
</style>