<template>
  <div>
    <h2>文件上传</h2>
    <input type="file" @change="handleFileUpload" />
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>

import api from '@/services/api';
export default {
  data() {
    return {
      file: null,
      message: ''
    };
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.uploadFileToServer(file);
      }
    },
    async uploadFileToServer(file) {
      try {
        const formData = new FormData();
        formData.append('file', file);
        const response = await api.uploadFile(formData);
        this.message = response.message;
      } catch (error) {
        this.message = '文件上传失败，请重试。';
      }
    }
    
  }
};
</script>
