from django.urls import path
from rest_framework.routers import DefaultRouter
from polls.apiviews import PollViewSet, ChoiceList, CreateVote


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')


urlpatterns = [
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls
