# line-bot--Auto-reply-messages-for-google-cloud
use google cloud run function

參考此篇教學製作https://github.com/yaoandy107/line-bot-tutorial

https://manager.line.biz/account/@412brmmv/setting 這個是line official account manager的後台控制

https://developers.line.biz/console/provider/2003743993 這個是line Developers 程式內的Channel secret token和Channel access token必須從這裡取得並且要使用WebHook連結

main.py 是主要程式，內容主要是讓使用者輸入關鍵字後linebot會隨機抽取一張相片
