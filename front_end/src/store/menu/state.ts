import { RootStateTypes } from './types'
const state: RootStateTypes = {
  username: '',
  isLogin: Number(localStorage.getItem('_a')),
  loading:false
}

export default state
