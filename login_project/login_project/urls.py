"""login_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('accounts/', include('accounts.urls')),  # 追加　
    path('accounts/', include('django.contrib.auth.urls')),  # 認証ビューが使用可能

]
"""
   django.contrib.auth.urlsをインポートするだけで、
   templates/registration/以下に配置されたlogin.htmlおよびlogged_out.htmlという名前のテンプレートが、
   それぞれ上記URLにおいて自動的に表示される。
   myapp/urls.pyで、loginおよびlogoutに関するビューを記述する必要がなくなる
"""