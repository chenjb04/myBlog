module.exports = {
    outputDir: 'dist',
    devServer: {
        before(app) {},
        proxy: {
            // 设置代理
            '/api': {
                target: 'http://127.0.0.1:9000/',
                ws: true, // 如果要代理 websockets
                changeOrigin: false // 将主机标头的原点更改为目标URL
            },

        }
    },
}
