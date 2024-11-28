<template>
  <div>
    <h2>注册</h2>
    <form @submit.prevent="handleRegister">
      <input v-model="username" placeholder="用户名" required />
      <input v-model="password" type="password" placeholder="密码" required />
      <button type="submit">注册</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
// 导入默认导出的api对象
import api from '@/services/api';

export default {
  data() {
    return {
      username: '',
      password: '',
      message: ''
    };
  },
  methods: {
    async handleRegister() {
      try {
        // 调用api对象中的register方法
        const response = await api.register({
          username: this.username,
          password: this.password
        });
        this.message = response.data.message; // 根据API返回的结构获取message
      } catch (error) {
        console.log(error)
        this.message = '注册失败，请重试。';
      }
    }
  }
};
</script>
