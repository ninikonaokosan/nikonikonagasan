import streamlit as st

checked_items=[]
total_score=0

todo_items={
    "洗濯":2,
    "ゴミ捨て":1,
    "料理":3,
    "買い物":2,
    "食器洗い":2,
    "自治会の仕事":5,
    "シャンプーなどの詰め替え":1,
    "お風呂掃除":3,
    "トイレ掃除":5,
    "部屋掃除":4,
    "断捨離":5,
    "整理整頓":5,
    "イベント企画":4,
    "金融関係":5,
    "カーテン雨戸の開け閉め換気":1,
    "タオルシーツ類交換":3,
    "布団メンテナンス":3,
    "車メンテナンス":4,
    "庭メンテナンス":4,
    "季節物メンテナンス":4
}
st.title("家事の勇者よ、よくぞきてくれた。さて、今日のクエスト達成具合はいかがかな？")
st.write("チェックボックスに軌跡を残そう！")

checked_items=[]
total_score=0

for item, score in todo_items.items():
    if st.checkbox(item):
        checked_items.append(item)
        total_score += score
if checked_items:
  st.write("達成したクエスト:")
  for item in checked_items:
    st.write(f"- {item}")
  st.write(f"達成度:{total_score}")
else:
  st.write("達成したクエストはありません")

if total_score>0:
  if total_score<=20:
    st.write("今の家事勇者レベルは20じゃ。まだまだ修行が必要じゃな。")
  elif total_score<=40:
    st.write("今の家事勇者レベルは50じゃ。だいぶ腕を上げてきたようじゃな。")
  else:
    st.write("今の家事勇者レベルは100じゃ。すごいぞい！")


if st.button("家事モンスター討伐完了！"):
  st.write("こうして、今日も家の平和は守られた。お疲れ様でした！")