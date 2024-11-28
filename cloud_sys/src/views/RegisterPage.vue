<template>
  <div class="register">
    <el-card class="register-card" shadow="always">
      <h2 class="register-title">用户注册</h2>
      <el-form class="register-form" :model="form" label-position="top" label-width="100px">
        <el-form-item label="用户名">
          <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password" type="password" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleRegister">注册</el-button>
        </el-form-item>
      </el-form>
      <div class="login-link">
        <router-link to="/login">已有账户？立即登录</router-link>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    handleRegister() {
      // 在此处添加注册逻辑
      console.log('注册信息:', this.form);
    }
  }
};
</script>

<style scoped>
.register {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #f4f6f8, #e9eff1);
}

.register-card {
  width: 100%;
  max-width: 450px;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  text-align: center;
  transition: box-shadow 0.3s ease-in-out;
}

.register-card:hover {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.register-title {
  font-size: 28px;
  color: #409eff;
  font-weight: 700;
  margin-bottom: 30px;
}

.register-form {
  text-align: left;
}

.el-input {
  width: 100%;
}

.login-link {
  margin-top: 20px;
  font-size: 14px;
  color: #999999;
}

.login-link a {
  color: #409eff;
  text-decoration: none;
}

.login-link a:hover {
  text-decoration: underline;
}
</style>
