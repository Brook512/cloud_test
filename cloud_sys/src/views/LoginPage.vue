<template>
  <div class="login">
    <el-card class="login-card" shadow="always">
      <h2 class="login-title">用户登录</h2>
      <el-form :model="form" ref="form" label-width="80px" class="login-form" @submit.prevent="login">
        <el-form-item label="账号" prop="username" :rules="usernameRules">
          <el-input
            v-model="form.username"
            placeholder="请输入账号"
            prefix-icon="el-icon-user"
            type="text"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password" :rules="passwordRules">
          <el-input
            v-model="form.password"
            placeholder="请输入密码"
            prefix-icon="el-icon-lock"
            type="password"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" block size="large" native-type="submit">
            登录
          </el-button>
        </el-form-item>
      </el-form>
      <div class="register-link">
        <router-link to="/register">没有账户? 立即注册</router-link>
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
      },
      usernameRules: [
        { required: true, message: '请输入账号', trigger: 'blur' }
      ],
      passwordRules: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 6, message: '密码至少 6 位', trigger: 'blur' }
      ]
    };
  },
  methods: {
    async login() {
      // const response = await this.$api.login({
      //   username: this.form.username,
      //   password: this.form.password
      // });
      // if (response.success) {
      //   this.$router.push('/dashboard');
      // } else {
      //   alert('登录失败');
      // }
      this.$router.push('/dashboard');
    }
  }
};
</script>

<style scoped>
.login {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f4f6f8;
}

.login-card {
  width: 400px;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.login-title {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
  font-weight: 500;
}

.login-form {
  margin-bottom: 20px;
}

.register-link {
  text-align: center;
  margin-top: 10px;
  font-size: 14px;
}

.register-link a {
  color: #409eff;
}
</style>
