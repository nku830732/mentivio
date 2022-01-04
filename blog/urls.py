from . import views
from django.urls import path
urlpatterns = [
    path('opportunities', views.opportunities, name="opportunities"),
    path('opportunities/comment/<str:slug>', views.opportunitiesComment,name="opportunitiesComment"),
    path('opportunities/<str:slug>', views.opportunitiesPost,name="opportunitiesPosts"),
    path('strategies', views.strategies, name="strategies"),
    path('strategies/<str:slug>', views.strategiesPost,name="strategiesPost"),
    path('strategies/comment/<str:slug>', views.strategiesPostComment,name="strategiesPostComment"),
]