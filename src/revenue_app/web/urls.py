from django.urls import path

from revenue_app.web import views

app_name = "web"
urlpatterns = [path("", views.home, name="home"), path("health/", views.health, name="health")]
