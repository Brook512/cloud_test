import { createApp } from 'vue';  // 引入 createApp
import App from './App.vue';
import router from './router';
import api from './services/api';
import ElementPlus from 'element-plus';  // 引入 element-plus
import 'element-plus/dist/index.css';    // 引入 element-plus 样式

// 创建 Vue 应用实例
const app = createApp(App);

// 将API接口挂载到全局，使得每个组件可以通过 this.$api 访问
app.config.globalProperties.$api = api;  // 使用 globalProperties 来挂载全局方法

// 配置并挂载路由
app.use(router);

// 使用 element-plus 插件
app.use(ElementPlus);

// 挂载 Vue 应用
app.mount('#app');
