import axios from 'axios';

const api = axios.create({
  baseURL: '*',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json' // 确保请求头是JSON格式
  }
});

// 用于获取华为云 IAM Token
async function getToken() {
  const data = {
    auth: {
      identity: {
        methods: ['password'],
        password: {
          user: {
            domain: {
              name: '*'  
            },
            name: '*',             
            password: '*'        
          }
        }
      },
      scope: {
        project: {
          name: 'cn-southwest-2'            // 项目名称，表示 Token 作用于特定区域的服务
        }
      }
    }
  };

  try {
    const response = await axios.post(
      '/api',
      data,
      {
        headers: {
          'Content-Type': 'application/json;charset=utf8' // 使用文档中推荐的 Content-Type
        }
      }
    );

    return response.headers['x-subject-token']; // IAM Token 在响应头部的 'x-subject-token'
  } catch (error) {
    console.error('Error fetching IAM token:', error.response ? error.response.data : error.message);
    throw error;
  }
}

// 添加请求拦截器，在每个请求中附加 Token
api.interceptors.request.use(async (config) => {
  const token = await getToken();
  config.headers['Authorization'] = `Bearer ${token}`;
  return config;
}, (error) => {
  return Promise.reject(error);
});

export default {
  async register(data) {
    return api.post('/register_function', data);
  },
  async login(data) {
    return api.post('/login', data);
  },
  async getFiles() {
    return api.get('/files');
  },
  async uploadFile(formData) {
    return api.post('/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
  },
  async downloadFile(fileId) {
    return api.get(`/download/${fileId}`, { responseType: 'blob' });
  }
};
