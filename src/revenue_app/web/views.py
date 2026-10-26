from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_safe


@require_safe
def home(request: HttpRequest) -> HttpResponse:
    return render(request, "web/home.html")


@require_safe
def health(request: HttpRequest) -> JsonResponse:
    """Sonde de vie du processus ; ne prétend pas vérifier PostgreSQL."""
    return JsonResponse({"status": "ok"})
