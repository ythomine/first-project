from django.urls import include, path

urlpatterns = [path("", include("revenue_app.web.urls"))]
