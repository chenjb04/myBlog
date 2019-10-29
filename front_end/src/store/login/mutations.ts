import state from './state'
import { RootStateTypes } from './types'
import { MutationTree } from 'vuex'
const mutations: MutationTree<RootStateTypes> = {
  SET_VAlIDCODE(state: RootStateTypes, data: any) {
    state.validcode.images = data
  }
}

export default mutations
