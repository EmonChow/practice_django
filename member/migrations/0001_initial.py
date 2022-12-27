# Generated by Django 3.2.8 on 2022-03-14 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authentication.user')),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_name', models.CharField(blank=True, max_length=255, null=True)),
                ('village', models.CharField(blank=True, max_length=255, null=True)),
                ('post_office', models.CharField(blank=True, max_length=255, null=True)),
                ('union', models.CharField(blank=True, max_length=255, null=True)),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
                ('religion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('authentication.user',),
        ),
        migrations.CreateModel(
            name='GeneralMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='general_member', to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='ExecutiveMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='executive_member', to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='AdviserMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='adviser_member', to='member.member')),
            ],
        ),
    ]