# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from ..models import *
from ..forms.recipe import *
import pdb

# index of recipes
def index(request,none):
    template = 'recipes/index.html'
    recipes = Recipe.objects.all().order_by("-created_at")
    return render(request, template, {'recipes': recipes})

# detail of one recipe
def show(request):
    pass

def new(request):
    template = 'recipes/new.html'
    form = RecipeForm
    return render(request, template, {'form': form})

def create(request):
    form = RecipeForm(request.POST, request.FILES)
    if form.is_valid():
        # 直接保存form都 OK 的？
        recipe = Recipe(
            content = form.cleaned_data['content'],
            title = form.cleaned_data['title'],
            avatar = form.cleaned_data['avatar'],
        )
        recipe.created_at = timezone.now()
        recipe.updated_at = timezone.now()
        recipe.save()
        # 这里需要看下如何动态拿到url
        return redirect('/recipes')
    else:
        template = 'recipes/new.html'
        return render(request, template, {'form': form})