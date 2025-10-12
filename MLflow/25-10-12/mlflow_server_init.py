import subprocess
import os
import time

# =========================================================
# 1️⃣ MLflow 서버 실행
# =========================================================
mlflow_server = subprocess.Popen(
    [
        "mlflow",
        "server",
        "--host", "127.0.0.1",
        "--port", "5000",
        "--backend-store-uri", "./mlruns"
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("🚀 MLflow Tracking Server 실행 중... (http://127.0.0.1:5000)")
time.sleep(5)  # 서버가 완전히 켜질 때까지 대기

# =========================================================
# 2️⃣ Tracking URI 설정
# =========================================================
os.environ["MLFLOW_TRACKING_URI"] = "http://127.0.0.1:5000"
print(f"✅ Tracking URI 설정 완료: {os.environ['MLFLOW_TRACKING_URI']}")

# =========================================================
# 3️⃣ 모델 서빙 실행
# =========================================================
print("🚀 모델 서빙 시작 (http://127.0.0.1:5001)")
subprocess.run([
    "mlflow",
    "models",
    "serve",
    "-m", "models:/Titanic_RF_Model@champion",
    "-p", "5001",
    "--no-conda"
])