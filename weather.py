import requests
import streamlit as st
import datetime

# APIキー（取得はpenWeatherMapから）
API_KEY = "自身のAPIキーを入力"
# OpenWeatherMapのURL
URL = "https://api.openweathermap.org/data/2.5/"
# 地域の指定
place = "Sapporo"
# 天気情報の取得
data = requests.get(URL + "forecast?lang=ja&units=metric&q=" + place + "&appid=" + API_KEY).json()

# タイトル
st.title("札幌市の４日間天気")

# 日付ごとのセレクトボタンを作成
# 今日
today = datetime.datetime.today()
today_txt = str(today.month) + "月" + str(today.day) + "日（今日）"
# 明日
tomorrow = today + datetime.timedelta(days=1)
tomorrow_txt = str(tomorrow.month) + "月" + str(tomorrow.day) + "日（明日）"
# 2日後
twodays = today + datetime.timedelta(days=2)
twodays_txt = str(twodays.month) + "月" + str(twodays.day) + "日（明後日）"
# 3日後
threedays = today + datetime.timedelta(days=3)
threedays_txt = str(threedays.month) + "月" + str(threedays.day) + "日（明々後日）"

# 日付を選ぶセレクトボタン
day = st.selectbox("日付を選んでください",[today_txt,tomorrow_txt,twodays_txt,threedays_txt])

# 選択された日付の天気を表示
def showWeather(start,end):
    for i in range(start,end):
        # 天気の画像を表示するidを取得
        icon_id = data['list'][i]['weather'][0]['icon']
        # 時刻のテキストを取得
        time_txt = data['list'][i]['dt_txt']
        # 日時
        st.write(time_txt[0:4] + "年"+ time_txt[6]+ "月"+ time_txt[8:10]+ "日"+ time_txt[11:13] +"時の天気 : " + data['list'][i]['weather'][0]['description'])
        # 天気の画像
        st.image("https://openweathermap.org/img/wn/" + icon_id + "@2x.png")
        # 雲の割合
        st.write("雲の割合：" + str(data['list'][i]['clouds']['all']) + "%")
        # 気温
        st.write("気温："+ str(data['list'][i]['main']['temp']) + "度")
        # 湿度
        st.write("湿度：" + str(data['list'][i]['main']['humidity']) + "%")
        # 風速
        st.write("風速：" + str(data['list'][i]['wind']['speed']) + "メートル/秒")
        st.write("-"*25)

# 現在時刻を取得し、天気を表示する範囲を指定する
def timeCatch():
    # 現在時刻の取得
    now = datetime.datetime.now()
    flag = now.hour

    if  0 <= flag < 3:
        return 2,10,18,26,34
    elif 3 <= flag < 6:
        return 1,9,17,25,33
    elif 6 <= flag < 9:
        return 0,8,16,24,32
    elif 9 <= flag < 12:
        return 0,7,15,23,31
    elif 12 <= flag < 15:
        return 0,6,14,22,30
    elif 15 <= flag < 18:
        return 0,5,13,21,29
    elif 18 <= flag < 21:
        return 0,4,12,20,28
    elif 18 <= flag < 24:
        return 0,3,11,19,27

# 現在時刻を基に表示する時刻の範囲指定に使う値を取得
a,b,c,d,e = timeCatch()

# 今日の天気を表示
if day == today_txt:
    showWeather(a,b)
# 明日の天気を表示
elif  day == tomorrow_txt:
        showWeather(b,c)
# 2日後の天気を表示
elif day == twodays_txt:
    showWeather(c,d)
# 3日後の天気を表示
elif day == threedays_txt:
    showWeather(d,e)



