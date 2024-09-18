import json
import hmac
import hashlib
import base64
import random
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, ImageSendMessage, VideoSendMessage

# 你的 LINE Bot API token
line_bot_api = LineBotApi('0zklkLsDpBpKOYBwv9ZkBHOJEQx/dcKMOwPMqYZ9a9q5BZUMHaPKLdV//QftJFLC5Ze762D6Zg2Wsjiv3zQ4S7KxHr2g4q200nqK2N4xF9SMWY/CM94xEkqaRsWbPSkako32cj8UQjMFXrvkzkHk4wdB04t89/1O/w1cDnyilFU=')
channel_secret = 'd4ed8326b8432727b3ca7fcb75e53b8c'
handler = WebhookHandler(channel_secret)

#隨機圖的 URL 列表
#抽
IMAGE_URLS_SET1 = [
    'https://i.imgur.com/v4Lgrki.png',
    'https://i.imgur.com/GVjj97G.png',
    'https://i.imgur.com/dlnrgGh.png',
    'https://i.imgur.com/CMYOQP5.png',
    'https://i.imgur.com/l1FtOvN.png',
    'https://i.imgur.com/sFejQbw.png'
]
#小桃
IMAGE_URLS_SET2 = [
    'https://i.imgur.com/l1FtOvN.png',
    'https://i.imgur.com/sFejQbw.png',
    'https://i.imgur.com/d6Aiq3H.gif'
]
#小八貓
IMAGE_URLS_SET3 = [
    'https://i.imgur.com/v4Lgrki.png',
    'https://i.imgur.com/GVjj97G.png',
    'https://i.imgur.com/dlnrgGh.png',
    'https://i.imgur.com/CMYOQP5.png'
]
#烏薩奇
IMAGE_URLS_SET4 = [
    'https://i.imgur.com/Cklmarp.jpg',
    'https://i.imgur.com/b1NdUzK.jpg',
    'https://i.imgur.com/Jkvh6Xl.jpg',
    'https://i.imgur.com/EMe6mco.gif'
]

VIDEO_URLS_SET1 = [   
    {
        'video': 'https://i.imgur.com/yzA9zjI.mp4',      # 影片 URL
        'preview': 'https://imgur.com/yzA9zjI.jpg'  # 影片預覽圖 URL
    },
    {
        'video': 'https://i.imgur.com/qQ3xio4.mp4',     
        'preview': 'https://i.imgur.com/qQ3xio4.jpg' 
    }

]

def linebot(request):
    try:
        # 輸出所有請求信息
        print(f'Headers: {request.headers}')

        # 確認X-Line-Signature 是否存在於標頭
        signature = request.headers.get('X-Line-Signature')
        if not signature:
            print('Error: Missing X-Line-Signature')
            return 'Error: Invalid source', 403
        
        # 取得 request body
        body = request.get_data(as_text=True)
        print(f'Body: {body}')  # 日志輸出
        
        # 驗證簽名
        hash = hmac.new(channel_secret.encode('utf-8'),
                        body.encode('utf-8'), hashlib.sha256).digest()
        calculated_signature = base64.b64encode(hash).decode('utf-8')
        print(f'Calculated signature: {calculated_signature}')  # 日志樹出計算的簽名
        
        # 比對 X-Line-Signature 與計算出的簽名
        if calculated_signature != signature:
            print('Error: Invalid signature')
            return 'Invalid signature', 403

        json_data = json.loads(body)
        print(f'JSON data: {json_data}')  # 日志输出 JSON 數據
        
        handler.handle(body, signature)
        
        event = json_data['events'][0]
        reply_token = event['replyToken']          # 取得 reply token
        message_text = event['message']['text']    # 取得訊息 
        print(f'Reply token: {reply_token}, Message: {message_text}')  # 日志輸出回復 token 和消息
        
        # 如果收到“抽”字样的消息，回復隨機圖片
        if message_text == '抽':
            # 隨機選擇發送圖片或影片
            choice = random.choice(['image', 'video'])
            
            if choice == 'image':
                # 隨機選擇圖片
                image_url = random.choice(IMAGE_URLS_SET1)
                line_bot_api.reply_message(
                    reply_token,
                    ImageSendMessage(
                        original_content_url=image_url,
                        preview_image_url=image_url
                    )
                )
            else:
                # 隨機選擇影片
                video_choice = random.choice(VIDEO_URLS_SET1)
                line_bot_api.reply_message(
                    reply_token,
                    VideoSendMessage(
                        original_content_url=video_choice['video'],
                        preview_image_url=video_choice['preview']
                    )
                )
        
        elif message_text == '小桃':
            # 隨機選擇發送圖片或影片
            choice = random.choice(['image', 'video'])
            
            if choice == 'image':
                # 隨機選擇圖片
                image_url = random.choice(IMAGE_URLS_SET2)
                line_bot_api.reply_message(
                    reply_token,
                    ImageSendMessage(
                        original_content_url=image_url,
                        preview_image_url=image_url
                    )
                )
            else:
                # 隨機選擇影片
                video_choice = random.choice(VIDEO_URLS_SET1)
                line_bot_api.reply_message(
                    reply_token,
                    VideoSendMessage(
                        original_content_url=video_choice['video'],
                        preview_image_url=video_choice['preview']
                    )
                )

        elif message_text == '小八貓':
            # 隨機選擇發送圖片或影片
            choice = random.choice(['image', 'video'])
            
            if choice == 'image':
                # 隨機選擇圖片
                image_url = random.choice(IMAGE_URLS_SET3)
                line_bot_api.reply_message(
                    reply_token,
                    ImageSendMessage(
                        original_content_url=image_url,
                        preview_image_url=image_url
                    )
                )
            else:
                # 隨機選擇影片
                video_choice = random.choice(VIDEO_URLS_SET1)
                line_bot_api.reply_message(
                    reply_token,
                    VideoSendMessage(
                        original_content_url=video_choice['video'],
                        preview_image_url=video_choice['preview']
                    )
                )
            
        elif message_text == '烏薩奇':
            # 隨機選擇發送圖片或影片
            choice = random.choice(['image', 'video'])
            
            if choice == 'image':
                # 隨機選擇圖片
                image_url = random.choice(IMAGE_URLS_SET4)
                line_bot_api.reply_message(
                    reply_token,
                    ImageSendMessage(
                        original_content_url=image_url,
                        preview_image_url=image_url
                    )
                )
            else:
                # 隨機選擇影片
                video_choice = random.choice(VIDEO_URLS_SET1)
                line_bot_api.reply_message(
                    reply_token,
                    VideoSendMessage(
                        original_content_url=video_choice['video'],
                        preview_image_url=video_choice['preview']
                    )
                )
        
        elif message_text.strip() == 'test':  #測試用
            video_choice = random.choice(VIDEO_URLS)  
            line_bot_api.reply_message(
                reply_token,
                VideoSendMessage(
                        original_content_url=video_choice['video'],
                        preview_image_url=video_choice['preview']
                    )
            )

        else:
            return
        
        return 'OK', 200
    
    except Exception as e:
        print(f'Exception: {e}')
        return 'Internal Server Error', 500
