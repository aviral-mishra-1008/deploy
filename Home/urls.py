from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name = "Home"),
    path("About/", views.about, name="About"),
    path("Contact/", views.contact_us, name = "Contact s"),
    path("Submission/", views.sub, name="Submission"),
    path('Success/',views.success,name="success"),
    path('Backend/',views.Login,name="backend"),
    path('Verification/',views.article,name="Article"),
    path('search/',views.search,name="search"),
    path('backend_uid/', views.backend, name='backend'),
    path("article/", views.first, name = "firstpost"),
    path('article/<str:slug>/', views.allpost, name="allpost")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


