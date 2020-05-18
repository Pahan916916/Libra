from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

from accounts.views import login_view, register_view, logout_view
from api.views import *
from libra.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('help/', help),
    path('books/', books),
    path('authors/', authors),
    path('category/', category_list),
    path('category/<int:id>/', category_about),
    path('author/<int:id>/', author_about),
    path('book/<int:id>/', book_about),
    path('book/<int:id>/read', book_reader),
    path('accounts/login/', login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view),
    path('api/get_text_from_book/', get_text_from_book)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
