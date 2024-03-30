# Generated by Django 5.0.3 on 2024-03-29 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0002_modelwithsvg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelwithsvg',
            old_name='name',
            new_name='icon_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='modelwithsvg',
            name='image',
        ),
        migrations.AddField(
            model_name='articleblock',
            name='icon',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_icon', to='portfolioApp.modelwithsvg'),
        ),
        migrations.AddField(
            model_name='company',
            name='icon',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_icon', to='portfolioApp.modelwithsvg'),
        ),
        migrations.AddField(
            model_name='modelwithsvg',
            name='svg_content',
            field=models.TextField(default=-2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programminglanguage',
            name='icon',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='programming_language_icon', to='portfolioApp.modelwithsvg'),
        ),
        migrations.AddField(
            model_name='technologies',
            name='icon',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='technology_icon', to='portfolioApp.modelwithsvg'),
        ),
        migrations.AlterField(
            model_name='programminglanguage',
            name='level',
            field=models.IntegerField(choices=[(1, 'beginner'), (2, 'elementary'), (3, 'intermediate'), (4, 'advanced'), (5, 'expert')], verbose_name='Programming Lang Level'),
        ),
        migrations.AlterField(
            model_name='technologies',
            name='level',
            field=models.IntegerField(choices=[(1, 'beginner'), (2, 'elementary'), (3, 'intermediate'), (4, 'advanced'), (5, 'expert')], verbose_name='Technology Level'),
        ),
    ]
