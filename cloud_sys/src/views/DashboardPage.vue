<template>
  <div class="dashboard">
    <el-row class="dashboard-header">
      <el-col :span="24">
        <el-card shadow="hover">
          <h2>文件列表</h2>
          <DashboardForm @file-uploaded="refreshFiles" ref="dashboardForm" />
        </el-card>
      </el-col>
    </el-row>

    <el-row>
      <el-col :span="24">
        <el-table
          :data="fileList"
          style="width: 100%"
          size="medium"
        >
          <el-table-column prop="name" label="文件名" />
          <el-table-column prop="size" label="文件大小" />
          <el-table-column prop="uploadTime" label="上传时间" />
          <el-table-column
            label="操作"
            width="180"
          >
            <!-- Updated slot syntax with v-slot -->
            <template v-slot="scope">
              <el-button size="mini" type="text" @click="downloadFile(scope.row)">
                下载
              </el-button>
              <el-button size="mini" type="text" @click="deleteFile(scope.row)">
                删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import DashboardForm from '@/components/DashboardForm.vue'; // 引入DashboardForm组件
import { ElRow, ElCol, ElCard, ElTable, ElTableColumn, ElButton } from 'element-plus'; // 引入Element Plus组件

export default {
  components: {
    DashboardForm,
    ElRow,
    ElCol,
    ElCard,
    ElTable,
    ElTableColumn,
    ElButton
  },
  data() {
    return {
      fileList: [] // 存储文件数据
    };
  },
  mounted() {
    this.refreshFiles(); // 页面加载时获取文件列表
  },
  methods: {
    refreshFiles() {
      // 假设从后端获取文件列表
      this.fileList = this.fetchFiles();
    },
    fetchFiles() {
      // 模拟获取文件列表
      return [
        { name: 'leisa.jpg', size: '6.58MB', uploadTime: '2024-11-20 10:27' },
        { name: 'new.docx', size: '0MB', uploadTime: '2024-11-19 15:26' }
      ];
    },
    downloadFile(file) {
      console.log('下载文件:', file.name);
    },
    deleteFile(file) {
      console.log('删除文件:', file.name);
    }
  }
};
</script>

<style scoped>
/* DashboardPage的样式 */
.dashboard {
  margin-top: 50px;
}

.dashboard-header {
  margin-bottom: 20px;
}

.el-card {
  padding: 20px;
}

.el-table {
  margin-top: 20px;
}
</style>
