# Generated by Django 4.0.4 on 2022-05-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_tag_project_vote_total_review_project_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
