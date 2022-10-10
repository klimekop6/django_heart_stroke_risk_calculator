import numpy as np
from pandas import DataFrame
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .apps import HomePageConfig


# Create your views here.
def index(request):
    return render(request, "home_page/index.html")


class predict_data(APIView):
    def post(self, request):

        if request.method == "POST":

            response: dict = request.POST.dict()

            response["age"] = np.log(int(response["age"]))
            response["trtbps"] = np.log(int(response["trtbps"]))
            response["chol"] = np.log(int(response["chol"]))
            response["thalachh"] = np.log(int(response["thalachh"]))

            del response["csrfmiddlewaretoken"]

            user_data = DataFrame.from_dict([response])

            # Use basic scaler and model
            if len(response) < 13:
                del user_data["oldpeak"]

                user_data = HomePageConfig.scaler_basic.transform(user_data)
                user_heart_risk = {
                    "heart_failure_risk": HomePageConfig.model_basic.predict(user_data)
                }

                return HttpResponse(*user_heart_risk.values())

            # Use fuly trained model and its data scaler
            user_data = HomePageConfig.scaler.transform(user_data)
            user_heart_risk = {
                "heart_failure_risk": HomePageConfig.model.predict(user_data)
            }

            return HttpResponse(*user_heart_risk.values())
