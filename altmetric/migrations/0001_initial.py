# Generated by Django 3.2.12 on 2022-11-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawAltmetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issn_scielo', models.CharField(max_length=9, verbose_name='ISSN SciELO')),
                ('extraction_date', models.CharField(max_length=50, verbose_name='Extraction Date')),
                ('resource_type', models.CharField(blank=True, choices=[('', ''), ('article', 'Article'), ('journal', 'Journal')], max_length=10, verbose_name='Resource Type')),
                ('json', models.JSONField(blank=True, null=True, verbose_name='JSON File')),
            ],
        ),
        migrations.AddIndex(
            model_name='rawaltmetric',
            index=models.Index(fields=['issn_scielo'], name='altmetric_r_issn_sc_9a6916_idx'),
        ),
        migrations.AddIndex(
            model_name='rawaltmetric',
            index=models.Index(fields=['resource_type'], name='altmetric_r_resourc_326e05_idx'),
        ),
    ]
