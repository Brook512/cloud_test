module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'https://iam.cn-southwest-2.myhuaweicloud.com',
        changeOrigin: true,
        secure: false, // 如果目标服务器使用的是自签名的 SSL 证书，设置为 false
        pathRewrite: {
          '^/api': '/v3/auth/tokens'
        }
      }
    }
  }
};
