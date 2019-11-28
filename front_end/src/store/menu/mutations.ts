import state from './state'
import { RootStateTypes } from './types'
import { MutationTree } from 'vuex'
const mutations: MutationTree<RootStateTypes> = {
    SET_USER_INFO(state: RootStateTypes, data: any) {
        state.username = data.username
        state.isLogin = data.isLogin
    },
}

export default mutations
