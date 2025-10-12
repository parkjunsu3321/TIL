import requests
import json

# REST API 엔드포인트
url = "http://127.0.0.1:5001/invocations"

# HTTP 헤더 설정
headers = {"Content-Type": "application/json"}

# ✅ sklearn 모델에 완벽히 맞는 입력 형식
data = {
    "dataframe_split": {
        "columns": ["pclass", "sex", "age", "sibsp", "parch", "fare", "embarked"],
        "data": [
            [3, 1, 22.0, 1, 0, 7.25, 2],
            [1, 0, 38.0, 1, 0, 71.2833, 0]
        ]
    }
}

# POST 요청 전송
response = requests.post(url, headers=headers, data=json.dumps(data))

# 결과 출력
print("✅ Status Code:", response.status_code)
print("📊 Prediction:", response.json())