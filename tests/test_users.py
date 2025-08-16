import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_user_registration(client):
    """
    Test that a user can register and is created as inactive.
    """
    url = reverse('register')
    data = {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'testuser@example.com',
        'password': 'testpassword123',
        'password2': 'testpassword123',
        'terms': True,
        'privacy': True,
    }
    response = client.post(url, data)
    if response.status_code != 302:
        print(response.context['form'].errors)
    assert response.status_code == 302  # Should redirect on success
    assert response.url == reverse('login')
    
    # Check that the user was created and is inactive
    user = User.objects.get(email='testuser@example.com')
    assert user.first_name == 'Test'
    assert not user.is_active


@pytest.mark.django_db
def test_user_login(client, django_user_model):
    """
    Test that an active user can log in.
    """
    # Create an active user
    user = django_user_model.objects.create_user(
        username='activeuser@example.com',
        email='activeuser@example.com',
        password='testpassword123',
        first_name='Active',
        last_name='User',
        is_active=True
    )
    
    url = reverse('login')
    data = {
        'username': 'activeuser@example.com',
        'password': 'testpassword123',
    }
    response = client.post(url, data)
    assert response.status_code == 302  # Redirects on successful login
    # Check that the user is logged in by accessing a protected page
    profile_url = reverse('profile')
    response = client.get(profile_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_inactive_user_login(client, django_user_model):
    """
    Test that an inactive user cannot log in.
    """
    # Create an inactive user
    django_user_model.objects.create_user(
        username='inactiveuser@example.com',
        email='inactiveuser@example.com',
        password='testpassword123',
        first_name='Inactive',
        last_name='User',
        is_active=False
    )
    
    url = reverse('login')
    data = {
        'username': 'inactiveuser@example.com',
        'password': 'testpassword123',
    }
    response = client.post(url, data)
    assert response.status_code == 200  # Stays on the login page
    assert b'This account is inactive.' in response.content


@pytest.mark.django_db
def test_profile_access(client, django_user_model):
    """
    Test that only authenticated users can access the profile page.
    """
    profile_url = reverse('profile')
    
    # Test unauthenticated access
    response = client.get(profile_url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

    # Test authenticated access
    user = django_user_model.objects.create_user(
        username='test@example.com', email='test@example.com', password='password123', is_active=True
    )
    client.login(username='test@example.com', password='password123')
    response = client.get(profile_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_logout(client, django_user_model):
    """
    Test that a logged-in user can log out.
    """
    user = django_user_model.objects.create_user(
        username='testlogout@example.com', email='testlogout@example.com', password='password123', is_active=True
    )
    client.login(username='testlogout@example.com', password='password123')

    # Check we are logged in
    response = client.get(reverse('profile'))
    assert response.status_code == 200

    # Log out
    logout_url = reverse('logout')
    response = client.post(logout_url)
    assert response.status_code == 302 # Redirects after logout

    # Check we are logged out
    response = client.get(reverse('profile'))
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))
