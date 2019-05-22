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
    # URL for sorting by name page
    path('sortname/',views.sortbyname,name="sname"), 
    # URL for sorting by price page
    path('sortprice/',views.sortbyprice,name="sprice"),
    # URL for sorting by date page
    path('sortdate/',views.sortbydate,name="sdate"),
    # URL for editing page
    path('<int:id>/edit/',views.update,name="update"),
 
 
]