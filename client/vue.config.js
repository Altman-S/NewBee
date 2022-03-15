module.exports = {
    devServer: {
        hot: true,
        host: 'localhost',
        proxy: {
            '/api': {
                target: 'http://localhost:5000',
                changeOrigin: true,
                pathRewrite: { '^/api': '/api' },
                logLevel: 'debug'
            },
        }
    },

    assetsDir: 'static'
}
