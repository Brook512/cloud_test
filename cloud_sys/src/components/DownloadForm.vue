<template>
    <div class="download-form">
      <h2>文件下载</h2>
      <form @submit.prevent="handleDownload">
        <div>
          <label for="fileId">文件 ID:</label>
          <input type="text" v-model="fileId" id="fileId" required />
        </div>
        <button type="submit" :disabled="isDownloading">
          {{ isDownloading ? '正在下载...' : '下载文件' }}
        </button>
      </form>
      <div v-if="downloadError" class="error-message">
        <p>下载出错，请稍后重试。</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import api from '@/services/api'; // 假设你已经有一个封装的api服务
  
  export default {
    name: 'DownloadForm',
    setup() {
      const fileId = ref('');
      const isDownloading = ref(false);
      const downloadError = ref(false);
  
      // 处理文件下载
      const handleDownload = async () => {
        if (!fileId.value) return;
  
        isDownloading.value = true;
        downloadError.value = false;
  
        try {
          const response = await api.get(`/download/${fileId.value}`, { responseType: 'blob' });
          
          // 创建文件链接并触发下载
          const fileURL = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = fileURL;
          link.setAttribute('download', fileId.value);  // 设置默认下载文件名
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
  
          isDownloading.value = false;
        } catch (error) {
          console.error('Error downloading file:', error);
          downloadError.value = true;
          isDownloading.value = false;
        }
      };
  
      return {
        fileId,
        isDownloading,
        downloadError,
        handleDownload
      };
    }
  };
  </script>
  
  <style scoped>
  .download-form {
    width: 300px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  
  .download-form h2 {
    text-align: center;
  }
  
  .download-form form {
    display: flex;
    flex-direction: column;
  }
  
  .download-form label {
    margin-bottom: 5px;
  }
  
  .download-form input {
    margin-bottom: 10px;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .download-form button {
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .download-form button:disabled {
    background-color: #ccc;
  }
  
  .error-message {
    margin-top: 10px;
    color: red;
    text-align: center;
  }
  </style>
  