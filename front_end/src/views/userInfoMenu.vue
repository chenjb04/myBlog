<template>
  <div id="userInfoMenu">
    <el-row :gutter="20">
      <el-col :span="2"><div style="margin-top: 20px"></div></el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple" style="margin-top: 20px">
          <div style="margin-top: 20px;text-align:center;">
            <el-upload
              action=""
              :show-file-list="false"
              :before-upload="beforeAvatarUpload"
              :on-change="fileChange"
              :http-request="uploadAvatar"
              accept="image/png,image/jpeg,image/gif"
              ><hoverMask @click="handleClick">
                <el-avatar
                  :src="avatarUrl"
                  :size="200"
                  class="avatar"
                  shape="square"
                ></el-avatar>
                <template v-slot:action>
                  <i class="el-icon-camera">修改头像</i>
                </template>
              </hoverMask></el-upload
            >
            <VueCropper ref="mychild"></VueCropper>
            <h2>{{ username }}</h2>
            <hr style="border-top: 1px solid rgba(0,0,0,.1)"/>
          </div>
          <div style="text-align:center">
            <el-menu
              class="el-menu-vertical-demo"
              background-color="#fff"
              text-color="#777777"
              active-text-color="#ffd04b"
              style="border-right: 0;"
            >
              <el-menu-item
                v-for="(item, index) in menus"
                @click="handleMenuClick(item, index, null)"
                :key="index"
                :class="{ active: index == menuIndex }"
                style="text-align:center;width:50%;margin-left:25%"
                ><span>{{ item.text }}</span>
              </el-menu-item></el-menu
            >
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
import hoverMask from '@/components/hoverMask.vue'
let menuStore = namespace('menu')
@Component({
  components: {
    VueCropper: VueCropper,
    hoverMask: hoverMask
  }
})
export default class userInfoMenu extends Vue {
  @menuStore.State(state => state.avatarUrl) avatarUrl: any
  @menuStore.State(state => state.username) username: any
  @menuStore.Action('UPLOAD_AVATAR') UPLOAD_AVATAR: any
  showButton: boolean = false
  newFile: any
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
  ]
  beforeAvatarUpload(file: any) {
    let isLt2M = file.size / 1024 / 1024 < 2
    if (!isLt2M) {
      ;(this as any).$message.error('上传头像图片大小不能超过 2MB!')
    }
    return isLt2M
  }
  uploadAvatar(param: any) {}
  fileChange(file: any) {
    ;(this as any).$refs.mychild.openCrop = true
    ;(this as any).$refs.mychild.change(file.raw)
  }
  handleClick() {}
}
</script>
<style scoped>
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
