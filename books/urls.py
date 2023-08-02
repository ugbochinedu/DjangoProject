from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('books', views.BookViewSet)
router.register('authors', views.AuthorViewSet)
# print(router.urls)

urlpatterns = router.urls

# urlpatterns = [
    # path('book/', views.book_list),
    # path('book/', views.BookViewSet.as_view()),
    # path('book/<int:pk>', views.BookDetail.as_view()),
    # path('', include(router.urls)),

    # path('author/', views.AuthorList.as_view()),
    # path('author/<int:pk>', views.AuthorDetail.as_view(), name="author-detail")
    # path('welcome/', views.welcome),
    # path('hello/', views.hello),
    # path('books/pk/', views.get_books)
# ]