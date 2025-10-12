import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import time
import subprocess
import sys
import os

# =========================================================
# 1️⃣ MLflow 초기 설정
# =========================================================
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("Titanic_Classification")

client = MlflowClient()
experiment = client.get_experiment_by_name("Titanic_Classification")
print(f"✅ Experiment ID: {experiment.experiment_id}")

# =========================================================
# 2️⃣ 데이터 로드 & 전처리
# =========================================================
df = sns.load_dataset("titanic")
df = df[["survived", "pclass", "sex", "age", "sibsp", "parch", "fare", "embarked"]]
df = df.dropna()

# 범주형 -> 숫자형 변환
df["sex"] = df["sex"].map({"male": 0, "female": 1})
df["embarked"] = df["embarked"].map({"C": 0, "Q": 1, "S": 2})

X = df.drop("survived", axis=1)
y = df["survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# =========================================================
# 3️⃣ 모델 학습 + MLflow 기록
# =========================================================
with mlflow.start_run(run_name="titanic_rf_model") as run:
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=5,
        random_state=42
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    mlflow.log_param("n_estimators", 200)
    mlflow.log_param("max_depth", 5)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)

    mlflow.sklearn.log_model(model, "model")

    print(f"📈 Accuracy: {acc:.4f}, F1 Score: {f1:.4f}")
    print(f"🔗 Run ID: {run.info.run_id}")

    # =========================================================
    # 4️⃣ 모델 레지스트리에 등록 + alias 설정
    # =========================================================
    model_name = "Titanic_RF_Model"
    model_uri = f"runs:/{run.info.run_id}/model"

    model_version = mlflow.register_model(model_uri, model_name)
    time.sleep(2)

    client.set_registered_model_alias(model_name, "champion", model_version.version)

    print(f"✅ 모델 등록 완료: {model_name} (version: {model_version.version})")
    print(f"🏆 Alias 'champion'이 {model_name}의 version {model_version.version}에 설정되었습니다.")