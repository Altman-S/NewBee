module.exports = {
    devServer: {
        hot: true,
        host: 'localhost',
        proxy: {
            '/api': {
                target: 'http://104.155.34.47:5000',
                changeOrigin: true,
                pathRewrite: { '^/api': '/api' },
                logLevel: 'debug'
            },
        }
    },

    assetsDir: 'static'
}
