import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go

st.set_page_config(page_title="Bitcoin 예측 UI", layout="wide")

# -------------------------
# 제목 + 버튼
# -------------------------
col_title, col_button = st.columns([8, 2])  # 비율로 너비 조절
with col_title:
    st.title("🚀 Bitcoin 1시간 단위 가격 예측 UI")
with col_button:
    predict_btn = st.button("예측하기")

# -------------------------
# 사이드바 옵션
# -------------------------
st.sidebar.header("⚙️ 설정")

coins = ['KRW-BTC', 'KRW-ETH', 'KRW-DOGE', 'KRW-XRP']
selected_coin = st.sidebar.selectbox("코인 선택", coins)

period = 24
model = st.sidebar.selectbox("예측 모델 선택", ["LSTM", "GRU", "Prophet", "LightGBM"])

# -------------------------
# 더미 데이터 생성 (실제 환경에서는 S3 등에서 불러오기)
# -------------------------
now = datetime.now()
timestamps = [now - timedelta(hours=i) for i in range(period)][::-1]
prices = np.cumsum(np.random.randn(period)) + 73000000  # 랜덤 walk around 73M
volumes = np.random.randint(100, 1000, period)

df = pd.DataFrame({"timestamp": timestamps, "price": prices, "volume": volumes})

# 예측값 (더미: 마지막 값에서 + 랜덤)
pred_price = df["price"].iloc[-1] * (1 + np.random.uniform(-0.01, 0.01))
pred_change = (pred_price - df["price"].iloc[-1]) / df["price"].iloc[-1] * 100

# -------------------------
# 메트릭 카드 (단위 제거)
# -------------------------
col1, col2, col3 = st.columns(3)
col1.metric("현재 가격", f"{df['price'].iloc[-1]:,.0f}", f"{(df['price'].iloc[-1]-df['price'].iloc[-2])/df['price'].iloc[-2]*100:.2f}%")
col2.metric("24h 거래량", f"{df['volume'].sum():,.0f}")
col3.metric("1시간 뒤 예측", f"{pred_price:,.0f}", f"{pred_change:.2f}%")

# -------------------------
# Plotly 차트
# -------------------------
fig = go.Figure()

# 실제 가격 선 그래프
fig.add_trace(go.Scatter(
    x=df["timestamp"],
    y=df["price"],
    mode="lines",
    name="실제 가격",
    line=dict(color="blue")
))

# 예측값을 기존 마지막 점과 이어서 선으로 표시
fig.add_trace(go.Scatter(
    x=[df["timestamp"].iloc[-1], df["timestamp"].iloc[-1] + timedelta(hours=1)],
    y=[df["price"].iloc[-1], pred_price],
    mode="lines+markers+text",
    name="예측 가격",
    line=dict(color="red", dash="dash"),
    marker=dict(color="red", size=10),
    text=[None, f"{pred_price:,.0f}"],
    textposition="top center"
))

fig.update_layout(
    title=f"{selected_coin} 최근 {period}시간 가격 & 예측",
    xaxis_title="시간",
    yaxis_title="가격",
    template="plotly_white",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# 데이터 테이블
# -------------------------
st.subheader("📊 최근 데이터")

df_display = df.tail(24).copy()
df_display["timestamp"] = df_display["timestamp"].dt.strftime("%Y-%m-%d %H:%M")
df_display = df_display.set_index("timestamp")

# height 옵션 추가
st.dataframe(df_display, height=400, use_container_width=True)

# -------------------------
# 모델 성능 지표 (더미 값)
# -------------------------
st.subheader("📈 모델 성능 지표")
metrics_df = pd.DataFrame({
    "모델": [model],
    "RMSE": [np.random.uniform(20000, 60000)]
})

metrics_df_reset = metrics_df.reset_index(drop=True)

st.dataframe(metrics_df_reset, height=100, use_container_width=True)

print("Streamlit app is running.")