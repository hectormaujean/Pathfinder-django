from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # ex: /job
    url(r'^(?P<job_title>(\w+)+)$', views.job, name='job'),
    # ex: /ecole
    url(r'^(?P<school>(ece|all)+)$', views.job, name='job'),
    # ex: /sexe
    url(r'^(?P<gender>(male|female|all)+)$', views.job, name='job'),
    # ex: /job/sexe
    url(r'^(?P<job_title>(\w+)+)/(?P<gender>(male|female|all)+)$', views.job, name='job'),
    # ex: /job/ecole
    url(r'^(?P<job_title>(\w+)+)/(?P<school>(ece|all)+)$', views.job, name='job'),
    # ex: /ecole/sexe
    url(r'^(?P<school>(ece|all)+)/(?P<gender>(male|female|all)+)$', views.job, name='job'),
    # ex: /job/ecole/sexe
    url(r'^(?P<job_title>(\w+)+)/(?P<school>(ece|all)+)/(?P<gender>(male|female|all)+)$', views.job, name='job'),

]