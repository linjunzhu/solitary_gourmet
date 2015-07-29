# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import recipes, users

urlpatterns = [
    # /recipes
    # 只要有()，就会当成一个参数传递到view
    url(r'(^$)|recipes/$', recipes.index, name="recipes.index"),
    # /recipes/:pk
    url(r'^recipes/(?P<pk>[0-9]+)/$', recipes.show, name="recipes.show"),
    # /recipes/new
    url(r'^recipes/new/$', recipes.new, name="recipes.new"),
    # /recipes/create
    url(r'^recipes/create/$', recipes.create, name="recipes.create"),
    # # ex: /polls/5/results/
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]