"""JobProcess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from .views import MainView, UpdateWorkView, CreateWorkView,delete_work, DetailIssueView, CreateIssueView,UpdateIssueView, SearchView, SearchNoConView

search_patterns = [
    path('manager/<manager>/status/<status>/contents/<contents>', SearchView.as_view(), name='search'),
    path('manager/<manager>/status/<status>/contents/', SearchNoConView.as_view(), name='search'),
    # path('manager/<query>', SearchManView.as_view()),
    # path('status/<query>', SearchStatusView.as_view()),
]

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('search/', include(search_patterns)),
    path('issueDetail/<int:pk>', DetailIssueView.as_view()),
    path('update/<int:pk>', UpdateWorkView.as_view()),
    path('issueUpdate/<int:pk>', UpdateIssueView.as_view()),
    path('create/', CreateWorkView.as_view()),
    path('issueCreate/<int:pk>', CreateIssueView.as_view()),
    path('issueCreate/', CreateIssueView.as_view()),
    path('delete/<int:id>', delete_work),
    path('issue/delete/<int:id>', delete_work),
]

