from myapp import views
from django.urls import path

urlpatterns = [
    # path("", views.index, name='index'),
    # path("about/", views.about, name='about'),
    # path("contact/", views.contact, name='contact'),
    path("", views.prediction, name='prediction')
]
