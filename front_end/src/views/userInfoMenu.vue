<template>
  <div id="userInfoMenu">
    <el-row :gutter="20">
      <el-col :span="2"><div style="margin-top: 20px"></div></el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple" style="margin-top: 20px">
          <div style="margin-top: 20px;text-align:center;">
            <VueCropper></VueCropper>
            <!-- <el-avatar
              :src="avatarUrl"
              :size="200"
              class="avatar"
              shape="square"
              v-show="!showButton"
              @mouseenter.native="change_hover()"
              @mouseleave.native="change_hover1()"
            ></el-avatar> -->

            <h2>{{ username }}</h2>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { State, Action, namespace, Getter } from 'vuex-class'
import VueCropper from '@/components/uploadCropper.vue'
let menuStore = namespace('menu')
@Component({
  components: {
    VueCropper: VueCropper
  }
})
export default class userInfoMenu extends Vue {
  @menuStore.State(state => state.avatarUrl) avatarUrl: any
  @menuStore.State(state => state.username) username: any
  @menuStore.Action('UPLOAD_AVATAR') UPLOAD_AVATAR: any
  showButton: boolean = false
  beforeAvatarUploa(file: any) {
    let isLt2M = file.file.size / 1024 / 1024 < 2
    if (!isLt2M) {
      ;(this as any).$message.error('上传头像图片大小不能超过 2MB!')
    } else {
      let formData = new FormData()
      formData.append('file', file.file)
      this.UPLOAD_AVATAR(formData)
    }
  }
  change_hover() {
    this.showButton = true
  }
  change_hover1() {
    this.showButton = false
  }
}
</script>
<style>
#userInfoMenu .bg-purple {
  border: solid 1px #ddd;
}
#userInfoMenu .grid-content {
  min-height: 36px;
}
#userInfoMenu .avatar {
  border: 1px solid #ddd;
  width: 200px;
  height: 200px;
  overflow: hidden;
  cursor: pointer;
}
</style>
