from django.urls import path
from . import views
urlpatterns = [
    path('',views.nav),
    path('category/<str:category_title>/',views.note_by_category,name='category')
]
