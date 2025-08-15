from django.shortcuts import render
from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = "landing.html"

class ImpressumView(TemplateView):
    template_name = "legal/impressum.html"

class PrivacyPolicyView(TemplateView):
    template_name = "legal/privacy.html"

class TermsView(TemplateView):
    template_name = "legal/terms.html"

class PlaceholderView(TemplateView):
    template_name = "placeholder.html"
