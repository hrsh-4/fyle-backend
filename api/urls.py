from django.urls import path, include

from . import views

urlpatterns = [
	
	path("",views.index),
    path("api/branches", views.BranchSearchView.as_view()),
    path("api/branches/autocomplete", views.BranchAutoCompleteSearchView.as_view()),
    path("set-favourite/<pk>", views.set_favourite),

]
