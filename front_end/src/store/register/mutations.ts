import state from './state'
import { RootStateTypes } from './types'
import { MutationTree } from 'vuex'
const mutations: MutationTree<RootStateTypes> = {
    SET_USER(state: RootStateTypes, data: any) {
        state.msg = data.msg
    },
    SEND_CODE(state: RootStateTypes, data: any) {
        
    }
}

export default mutations
