import axios from 'axios'
import { Message } from 'element-ui'
import { stringify } from 'qs'

let swicthTimeOut: boolean = false
const httpConfig:any = {
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Max-Age': '86400',
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT, DELETE',
    'Access-Control-Allow-Headers':
      'token, host, x-real-ip, x-forwarded-ip, accept, content-type'
  }
}

const $http = (url:string, option:object = {}, header:object = {}) => {
  return axios
    .request({ url, headers: { ...httpConfig.headers, ...header }, ...option })
    .then(resp => {
      if (resp.status >= 400) {
        throw new Error('400+Error')
      }
      return resp
    })
    .then(resp => {
      try {
        return resp.data
      } catch (e) {
        throw new Error('JSONError')
      }
    })
    .then(resp => {
      if (resp.status == 'timeout') {
        if (swicthTimeOut == false) {
          swicthTimeOut = true
          Message({
            message: resp.message || 'Error',
            type: 'error',
            duration: 5 * 1000
          })
          // return {status:"fail", data:"", msg:"因长时间未操作,请重新登录"};				}
          // else{
        }
        return { status: 'timeout', data: '', msg: '' }
        // }
      } else {
        swicthTimeOut = false
        if (resp.status != 'success' && resp.status != 'default')
          resp.status = 'fail'
        return resp
      }
    })
}

const httpMiddleware:any = {
  get: (url:string, param:object = {}) =>
    $http(`${url}?${stringify({ ...param, _k: new Date().getTime() })}`, {
      method: 'GET'
    }),
  post: (url:string, param = {}) =>
    $http(url, {
      method: 'POST',
      data: stringify({ ...param, _k: new Date().getTime() })
    }),
  put: (url:string, param = {}) =>
    $http(url, {
      method: 'PUT',
      data: stringify({ ...param, _k: new Date().getTime() })
    }),
  delete: (url:string, param = {}) =>
    $http(`${url}?${stringify({ ...param, _k: new Date().getTime() })}`, {
      method: 'DELETE'
    }),
  option: (url:string, param = {}, header = { 'Content-Type': 'application/json' }) =>
    $http(url, { method: 'POST', data: param }, header)
}

export default httpMiddleware
