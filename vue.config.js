const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave:false,
    devServer: {
        //port: 8080, // 端口
        proxy: {
            '/api': {
                target: 'http://127.0.0.1',
                changeOrigin: true, //支持跨域
                ws:true,
                pathRewrite: {
                    // 路径重写
                    '^/api': '' // 用'/api'代替target里面的地址}
                },
                onProxyReq: function(proxyReq, req, res) {
                  const token = req.headers['X_CSRFToken'] //req.headers会将大小转为小写，此处key需要转为小写
                  proxyReq.setHeader('X_CSRFToken', token)
                },
            }
        }
    }
})
