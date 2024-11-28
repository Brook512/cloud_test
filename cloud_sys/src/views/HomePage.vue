<template>
  <div class="home">
    <el-card class="welcome-card" shadow="always">
      <h1 class="home-title">欢迎使用云盘系统</h1>
      <p class="home-description">
        通过云盘，您可以轻松上传、下载和管理您的文件。
      </p>
      <div class="home-actions">
        <router-link to="/login">
          <el-button type="primary" size="large" class="home-button">登录</el-button>
        </router-link>
        <router-link to="/register">
          <el-button type="success" size="large" class="home-button">注册</el-button>
        </router-link>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
};
</script>

<style scoped>
.home {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f4f6f8;
}

.welcome-card {
  text-align: center;
  padding: 30px;
  width: 400px;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.home-title {
  font-size: 28px;
  color: #409eff;
  font-weight: 600;
  margin-bottom: 20px;
}

.home-description {
  font-size: 18px;
  color: #333;
  margin-bottom: 30px;
}

.home-actions {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.home-button {
  width: 120px;
}
</style>
