# 制作したアプリ：天気予報アプリ  

# 制作に至った理由
現在、Pythonの学習に力を入れており、その学習成果を形にしたいと思ったのが理由です。  
自分の力でも実装できるレベルのアプリが何かあるかを探していた際に、  
比較的簡単に操作可能なAPIの利用を考えました。  

# 機能の説明
・Streamlitのコマンドで起動ができます。（streamlit run weather.py）  
・起動に成功すると本日の天気が表示されます。  

## １．天気予報の表示について
・天気は3時間ごとの情報が表示されます。  
・表示される情報は、天気、雲の割合、気温、湿度、風速です。  

## ２．日付の切り替え
・タイトル下部にあるセレクトボックスをクリックすると、本日から3日後までの日付を選択できます。  
・選択すると該当する日付の天気予報が表示されます。  


# 使用技術
・Python(バージョン3.12)  
・UIにPythonライブラリのStreamlitを使用  
・API(OpenWeatherMapを使用)

