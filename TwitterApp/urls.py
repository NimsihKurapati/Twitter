from django.urls import path, include
from django.contrib.auth import views as auth_view
from .import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

appname = 'TwitterApp'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    url(r'register/$', views.UserFormView.as_view(), name='register'),

    url(r'^profile_view/(?P<username>[\w]+)/$',views.PublicView, name = "public"),
    path('/logout', auth_view.LogoutView.as_view(template_name= 'TwitterApp/logout.html'), name="logout"),

    path('index/', views.IndexView, name="index"),
    path('retweet/(?P<uuid>[-w\W]+)/(?P<username>[\w]+)/', views.RetweetView, name="retweet"),
    path('retweet_comment/(?P<uuid>[-w\W]+)/(?P<username>[\w]+)/', views.RetweetCommentView, name="retweet_comment"),

    path('explore/', views.ExploreView, name="explore"),
    path('notifications/', views.NotificationView, name = "notification"),
    path('messages/', views.MessageView, name = "messages"),
    path('bookmarks/', views.BookmarkView, name = "bookmarks"),
    path('lists/', views.ListView, name = "lists"),
    path('profile/', views.ProfileView, name = "profile"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)