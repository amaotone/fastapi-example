import joblib
from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel, Field
from typing_extensions import Literal

from train import train

app = FastAPI()
models = {
    "randomforest": joblib.load("model/rf.pkl"),
    "decisiontree": joblib.load("model/dt.pkl"),
}


class PenguinItem(BaseModel):
    model: Literal["randomforest", "decisiontree"] = Field(
        "randomforest", example="randomforest"
    )
    bill_length: float = Field(..., example=39.1)
    bill_depth: float = Field(..., example=18.7)
    flipper_length: float = Field(..., example=181.0)
    body_mass: float = Field(
        ..., gt=1000, lt=10000, example=3750.0
    )


class PenguinPrediction(BaseModel):
    name: str
    probability: float


@app.post("/predict", response_model=PenguinPrediction)
async def predict_species(data: PenguinItem):
    x = [
        [
            data.bill_length,
            data.bill_depth,
            data.flipper_length,
            data.body_mass,
        ]
    ]
    return {
        "name": models[data.model].predict(x)[0],
        "probability": models[data.model]
        .predict_proba(x)
        .max(),
    }


@app.get("/train")
async def train_models(background_tasks: BackgroundTasks):
    background_tasks.add_task(train)
    return {"message": "start training"}
