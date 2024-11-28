import json
import os
from obs import ObsClient
from urllib.parse import unquote

# 配置您的 OBS 访问密钥和存储桶信息
ACCESS_KEY = 'AFOWQEWCK5ABZ9PL0WEK'
SECRET_KEY = 'mNxYBEmxtdMdIAAfJHEOadlK17iXuxMsLIQvZird'
SERVER = 'https://obs.cn-southwest-2.myhuaweicloud.com'  # 例如：https://obs.cn-north-4.myhuaweicloud.com

# 创建 OBS 客户端
obs_client = ObsClient(
    access_key_id=ACCESS_KEY,
    secret_access_key=SECRET_KEY,
    server=SERVER
)

def handler(event, context):
    # 获取上传的文件
    file_data = event.get('body', {})
    
    if 'file' not in file_data:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'No file uploaded'})
        }

    file = file_data['file']
    file_name = unquote(file['filename'])
    file_content = file['content']

    # 生成对象存储的文件路径
    object_key = f"uploads/{file_name}"

    try:
        # 上传文件到 OBS
        response = obs_client.putContent(
            bucketName=BUCKET_NAME,
            objectKey=object_key,
            content=file_content
        )

        if response.status < 300:
            file_url = f"{SERVER}/{BUCKET_NAME}/{object_key}"
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'File uploaded successfully', 'file_url': file_url})
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Failed to upload file'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Error: {str(e)}'})
        }
