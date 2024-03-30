from django.db import models

class ModelWithSVG(models.Model):
    icon_name = models.CharField(max_length=100)
    svg_content = models.TextField()

    def __str__(self):
        return self.icon_name
    
class Language(models.Model):
    name = models.CharField(max_length=100, verbose_name="Lang Name")
    level = models.CharField(max_length=50, verbose_name="Lang Level")

    def __str__(self):
        return self.name
    
class ProgrammingLanguage(models.Model):
    LANGUAGE_CHOICES = [
        (1, 'beginner'),
        (2, 'elementary'),
        (3, 'intermediate'),
        (4, 'advanced'),
        (5, 'expert')
    ]
    
    name = models.CharField(max_length=100, verbose_name="Programming Lang Name")
    level = models.IntegerField(choices=LANGUAGE_CHOICES, verbose_name="Programming Lang Level")
    icon = models.OneToOneField(ModelWithSVG, on_delete=models.CASCADE, related_name='programming_language_icon',null=True)

    def __str__(self):
        return self.name
    
class Technologies(models.Model):
    LANGUAGE_CHOICES = [
        (1, 'beginner'),
        (2, 'elementary'),
        (3, 'intermediate'),
        (4, 'advanced'),
        (5, 'expert')
    ]
    
    name = models.CharField(max_length=100, verbose_name="Technology Name")
    level = models.IntegerField(choices=LANGUAGE_CHOICES, verbose_name="Technology Level")
    icon = models.OneToOneField(ModelWithSVG, on_delete=models.CASCADE, related_name='technology_icon',null=True)

    def __str__(self):
        return self.name
    
class PortfolioBlock(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    tech_stack = models.CharField(max_length=255, verbose_name="Tech Stack")
    about = models.TextField(verbose_name="About")
    key_responsibilities = models.TextField(verbose_name="Key Responsibilities")
    images = models.ImageField(upload_to='portfolio_images/', verbose_name="Images", blank=True, null=True)
    project_link = models.URLField(max_length=200, verbose_name="Project Link", blank=True, null=True)

    def __str__(self):
        return self.name

class ArticleBlock(models.Model):
    technology_name = models.CharField(max_length=255, verbose_name="Technology Name")
    icon = models.OneToOneField(ModelWithSVG, on_delete=models.CASCADE, related_name='article_icon',null=True)
    title = models.CharField(max_length=255, verbose_name="Title")
    summary = models.TextField(verbose_name="Summary")
    about_article = models.TextField(verbose_name="About Article")
    article_text = models.TextField(verbose_name="Article Text")
    images = models.ImageField(upload_to='article_images/', verbose_name="Article Images", blank=True, null=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name="Company Name")
    icon = models.OneToOneField(ModelWithSVG, on_delete=models.CASCADE, related_name='company_icon',null=True)
    website = models.URLField(max_length=200, verbose_name="Company Website", blank=True, null=True)
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date", blank=True, null=True)
    role = models.CharField(max_length=255, verbose_name="Role")
    role_summary = models.TextField(verbose_name="Role Summary")
    responsibilities = models.TextField(verbose_name="Responsibilities")
    technologies = models.CharField(max_length=255, verbose_name="Technologies and Programming Languages")
    applications_worked_with = models.CharField(max_length=255, verbose_name="Applications Worked With")
    application_description = models.TextField(verbose_name="Application Description")

    def __str__(self):
        return self.name
