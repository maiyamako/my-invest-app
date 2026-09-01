import streamlit as st

st.set_page_config(page_title="投資ダッシュボード", layout="centered")

st.markdown(
    "<h1 style='text-align:center; font-size:40px;'>📊 投資ダッシュボード（複数銘柄）</h1>",
    unsafe_allow_html=True
)

st.write("### 銘柄を追加していくと、下に一覧が自動で増えるよ")

# ---- 銘柄入力フォーム ----
with st.form("add_stock"):
    name = st.text_input("銘柄名（例：S&P500、楽天VTI、トヨタなど）")
    initial = st.number_input("元本（投資額）", min_value=0.0, step=1000.0)
    current = st.number_input("現在の評価額", min_value=0.0, step=1000.0)
    submitted = st.form_submit_button("追加する")

# ---- セッションに保存（アプリを閉じるまで記憶） ----
if "stocks" not in st.session_state:
    st.session_state["stocks"] = []

if submitted and name:
    st.session_state["stocks"].append({
        "name": name,
        "initial": initial,
        "current": current
    })

# ---- 銘柄一覧表示 ----
st.write("## 📈 銘柄一覧")

if len(st.session_state["stocks"]) == 0:
    st.info("まだ銘柄がありません。上のフォームから追加してね。")
else:
    for stock in st.session_state["stocks"]:
        profit = stock["current"] - stock["initial"]
        rate = (profit / stock["initial"] * 100) if stock["initial"] > 0 else 0
        color = "green" if profit >= 0 else "red"

        st.markdown(
            f"""
            <div style="
                border:1px solid #ddd;
                padding:20px;
                border-radius:10px;
                margin-bottom:15px;
                background-color:#f9f9f9;
            ">
                <h2 style="margin:0; font-size:28px;">{stock['name']}</h2>
                <p style="font-size:20px;">元本：{stock['initial']:,.0f} 円</p>
                <p style="font-size:20px;">評価額：{stock['current']:,.0f} 円</p>
                <h1 style="font-size:40px; color:{color}; margin:10px 0;">
                    {profit:,.0f} 円
                </h1>
                <h2 style="font-size:30px; color:{color}; margin:0;">
                    {rate:.2f} %
                </h2>
            </div>
            """,
            unsafe_allow_html=True
        )
