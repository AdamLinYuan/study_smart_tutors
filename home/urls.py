from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Tutoring Packages
    path('weekly-tutoring/', views.weekly_tutoring, name='weekly-tutoring'),
    path('group-tutoring/', views.group_tutoring, name='group-tutoring'),
    path('single-tutoring/', views.single_tutoring, name='single-tutoring'),
    path('university-admissions/', views.university_admissions, name='university-admissions'),

    # Notes
    path('note1/', views.note1, name='note1'),

    # Help
    path('about/', views.about, name='about-us'),
    path('contact/', views.contact, name='contact-us'),

    # Apply
    path('apply/', views.apply, name='apply'),
]
