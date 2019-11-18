import axios, { AxiosResponse, AxiosRequestConfig } from 'axios'
import { Message } from 'element-ui'
import { stringify } from 'qs'

const $http = axios.create({
  timeout: 10000 // 超时时间
})
// 请求拦截
$http.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    const token = window.localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `JWT ${token}`
    }
    return config
  },
  (err: any) => {
    Promise.reject(err)
  }
)
// 响应拦截
$http.interceptors.response.use(
  (response: AxiosResponse) => {
    console.log(response)
    return response.data
  },
  (err: any) => {
    let errMsg = ''
    if (err & err.response.status) {
      switch (err.response.status) {
        case 401:
          errMsg = '登录状态失效，请重新登录'
          break
        case 403:
          errMsg = '拒绝访问'
          break
        case 404:
          errMsg = '请求出错(404)'
          break
        case 408:
          errMsg = '请求超时(408)'
          break
        case 500:
          errMsg = '服务器错误(500)'
          break
        case 501:
          errMsg = '服务未实现(501)'
          break
        case 502:
          errMsg = '网络错误(502)'
          break
        case 503:
          errMsg = '服务不可用(503)'
          break
        case 504:
          errMsg = '网络超时(504)'
          break
        case 505:
          errMsg = 'HTTP版本不受支持(505)'
          break
        default:
          errMsg = err.response.data.msg
          break
      }
    } else {
      errMsg = err
    }
    Message.error(errMsg)
    return Promise.reject(errMsg)
  }
)
// export default service
// let swicthTimeOut: boolean = false
// const httpConfig: any = {
//   headers: {
//     'Content-Type': 'application/x-www-form-urlencoded',
//     'Access-Control-Allow-Origin': '*',
//     'Access-Control-Max-Age': '86400',
//     'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT, DELETE',
//     'Access-Control-Allow-Headers':
//       'token, host, x-real-ip, x-forwarded-ip, accept, content-type'
//   }
// }

// const $http = (url: string, option: object = {}, header: object = {}) => {
//   return axios
//     .request({ url, headers: { ...httpConfig.headers, ...header }, ...option })
//     .then(resp => {
//       if (resp.status >= 400) {
//         throw new Error('400+Error')
//       }
//       return resp
//     })
//     .then(resp => {
//       try {
//         return resp.data
//       } catch (e) {
//         throw new Error('JSONError')
//       }
//     })
//     .then(resp => {
//       if (resp.status == 'timeout') {
//         if (swicthTimeOut == false) {
//           swicthTimeOut = true
//           Message({
//             message: resp.message || 'Error',
//             type: 'error',
//             duration: 5 * 1000
//           })
//           // return {status:"fail", data:"", msg:"因长时间未操作,请重新登录"};				}
//           // else{
//         }
//         return { status: 'timeout', data: '', msg: '' }
//         // }
//       } else {
//         swicthTimeOut = false
//         if (resp.status != 'success' && resp.status != 'default')
//           resp.status = 'fail'
//         return resp
//       }
//     })
// }

const httpMiddleware: any = {
  get: (url: string, param: object = {}) =>
    $http(`${url}?${stringify({ ...param, _k: new Date().getTime() })}`, {
      method: 'GET'
    }),
  post: (url: string, param = {}) =>
    $http(url, {
      method: 'POST',
      data: stringify({ ...param, _k: new Date().getTime() })
    }),
  put: (url: string, param = {}) =>
    $http(url, {
      method: 'PUT',
      data: stringify({ ...param, _k: new Date().getTime() })
    }),
  delete: (url: string, param = {}) =>
    $http(`${url}?${stringify({ ...param, _k: new Date().getTime() })}`, {
      method: 'DELETE'
    }),
  option: (
    url: string,
    param = {},
  ) => $http(url, { method: 'POST', data: param })
}

export default httpMiddleware
