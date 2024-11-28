import json
from obs import ObsClient

# 配置您的访问密钥和 OBS 服务的详细信息
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
    body = json.loads(event['body'])
    username = body.get('username')
    password = body.get('password')

    if username and password:
        # 生成存储在 OBS 中的对象键（在桶中的存储路径）
        object_key = f"users/{username}.json"
        
        try:
            # 从 OBS 下载用户数据文件
            response = obs_client.getObject(
                bucketName=BUCKET_NAME,
                objectKey=object_key
            )

            # 如果文件存在，则解析 JSON 数据
            if response.status < 300:
                user_data = json.loads(response.body.decode('utf-8'))

                # 验证密码（建议使用加密方式存储密码，避免存储明文密码）
                stored_password = user_data.get('password')
                if stored_password == password:  # 密码匹配成功
                    return {
                        'statusCode': 200,
                        'body': json.dumps({'message': 'Login successful'})
                    }
                else:  # 密码错误
                    return {
                        'statusCode': 401,
                        'body': json.dumps({'message': 'Invalid username or password'})
                    }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'User not found'})
                }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': f'Error: {str(e)}'})
            }

    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid input data'})
        }
