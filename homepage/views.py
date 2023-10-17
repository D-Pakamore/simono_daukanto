from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        print(user.username)

        # Add custom data to the context
        context['nav_endpoints'] = [
            {
                'label': 'Mokytojai',
                'endpoint': ''
            }
        ]

        context['user'] = user
        return context   