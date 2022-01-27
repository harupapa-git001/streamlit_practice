import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 超入門")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
})

#ソート可能なテーブル(2種)

#枠の長さの指定不可(write)
st.write(df)

    #枠の長さの指定可能(dataframe)
    #st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)

#性的なテーブルを作りたい時
#st.table(df.style.highlight_max(axis=0))

"""
#   章
##  節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df2)

st.area_chart(df2)

st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df3)

st.write("Display Image")


img = Image.open("pokemon.jpg")
st.image(img, caption="Pokemon Image", use_column_width=True)

#チェックボックス
if st.checkbox("Show Image"):
    img = Image.open("pokemon.jpg")
    st.image(img, caption="pokemon Image", use_column_width=True)

#セレクトボックス
option = st.selectbox(
    "あなたが好きな数字は？",
    list(range(1, 11))
)

"あなたの好きな数字は", option, "ですね。"

st.write("インタラクティブなウィジェッツ")

option = st.sidebar.text_input("あなたの趣味を教えてください")
"あなたの趣味は:", option, "ですね。"

condition = st.sidebar.slider("あなたの今の調子は?", 0, 100, 50)
"あなたの調子は:", condition

left_colomn, right_column = st.columns(2)
button = left_colomn.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)


import time

for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!"

expander1 = st.beta_expander("問い合わせ")
expander1.write("問い合わせ1の回答")
expander2 = st.beta_expander("問い合わせ")
expander2.write("問い合わせ2の回答")
expander3 = st.beta_expander("問い合わせ")
expander3.write("問い合わせ３の回答")



