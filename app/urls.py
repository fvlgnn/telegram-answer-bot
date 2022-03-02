from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from app.views import WebhookView

urlpatterns = [

    path('webhook', 
        csrf_exempt(WebhookView.as_view()),
        name="webhook")

]