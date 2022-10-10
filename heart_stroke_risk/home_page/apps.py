import pickle
from pathlib import Path
from django.apps import AppConfig
from xgboost import XGBClassifier
from sklearn.preprocessing import MinMaxScaler


class HomePageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home_page"

    MODEL_PATH = Path("home_page/model/")

    # Full version with all params
    scaler: MinMaxScaler = pickle.load(open(f"{MODEL_PATH}/data_scaler", "rb"))
    model: XGBClassifier = pickle.load(open(f"{MODEL_PATH}/model_xgb_HSR", "rb"))

    # Basic version with fewer params
    scaler_basic: MinMaxScaler = pickle.load(
        open(f"{MODEL_PATH}/data_scaler_basic", "rb")
    )
    model_basic: XGBClassifier = pickle.load(
        open(f"{MODEL_PATH}/model_xgb_HSR_basic", "rb")
    )
