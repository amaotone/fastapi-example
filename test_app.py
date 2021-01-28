from fastapi.testclient import TestClient
from palmerpenguins import load_penguins

from app import app

client = TestClient(app)
models = ["randomforest", "decisiontree"]
example_body = {
    "model": "randomforest",
    "bill_length": 40,
    "bill_depth": 20,
    "flipoper_length": 200,
    "body_mass": 4000,
}


def test_predict():
    """テスト用データセットはどれを投げても結果が返ってくる"""
    data, _ = load_penguins(return_X_y=True, drop_na=True)
    for row in data.values:
        for model in models:
            body = {
                "model": model,
                "bill_length": row[0],
                "bill_depth": row[1],
                "flipper_length": row[2],
                "body_mass": row[3],
            }
            response = client.post("/predict", json=body)
            assert response.status_code == 200


def test_invalid_model_name():
    """存在しないモデルは指定できない"""
    body = example_body.update({"model": "invalidmodel"})
    response = client.post("/predict", json=body)
    assert response.status_code == 422


def test_invalid_endpoint():
    """変なエンドポイントは404が返る"""
    response = client.get("/invalid")
    assert response.status_code == 404
