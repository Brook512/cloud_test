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
    # 获取文件ID（实际是文件名）
    file_name = event.get('queryStringParameters', {}).get('file_id')

    if not file_name:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'File ID is required'})
        }

    object_key = f"uploads/{file_name}"

    try:
        # 从 OBS 下载文件
        response = obs_client.getObject(
            bucketName=BUCKET_NAME,
            objectKey=object_key
        )

        if response.status < 300:
            return {
                'statusCode': 200,
                'body': response.body,
                'isBase64Encoded': True,  # 如果是图片或视频文件，标记为 Base64 编码
                'headers': {
                    'Content-Type': response.headers.get('Content-Type', 'application/octet-stream'),
                    'Content-Disposition': f'attachment; filename={file_name}'
                }
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'File not found'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Error: {str(e)}'})
        }
