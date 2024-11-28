<template>
  <div>
    <el-row>
      <el-col :span="24">
        <el-card>

          <!-- 加载状态 -->
          <el-loading :loading="loading" text="加载中..." background="rgba(255, 255, 255, 0.7)"></el-loading>

          <!-- 文件上传 -->
          <el-upload
            action=""
            :before-upload="beforeUpload"
            :on-change="handleFileChange"
            :show-file-list="false"
            accept="image/*,application/pdf,.docx,.xlsx"
          >
            <el-button type="primary" icon="el-icon-upload">上传文件</el-button>
          </el-upload>

          <!-- 文件预览 -->
          <div v-if="previewUrl" style="margin-top: 20px;">
            <h3>文件预览</h3>
            <div v-if="previewType === 'image'">
              <img :src="previewUrl" alt="Uploaded File" style="max-width: 100%; max-height: 400px;" />
            </div>
            <div v-else-if="previewType === 'pdf'">
              <embed :src="previewUrl" width="100%" height="400px" />
            </div>
            <div v-else-if="previewType === 'docx'">
              <p>该文件为文档文件，无法预览。</p>
            </div>
            <div v-else>
              <p>无法预览该文件类型。</p>
            </div>
          </div>

          <!-- 文件列表 -->
          <el-table v-if="files.length > 0" :data="files" style="width: 100%">
            <el-table-column prop="name" label="文件名" width="250"></el-table-column>
            <el-table-column label="操作" width="180">
              <template v-slot="scope">
                <el-button @click="downloadFile(scope.row)" type="primary" size="small">下载</el-button>
              </template>
            </el-table-column>
          </el-table>

          <!-- 如果没有文件 -->
          <div v-else>
            <el-alert title="没有上传任何文件" type="info" center></el-alert>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { ElTable, ElTableColumn, ElButton, ElAlert, ElLoading, ElUpload } from 'element-plus';

export default {
  components: {
    ElTable,
    ElTableColumn,
    ElButton,
    ElAlert,
    ElLoading,
    ElUpload
  },
  data() {
    return {
      files: [], // 存储文件列表
      loading: false, // 加载状态
      previewUrl: '', // 存储预览文件URL
      previewType: '', // 存储文件类型，用于选择正确的预览方式
    };
  },
  methods: {
    // 处理文件上传前的检查
    beforeUpload(file) {
      const isImage = file.type.startsWith('image/');
      const isPdf = file.type === 'application/pdf';
      const isDocx = file.name.endsWith('.docx');
      const isValid = isImage || isPdf || isDocx;
      
      if (!isValid) {
        this.$message.error('请上传图片、PDF或文档文件');
      }
      return isValid;
    },
    
    // 处理文件变动（上传）
    handleFileChange(file) {
      const rawFile = file.raw; // 获取文件的原始对象
      if (!rawFile) {
        this.$message.error('未获取到文件的原始数据');
        return;
      }

      // 检查文件是否已存在于文件列表中（通过文件名）
      const isFileExist = this.files.some(item => item.name === rawFile.name);
      if (isFileExist) {
        this.$message.info('该文件已经上传');
        return;
      }

      // 处理文件预览
      const reader = new FileReader();
      reader.onload = (e) => {
        this.previewUrl = e.target.result;
        
        // 判断文件类型并设置预览类型
        if (rawFile.type.startsWith('image/')) {
          this.previewType = 'image';
        } else if (rawFile.type === 'application/pdf') {
          this.previewType = 'pdf';
        } else if (rawFile.name.endsWith('.docx')) {
          this.previewType = 'docx';
        }
        
        // 将文件信息推送到文件列表
        this.files.push({ name: rawFile.name, file: rawFile });
      };

      // Handle error case in FileReader
      reader.onerror = (error) => {
        this.$message.error(`文件读取失败: ${error}`);
      };
      
      reader.readAsDataURL(rawFile); // Start reading the file
    },

    // 文件下载处理
    downloadFile(file) {
      // Logic to download the file
      this.$message.success(`文件下载: ${file.name}`);
    }
  }
};
</script>

<style scoped>
/* 样式部分 */
.dashboard {
  margin-top: 50px;
}
</style>
