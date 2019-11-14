import state from './state'
import { RootStateTypes } from './types'
import { ActionTree } from 'vuex'
import router from '@/router'
import $http from '@/utils/http'
import { Message } from 'element-ui'

const actions: ActionTree<RootStateTypes, any> = {
  GET_USER({ commit, state: RootStateTypes }, data: any) {
    $http.option('/api/user/get_user', data).then((data: any) => {
      commit('SET_USER', data)
    })
  },
  SEND_CODE({ commit, state: RootStateTypes }, data: any) {
    $http.option('/api/user/send_mail', data).then((data: any) => {
      if (data.status === 'success') {
        Message({
          message: data.msg,
          type: 'success'
        })
        commit('SEND_CODE', data)
      } else {
        Message({
          message: data.msg,
          type: 'error'
        })
      }
    })
  },
  REGISTER({ commit, state: RootStateTypes }, data: any) {
    $http.option('/api/user/register', data).then((data: any) => {
      if (data.status === 'success') {
        Message({
          message: data.msg,
          type: 'success'
        })
        router.push('/login')
      } else {
        Message({
          message: data.msg,
          type: 'error'
        })
      }
    })
  }
}

export default actions
