"""TwoPhaseCommitProtocol URL Configuration

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
from . import views

urlpatterns = [
    path('create/<str:name>/<int:port>',views.create,name="create"),
    path('ping/<int:port>',views.ping,name="ping"),
    path('view_all',views.view_all,name="view_all"),
    path('delete',views.delete,name="delete"),
    path('master_home',views.master_home,name="master_home"),
    path('sendprepare',views.sendPrepare,name="sendprepare"),
    path('sendready',views.sendReady,name="sendready"),
    path('prepare/<int:port>',views.prepare,name="prepare"),
    path('ready/<int:port>',views.ready,name="ready"),
    path('commit/<int:port>',views.commit,name="commit"),
    path('sendcommit',views.sendCommit,name="sendcommit"),
    path('reset',views.reset,name="reset"),
    path('sendabort',views.sendAbort,name="sendabort"),
    path('abort/<int:port>',views.Abort,name="abort"),
]
