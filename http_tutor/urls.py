from django.urls import path, register_converter

from . import views, converts

app_name = 'http_tutor'

register_converter(converts.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/2003/', views.special_case_2003),
    path('articles/<yyyy:year>/', views.year_convert_archive),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]