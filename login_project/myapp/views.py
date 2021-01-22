from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    return HttpResponse("Hello, world. Yo\lu're at the polls index")


class LoginRequiredViewSample(LoginRequiredMixin, TemplateView):
    template_name = 'myapp/login_required_view.html'
    # login_url = '/login/' # 削除したコード

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "はじめまして"

        # ログインユーザ取得
        user = self.request.user

        return context
