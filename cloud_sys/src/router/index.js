import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import LoginPage from '@/views/LoginPage.vue';
import DashboardPage from '@/views/DashboardPage.vue';
import RegisterPage from '@/views/RegisterPage.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/login', component: LoginPage },
  { path: '/dashboard', component: DashboardPage },
  { path: '/register', component: RegisterPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
