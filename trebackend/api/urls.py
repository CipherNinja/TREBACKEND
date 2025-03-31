from core.views import course_api
from django.urls import path

urlpatterns = [
    path('v1/', course_api, name='course-api'),
]