from django.urls import path
from . import views

viewset = views.DentalProfileView.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})


urlpatterns = [
	path('sign_up', views.UserSignUp.as_view(), name='signup'),
	path('sign_in', views.UserSignIn.as_view(), name='signin'),
	path('sign_out', views.UserSignOut.as_view(), name='signout'),
	path('user_details', views.UserDetailView.as_view(), name='user-details'),
    path('dental-profile', viewset, name='dental-profile')
]