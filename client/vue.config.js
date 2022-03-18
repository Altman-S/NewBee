module.exports = {
    devServer: {
        hot: true,
        host: 'localhost',
        proxy: {
            '/api': {
                // target: 'http://104.155.34.47:5000',
                target: 'http://127.0.0.1:5000',
                changeOrigin: true,
                pathRewrite: { '^/api': '/api' },
                logLevel: 'debug'
            },
        }
    },

    assetsDir: 'static'
}
