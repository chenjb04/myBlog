import state from './state'
import { RootStateTypes } from './types'
import { ActionTree } from 'vuex'
import router from '@/router'
import $http from '@/utils/http'
import { Message } from 'element-ui'

const actions: ActionTree<RootStateTypes, any> = {
  GET_USER_INFO({ commit, state: RootStateTypes }, data: any) {
    $http.get('/api/user/get_user_info', data).then(({ status, msg, data }: any) => {
      if (status === 'success'){
        commit('SET_USER_INFO', data)
      }
    })
  },
}

export default actions
