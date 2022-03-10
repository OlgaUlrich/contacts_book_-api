from django.urls import path
from .views import ContactsList, ContactDetailView

urlpatterns = [
    path('', ContactsList.as_view()),
    path('<int:id>', ContactDetailView.as_view())
]