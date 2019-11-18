module.exports = {
  outputDir: 'dist',
  devServer: {
    proxy: {
      // 设置代理
      '/api': {
        target: 'http://127.0.0.1:5000/',
        ws: true, // 如果要代理 websockets
        changeOrigin: false // 将主机标头的原点更改为目标URL
      }
    }
  }
}
