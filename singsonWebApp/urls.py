from django.urls import path
from . import views


app_name = 'singsonWebApp'
#paths arranged alphabetically by name
urlpatterns = [
    # path('api/data', views.get_data, name='api-data'),

    #TEST URL
    path('', views.indexView.as_view(), name="index_view"),
]
