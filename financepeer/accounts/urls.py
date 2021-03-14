
from django.urls import path
from accounts.views import index, detail, signup, model_form_upload

urlpatterns = [
    path('', index, name="index"),
    path('detail/', detail, name="detail"),
    path('signup/', signup, name="signup"),
    path('upload/', model_form_upload, name="upload")
]