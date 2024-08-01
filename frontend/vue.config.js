const { defineConfig } = require('@vue/cli-service')
const webpack = require('webpack');


module.exports = defineConfig({
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
        __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false',
      })
    ],
  },
  transpileDependencies: true,
  devServer: {
    host: '0.0.0.0',
    port: 80
  },
})
