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
  GET_USER_INFO({ commit, state: RootStateTypes }, data: any) {
    $http.get('/api/user/get_user_info', data).then(({ status, msg, data }: any) => {
      if (status === 'success'){
        commit('SET_USER_INFO', data)
      }
    })
  },
  LOGIN({ commit,dispatch, state: RootStateTypes }, data: any) {
    $http.option('/api/user/login', data).then((data: any) => {
      if (data.status === 'success') {
        localStorage.setItem('token', data.token)
        router.go(-1)
        dispatch('GET_USER_INFO')
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
