from django.contrib import admin
from django.urls import path
from webapp.views import EmpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', EmpView.as_view()),

]
