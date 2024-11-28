# test1
## Architecture

cloud-drive/
├── public/
│   ├── index.html                    # 项目的入口HTML文件
├── src/
│   ├── assets/                       # 存放静态资源（如图片、样式等）
│   ├── components/                   # 存放可复用的组件
│   │   ├── RegisterForm.vue              # 用户注册组件
│   │   ├── FileUploadForm.vue            # 文件上传组件
│   ├── views/                        # 存放页面级别的视图组件
│   │   ├── HomePage.vue                  # 首页或其他主要页面
│   │   ├── LoginPage.vue                 # 登录页面
│   │   ├── DashboardPage.vue             # 用户文件管理和展示页面
│   │   ├── RegisterPage.vue             # 注册
│   ├── router/                       # 存放Vue Router相关的配置
│   │   └── index.js                  # 配置页面路由
│   ├── services/                     # 存放与后端交互的API调用逻辑
│   │   └── api.js                    # 后端API请求（例如注册、文件上传等）
│   ├── App.vue                       # 根组件
│   └── main.js                       # Vue实例初始化
├── package.json                      # 项目依赖和配置信息
├── vue.config.js                     # Vue CLI的配置
└── README.md                         # 项目说明


## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
