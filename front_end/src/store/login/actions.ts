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
  LOGIN({ commit, state: RootStateTypes }, data: any) {
    $http.option('/api/user/login', data).then((data: any) => {
      if (data.status === 'success') {
        localStorage.setItem('token', data.token)
        router.go(-1)
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
