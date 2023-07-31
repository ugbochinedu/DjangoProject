from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_list),
    path('book/<int:pk>', views.book_detail),
    path('author', views.author_list),
    path('author<int:pk>', views.author_list, name="author-detail")
    # path('welcome/', views.welcome),
    # path('hello/', views.hello),
    # path('books/pk/', views.get_books)
]