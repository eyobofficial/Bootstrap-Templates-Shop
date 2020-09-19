from django.urls import path

from .views import IndexView, ThemeListView


app_name = 'themes'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path(
        'category/<slug:slug>/',
        ThemeListView.as_view(),
        name='theme-list'
    )
]

