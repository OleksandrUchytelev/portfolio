from django.contrib import admin
from .models import Company, ArticleBlock, PortfolioBlock, Technologies, ProgrammingLanguage, Language, ModelWithSVG

# Register your models here.
admin.site.register(Company)
admin.site.register(ArticleBlock)
admin.site.register(PortfolioBlock)
admin.site.register(Technologies)
admin.site.register(ProgrammingLanguage)
admin.site.register(Language)
admin.site.register(ModelWithSVG)