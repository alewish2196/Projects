# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('date_of_death', models.DateField(null=True, verbose_name=b'Died', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text=b'Enter a brief description of the book', max_length=1000)),
                ('isbn', models.CharField(help_text=b'13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name=b'ISBN')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='catalog.Author', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True, help_text=b'Unique ID for this particular book across whole library')),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(null=True, blank=True)),
                ('status', models.CharField(default=b'd', help_text=b'Book availability', max_length=1, blank=True, choices=[(b'd', b'Maintenance'), (b'o', b'On loan'), (b'a', b'Available'), (b'r', b'Reserved')])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='catalog.Book', null=True)),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('my_field_name', models.CharField(help_text=b'Enter field documentation', max_length=20)),
            ],
            options={
                'ordering': ['-my_field_name'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text=b'Select a genre for this book', to='catalog.Genre'),
        ),
    ]
