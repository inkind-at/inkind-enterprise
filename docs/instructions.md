# Implementation Instructions — Public Landing Page (1.5) & Legal Pages (9)

## 1. Technical Context
- Consider existing folder structure in the repo
- **Backend:** Python/Django (REST API)
- **Frontend:** Bootstrap 5 (mobile-first), custom.css, favicon (already provided)
- **Database:** PostgreSQL in local development, AWS RDS in production
- **Internationalization:** English (default) & German
- **Branding:** Primary color Burgundy (#7A003D)
- **Responsiveness:** Mobile-first approach

---

## 2. Public Landing Page (NFR 1.5)

### 2.1 File Structure
- **Template:** `templates/landing.html`
- **CSS:** Extend `custom.css` (already available)
- **View:** `views.py` → `LandingPageView`
- **URL:** `/` (root URL)

### 2.2 Content Requirements
- Communicate platform's mission & value proposition (English/German)
- Two primary CTAs:
  - **For Social Enterprises:** "Register Your Enterprise" / "Learn More"
  - **For Donors:** "View Needs" / "How to Donate"
- Add **Painted Door Testing:** when clicking the buttons, "painted door" stubs shall be used. These stubs will lead to a placeholder page.
- Branding compliance:
  - Use Burgundy (#7A003D) for primary buttons and highlights
  - Display logo in header
  - Include provided favicon in `<head>`

### 2.3 Usability & Accessibility (NFR 1.1–1.3)
- **Responsive design** via Bootstrap grid
- **Touch-friendly elements:** Buttons & links ≥ 48x48px
- **ARIA labels** for all interactive elements
- **WCAG 2.1 AA** contrast compliance
- All images must have `alt` text

### 2.4 Internationalization
- Use Django `i18n` tags in templates
- Translations:
  - English strings in `locale/en/LC_MESSAGES/django.po`
  - German strings in `locale/de/LC_MESSAGES/django.po`
- Include language switcher in navbar

---

## 3. Legal Pages (NFR 9.1 – 9.3)

### 3.1 Pages to Create
- **Impressum** (`/impressum`) – NFR 9.1
- **Privacy Policy** (`/privacy`) – NFR 9.2
- **Terms & Conditions** (`/terms`) – NFR 9.3

### 3.2 Implementation Details
- Templates:
  - `templates/legal/impressum.html`
  - `templates/legal/privacy.html`
  - `templates/legal/terms.html`
- Views:
  - `ImpressumView`
  - `PrivacyPolicyView`
  - `TermsView`
- Static text content for both English & German via Django i18n
- Footer links to each page on **every template** (including landing page)

### 3.3 Registration Integration
- Modify registration form:
  - Checkbox for "I agree to the Terms & Conditions" (link to `/terms`)
  - Checkbox for "I have read the Privacy Policy" (link to `/privacy`)

---

## 4. Footer Structure
- Place footer in `templates/partials/footer.html`
- Include:
  - Links: Impressum, Privacy Policy, Terms
  - Language switcher
  - All links available in both languages

---

## 5. Internationalization Setup
- Enable `LocaleMiddleware` in `settings.py`
- Add `LANGUAGES = [('en', 'English'), ('de', 'Deutsch')]`
- Generate and compile message files:
  ```bash
  django-admin makemessages -l en
  django-admin makemessages -l de
  django-admin compilemessages


##  6. Example URL Config (urls.py)
```python
from django.urls import path
from .views import LandingPageView, ImpressumView, PrivacyPolicyView, TermsView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('impressum/', ImpressumView.as_view(), name='impressum'),
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),
    path('terms/', TermsView.as_view(), name='terms'),
]
```

## 7. Styling Guidelines

* Use `custom.css` for: 
    * Overriding Bootstrap defaults with Burgundy primary color
    * Adjusting typography for readability
* Ensure favicon is linked in base.html:
<link rel="icon" href="{% static 'images/favicon.ico' %}">

## 8. Acceptance Criteria

* Landing page visible without authentication
* Two primary CTAs per NFR 1.5.3
* All legal pages accessible from footer in all templates
* Responsive & mobile-first
* Accessible (ARIA, contrast, alt-text)
* English/German switch works correctly
* Branding & favicon applied