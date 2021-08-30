from django.urls import path

from .views import BookDocumentView


# router = DefaultRouter()
# books = router.register(r'books',
#                         BookDocumentView,
#                         basename='bookdocument')



# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]                    

urlpatterns = [
    path('search/', BookDocumentView.as_view()),
]