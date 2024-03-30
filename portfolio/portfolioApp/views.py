from django.shortcuts import render
from django.http import HttpResponse
from .models import Language, ProgrammingLanguage, Technologies, PortfolioBlock, ArticleBlock, Company, ModelWithSVG
from django.http import JsonResponse

def career_view(request):
    companies = Company.objects.all()
    return render(request, 'portfolioApp/career.html', {'companies': companies})

def projects_view(request):
    projects = PortfolioBlock.objects.all()
    return render(request, 'portfolioApp/projects.html', {'projects': projects})

def skills_view(request):
    languages = Language.objects.all()
    programming_languages = ProgrammingLanguage.objects.all()
    technologies = Technologies.objects.all()
    return render(request, 'portfolioApp/skills.html', {'languages': languages, 'programming_languages': programming_languages, 'technologies': technologies})

def articles_view(request):
    articles = ArticleBlock.objects.all()
    svgImages = ModelWithSVG.objects.all()
    return render(request, 'portfolioApp/articles.html', {'articles': articles, 'svgImages': svgImages })

def handle_404(request,exception):
    return render(request, 'portfolioApp/404.html', status=404)

def handle_500(request):
    return JsonResponse({'error': 'Internal server error'}, status=500)
    