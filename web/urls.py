from django.urls import path
from .import views
import re
from .views import submit_expense


urlpatterns = [
    path('submit_expense', submit_expense  )
         
]