import state from './state'
import { RootStateTypes } from './types'
import { ActionTree } from 'vuex'
import router from '@/router'
import $http from '@/utils/http'

const actions: ActionTree<RootStateTypes, any> = {
  GET_VALIDCODE({ commit, state: RootStateTypes }, data: string) {
    $http
      .get('/api/user/image_code', data)
      .then(({ status, msg, data }: any) => {
        if (status == 'success') {
          commit('SET_VAlIDCODE', data)
        }
      })
  }
}

export default actions
