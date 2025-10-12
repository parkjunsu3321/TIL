# 🚢 Titanic Survival Classification with MLflow

이 프로젝트는 **Titanic 생존자 예측 모델**을 구축하고, **MLflow를 사용해 실험 추적(Experiment Tracking)**, **모델 등록(Model Registry)**, **모델 서빙(Model Serving)** 과정을 자동화한 예제입니다.  

---

## 🧠 프로젝트 개요

Titanic 데이터셋을 기반으로 한 **RandomForestClassifier** 모델을 학습시켜 승객의 생존 여부를 예측합니다.  
MLflow를 통해 다음을 수행합니다:

- 실험(Experiment) 관리 및 자동 로깅  
- 모델 등록 및 버전 관리  
- Champion 모델 Alias 설정  
- 모델 서빙 및 REST API 호출 예시

---

## 🗂️ 프로젝트 구조

```
📦 Titanic_MLflow_Project
├── training_model.py      # MLflow 서버 및 모델 서빙 자동 실행 스크립트
├── mlflow_server_init.py  # REST API를 통해 모델 예측 테스트
├── model_client.py        # (선택) 사용자 정의 클라이언트 예제
├── requirements.txt       # 필요 패키지 목록
└── README.md              # 프로젝트 설명 문서
```

---

## ⚙️ 1. 환경 설정

### ✅ 필수 패키지 설치

```bash
pip install mlflow seaborn scikit-learn pandas requests
```

### ✅ MLflow 서버 설정

MLflow는 로컬에서 실행됩니다.

```bash
mlflow server --host 127.0.0.1 --port 5000 --backend-store-uri ./mlruns
```

또는 자동 실행 스크립트를 사용할 수 있습니다:

```bash
python training_model.py
```

> 💡 서버는 기본적으로 `http://127.0.0.1:5000` 에서 실행됩니다.

---

## 🧩 2. 모델 학습 및 등록

Titanic 데이터를 기반으로 모델을 학습하고 MLflow에 기록합니다.

```bash
python main.py
```

**주요 기능:**
- 실험 이름: `Titanic_Classification`
- 모델 이름: `Titanic_RF_Model`
- 등록 후 alias: `champion`

출력 예시:
```
✅ Experiment ID: 1
📈 Accuracy: 0.8265, F1 Score: 0.7821
🔗 Run ID: 123abc456def
✅ 모델 등록 완료: Titanic_RF_Model (version: 1)
🏆 Alias 'champion'이 Titanic_RF_Model의 version 1에 설정되었습니다.
```

---

## 🚀 3. 모델 서빙 (Serving)

MLflow Model Registry에 등록된 `champion` 버전의 모델을 API 형태로 제공합니다.

```bash
mlflow models serve -m "models:/Titanic_RF_Model@champion" -p 5001 --no-conda
```

또는 자동 실행 스크립트를 사용하세요:

```bash
python training_model.py
```

> ✅ 모델 서버는 기본적으로 `http://127.0.0.1:5001` 에서 실행됩니다.

---

## 📡 4. REST API 예측 테스트

모델 서빙이 시작된 후, 다음 스크립트로 예측 요청을 보낼 수 있습니다:

```bash
python mlflow_server_init.py
```

예시 응답:
```
✅ Status Code: 200
📊 Prediction: [0, 1]
```

요청 예시 (JSON):
```json
{
  "dataframe_split": {
    "columns": ["pclass", "sex", "age", "sibsp", "parch", "fare", "embarked"],
    "data": [
      [3, 1, 22.0, 1, 0, 7.25, 2],
      [1, 0, 38.0, 1, 0, 71.2833, 0]
    ]
  }
}
```

---

## 📈 5. MLflow UI에서 실험 확인

웹 브라우저에서 MLflow UI를 열어 결과를 시각적으로 확인할 수 있습니다.

🔗 [http://127.0.0.1:5000](http://127.0.0.1:5000)

UI에서 다음을 확인할 수 있습니다:
- 각 실험(run)의 파라미터 및 메트릭
- 모델 버전 및 alias 상태
- 자동으로 저장된 모델 artifact

---


## 🧾 6. 라이선스

이 프로젝트는 MIT License를 따릅니다.  
자유롭게 수정 및 재배포 가능합니다.
