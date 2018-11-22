# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Article
from django.shortcuts import render


def article_list(request):
  articles = Article.objects.all().order_by('date')
  return render(request,'articles/article_list.html',{'articles':articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})