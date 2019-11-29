import state from './state'
import { RootStateTypes } from './types'
import { MutationTree } from 'vuex'
const mutations: MutationTree<RootStateTypes> = {
    SET_USER_INFO(state: RootStateTypes, data: any) {
        state.username = data.username
        state.isLogin = data.isLogin
        state.avatarUrl = data.avatar_url
    },
}

export default mutations
