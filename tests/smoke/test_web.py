from django.test import Client


def test_home_renders_template(client: Client) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Simulations de revenus" in response.content.decode()
    assert any(template.name == "web/home.html" for template in response.templates)
    assert "/static/web/app.css" in response.content.decode()


def test_health_is_a_liveness_probe(client: Client) -> None:
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_unknown_route_returns_404(client: Client) -> None:
    assert client.get("/missing/").status_code == 404


def test_routes_reject_writes(client: Client) -> None:
    assert client.post("/").status_code == 405
    assert client.post("/health/").status_code == 405
