# Generated by Django 4.2.5 on 2023-09-30 09:58

from django.db import migrations, models
import faker.providers.date_time
import faker.providers.person


class Migration(migrations.Migration):
    dependencies = [
        (
            "create_student",
            "0009_alter_student_birth_date_alter_student_first_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="birth_date",
            field=models.DateField(
                default=faker.providers.date_time.Provider.date_of_birth
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="first_name",
            field=models.CharField(
                default=faker.providers.person.Provider.first_name, max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="last_name",
            field=models.CharField(
                default=faker.providers.person.Provider.last_name, max_length=100
            ),
        ),
    ]
