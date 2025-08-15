import pytest
from django.urls import reverse
from django.utils import translation

@pytest.mark.django_db
def test_landing_page(client):
    with translation.override("en"):
        url = reverse('landing')
        response = client.get(url)
    assert response.status_code == 200
    assert "in-kind enterprise" in str(response.content)

@pytest.mark.django_db
def test_impressum_page(client):
    with translation.override("en"):
        url = reverse('impressum')
        response = client.get(url)
    assert response.status_code == 200
    assert "Impressum" in str(response.content)

@pytest.mark.django_db
def test_privacy_page(client):
    with translation.override("en"):
        url = reverse('privacy')
        response = client.get(url)
    assert response.status_code == 200
    assert "Privacy Policy" in str(response.content)

@pytest.mark.django_db
def test_terms_page(client):
    with translation.override("en"):
        url = reverse('terms')
        response = client.get(url)
    assert response.status_code == 200
    assert "Terms & Conditions" in str(response.content)

@pytest.mark.django_db
def test_placeholder_page(client):
    with translation.override("en"):
        url = reverse('placeholder')
        response = client.get(url)
    assert response.status_code == 200
    assert "Feature Coming Soon" in str(response.content)
