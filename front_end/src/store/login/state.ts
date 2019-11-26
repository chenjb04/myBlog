import { RootStateTypes } from './types'
const state: RootStateTypes = {
  validcode: {
    images: ''
  },
  msg: '', 
  username: localStorage.getItem('username') ? localStorage.getItem('username') : ''
}

export default state
