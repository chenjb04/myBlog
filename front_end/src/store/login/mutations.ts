import state from './state'
import { RootStateTypes } from './types'
import { MutationTree } from 'vuex'
const mutations: MutationTree<RootStateTypes> = {
  SET_VAlIDCODE(state: RootStateTypes, data: any) {
    state.validcode.images = data
  },
  SET_USER(state: RootStateTypes, data: any) {
    state.msg = data.msg
},
}

export default mutations
