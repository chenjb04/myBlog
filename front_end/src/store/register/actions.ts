import state from './state'
import { RootStateTypes } from './types'
import { ActionTree } from 'vuex'
import router from '@/router'
import $http from '@/utils/http'

const actions: ActionTree<RootStateTypes, any> = {
  GET_USER({ commit, state: RootStateTypes }, data: any) {
    $http
      .option('/api/user/get_user', data)
      .then((data:any) => {
        commit('SET_USER', data)
      })
  }
}

export default actions
