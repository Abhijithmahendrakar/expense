from django.urls import path,include
from . import views
from django.contrib.auth.views import logout_then_login

app_name="track"
urlpatterns=[
	# URL for  signup page
    path('signup/',views.signup,name="signup"), 
    # URL for Adding items
    path('item/',views.add_item,name="items"),  
    # URL for displaying
    path('display/',views.display,name="display"),
    # URL for deleting
    path('<int:id>/', views.delete, name='delete'), 
 
]