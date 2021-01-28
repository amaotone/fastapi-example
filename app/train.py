import joblib
from palmerpenguins import load_penguins
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier


def train():
    data, target = load_penguins(return_X_y=True, drop_na=True)

    models = {
        "rf": RandomForestClassifier(max_depth=3, random_state=0),
        "dt": DecisionTreeClassifier(max_depth=3, random_state=0),
    }

    for name, model in models.items():
        model.fit(data, target)
        joblib.dump(model, f"model/{name}.pkl")
        print(f"save model: {name}")


if __name__ == "__main__":
    train()
