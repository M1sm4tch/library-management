# Generated by Django 4.2.3 on 2023-10-14 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_alter_issuedbook_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='isbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.book'),
        ),
    ]
