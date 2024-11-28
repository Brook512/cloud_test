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
        # 构造要存储的用户信息
        user_data = {
            'username': username,
            'password': password  # 密码应加密处理，存储敏感信息时一定要注意安全
        }

        # 生成对象键（在桶中的存储路径）
        object_key = f"users/{username}.json"

        try:
            # 将用户数据保存为 JSON 并上传到 OBS
            response = obs_client.putContent(
                bucketName=BUCKET_NAME,
                objectKey=object_key,
                content=json.dumps(user_data)
            )
            # console.log(response)
            # 关闭连接
            obs_client.close()

            if response.status < 300:
                return {
                    'statusCode': 200,
                    'body': json.dumps({'message': 'Registration successful'})
                }
            else:
                return {
                    'statusCode': 500,
                    'body': json.dumps({'message': f'Failed to save user information, {response}'})
                }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': f'Error: {str(e)}'})
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid data'})
        }
