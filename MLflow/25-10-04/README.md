# ML FLOW

## 🤔 ML Flow란?

> **MLflow는 머신러닝(ML) 실험을 관리하고, 모델을 추적·배포할 수 있게 해주는 오픈소스 플랫폼**
> 
> 
> 입니다. 머신러닝 프로젝트를 진행할 때 "실험 관리 + 모델 저장 + 배포"를 한 번에 지원하는 도구라고 보면 됩니다.
> 
![title](https://private-user-images.githubusercontent.com/127470862/497431413-55bc28bf-f2a0-4cc0-b84e-3de7d4d2780d.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTk1NzQxMjEsIm5iZiI6MTc1OTU3MzgyMSwicGF0aCI6Ii8xMjc0NzA4NjIvNDk3NDMxNDEzLTU1YmMyOGJmLWYyYTAtNGNjMC1iODRlLTNkZTdkNGQyNzgwZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMDA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTAwNFQxMDMwMjFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kMGU3MWJjMjAxMTQ1YmI1MjMxYzQ3MDlkOTA1YzM0ZTQ1MmRkM2U5ODNjYmU1YTVkMzc0ZmU3YWU5ZTU4MmU5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.tDMP_vrJsWNXrq7Zo6zZ5mMSW_hAW8FHSPHKclVWGU0)   



MLflow의 워크플로우는 위 그림과 같습니다.

먼저 Tracking Server에서 시작되며, 여기서 실험의 Parameters, Metrics, Artifacts, Metadata, 그리고 Models를 기록하고 관리합니다. 이렇게 추적된 모델과 관련 정보는 Model Registry로 전달되며, Model Registry는 개발자들끼리 협업할 수 있는 중앙 저장소 역할을 합니다. 모델은 Staging 단계에서 검증을 거친 후, Production 단계로 승격되어 실제 서비스에 활용되며 필요 시 Archived 상태로 보관됩니다. 이 과정에서 Reviewer와 CI/CD Tools가 개입하여 품질 보증과 자동화된 배포 파이프라인을 지원합니다. 최종적으로 Production 단계의 모델은 Downstream 애플리케이션, Automated Jobs, REST Serving을 통해 다양한 환경에서 활용되며, 안정적이고 일관된 모델 배포가 가능해진다.

## 🔊 ML Flow가 있어야하는 이유

### 1️⃣ 머신러닝 실험은 **재현(reproducibility)** 이 어려움

- 문제: 같은 코드라도 환경/버전이 조금만 달라지면 결과가 달라짐
- MLflow 역할:
    - 코드, 데이터 경로, 파라미터, 메트릭을 자동으로 기록
    - 동일한 실험을 다시 실행하거나, 다른 사람도 똑같이 재현 가능

### 2️⃣ **실험 추적과 비교**가 힘듦

- 문제: “learning_rate=0.01일 때 정확도가 몇 %였더라?” 매번 기억하거나 엑셀로 관리해야 함
- MLflow 역할:
    - 모든 실험을 UI 대시보드에서 확인 가능
    - 파라미터, 메트릭, 그래프를 손쉽게 비교 → **최적 모델 선택** 가능

### 3️⃣ **모델 버전 관리** 필요

- 문제: 모델이 계속 업데이트되는데, **어느 버전이 현재 서비스 중인지** 관리가 어려움
- MLflow 역할:
    - Model Registry를 통해 **Staging → Production → Archived** 단계 관리
    - 모델에 버전 태깅(예: v1, v2) 가능

### 4️⃣ **배포(Serving)** 자동화가 필요

- 문제: 모델을 저장했지만 운영 환경(API, 배치 작업)에 올리는 게 번거롭고 실수 잦음
- MLflow 역할:
    - REST API Serving 지원
    - CI/CD 파이프라인과 쉽게 연결 → **모델을 바로 서비스에 적용 가능**

### 5️⃣ **팀 협업**에서 필수

- 문제: 연구자와 엔지니어가 다른 툴을 쓰면, 모델/코드 공유가 번거롭고 불일치 발생
- MLflow 역할:
    - Data Scientist는 Tracking에 기록
    - Deployment Engineer는 Registry에서 모델 가져와 배포
    - 같은 플랫폼에서 협업 가능

## ⌨️ ML Flow 기능

### 1️⃣ **Tracking Server (왼쪽 박스)**

- ML 실험 결과를 기록하고 관리하는 공간
- 주요 기능:
    - **Parameters**: 학습에 사용한 하이퍼파라미터 (예: learning_rate, batch_size)
    - **Metrics**: 성능 지표 (예: accuracy, loss, RMSE)
    - **Artifacts**: 학습 과정에서 생성된 산출물 (예: 모델 가중치 파일, 시각화 그래프)
    - **Metadata & Models**: 모델 자체 및 부가 정보

➡️ 즉, 개발자가 실험을 할 때 남기는 “연구 노트 + 로그 저장소” 역할을 합니다.

### 2️⃣ **Model Registry (가운데 박스)**

- Tracking Server에서 기록된 모델을 **체계적으로 관리하는 저장소**
- 모델의 **버전 관리 + 상태 관리**가 핵심
- 상태 단계:
    - **Staging**: 테스트 단계 (아직 운영에 반영하지 않음)
    - **Production**: 운영 환경에서 실제 사용되는 모델
    - **Archived**: 더 이상 쓰지 않는 모델, 보관용

➡️ 여기서 **Data Scientists**는 모델을 올리고, **Deployment Engineers**는 운영 환경으로 배포/관리합니다.

### 3️⃣ **Downstream 활용 (오른쪽 박스)**

등록된 모델은 여러 방식으로 활용될 수 있어요:

- **Downstream**: 다른 애플리케이션에서 모델을 불러다 쓰는 경우
- **Automated Jobs**: 스케줄링된 자동 작업 (예: 매일 새 데이터로 예측 실행)
- **REST Serving**: API 형태로 배포하여, 외부에서 HTTP 요청을 보내 모델 예측을 받음

➡️ 즉, **모델을 실제 서비스에 연결**하는 부분입니다.

### 4️⃣ **CI/CD + Reviewer (아래 박스)**

- 모델이 **Staging → Production**으로 넘어가기 전에 리뷰 및 승인 절차를 거칠 수 있음
- CI/CD 툴(Jenkins, GitHub Actions, GitLab CI 등)과 연동 가능
- 모델 배포도 **자동화 파이프라인**에 통합할 수 있음

## 🏋️ ML Flow 사용 예시

### 라이브러리 불러오기

```python
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
```

### 데이터 로드 및 분할

```python
data = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(
data.data, data.target, test_size=0.2, random_state=42
)
```

### MLflow 실험 이름 설정

```python
mlflow.set_experiment("RandomForest Experiment")
```

### 하이퍼파라미터 탐색 설정

```python
n_estimators_list = [10, 50, 100, 200]
max_depth_list = [3, 5, 10, None]
```

### 반복 학습 및 평가

```python
for n_estimators in n_estimators_list:
for max_depth in max_depth_list:
with mlflow.start_run():
# 모델 학습
model = RandomForestRegressor(
n_estimators=n_estimators, max_depth=max_depth, random_state=42
)
model.fit(X_train, y_train)
```

### 예측 및 성능 평가

```python
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

### MLflow 로그 기록

```python
mlflow.log_param("n_estimators", n_estimators)
mlflow.log_param("max_depth", max_depth)
mlflow.log_metric("mse", mse)
mlflow.log_metric("r2_score", r2)
mlflow.sklearn.log_model(model, "random_forest_model")
```

### 시각화 및 아티팩트 저장

```python
plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred, alpha=0.6, color="blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title(f"Prediction Scatter Plot (n={n_estimators}, depth={max_depth})")
plt.savefig("scatter_plot.png")
plt.close()
mlflow.log_artifact("scatter_plot.png")
```

### 로그 출력

```python
print(f"Logged: n_estimators={n_estimators}, max_depth={max_depth}, MSE={mse:.4f}, R2={r2:.4f}")
```

### 모델 레지스트리에 등록

```python
import mlflow
import mlflow.sklearn
from mlflow import MlflowClient
from sklearn.metrics import mean_squared_error
import numpy as np

mlflow.sklearn.log_model(
    sk_model=model,
    artifact_path="random_forest_model",
    registered_model_name="RandomForestRegressor"
)

client = MlflowClient()
experiment = client.get_experiment_by_name("RandomForest test")
experiment_id = experiment.experiment_id

runs = client.search_runs(
    experiment_ids=[experiment_id],
    order_by=["metrics.rmse ASC"],
    max_results=1
)

best_run = runs[0]
best_run_id = best_run.info.run_id
print("Best run_id:", best_run_id)
print("Best RMSE:", best_run.data.metrics["mse"])

model_name = "RandomForestRegressor"
model_uri = f"runs:/{best_run_id}/random_forest_model"

mv = mlflow.register_model(model_uri=model_uri, name=model_name)
print(f"Registered model version: {mv.version}")

client.set_registered_model_alias(model_name, "champion", mv.version)
print(f"✅ Champion model updated to version {mv.version}")
```

### MLflow 서버에서 테스트하기

**Best RUN**

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()
experiment = client.get_experiment_by_name("RandomForest test")
runs = client.search_runs(experiment.experiment_id, order_by=["metrics.r2_score DESC"], max_results=1)

best_run = runs[0]
print("Best Run ID:", best_run.info.run_id)
print("Best Params:", best_run.data.params)
print("Best Metrics:", best_run.data.metrics)
```

**모델 로드 및 재사용**

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()
experiment = client.get_experiment_by_name("RandomForest test")
runs = client.search_runs(experiment.experiment_id, order_by=["metrics.r2_score DESC"], max_results=1)

best_run = runs[0]
print("Best Run ID:", best_run.info.run_id)
print("Best Params:", best_run.data.params)
print("Best Metrics:", best_run.data.metrics)
```