import state from './state'
import { RootStateTypes } from './types'
import { ActionTree } from 'vuex'
import router from '@/router'
import $http from '@/utils/http'
import { Message } from 'element-ui'

const actions: ActionTree<RootStateTypes, any> = {
  GET_VALIDCODE({ commit, state: RootStateTypes }, data: string) {
    $http
      .get('/api/user/image_code', data)
      .then(({ status, msg, data }: any) => {
        if (status === 'success') {
          commit('SET_VAlIDCODE', data)
        }
      })
  },
  GET_USER({ commit, state: RootStateTypes }, data: any) {
    $http.option('/api/user/check_user', data).then((data: any) => {
      commit('SET_USER', data)
    })
  },
  LOGIN({ commit, dispatch, state: RootStateTypes }, data: any) {
    $http.option('/api/user/login', data).then((data: any) => {
      if (data.status === 'success') {
        localStorage.setItem('token', data.token)
        // 1 已登录 0 未登录
        localStorage.setItem('_a', '1')
        router.go(-1)
      } else {
        Message({
          message: data.msg,
          type: 'error'
        })
        dispatch('GET_VALIDCODE')
      }
    })
  }
}

export default actions
