from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, HouseViewSet, TeamViewSet, TaskViewSet, CardTaskViewSet, ReportViewSet, TestCategoryViewSet, TestViewSet, QuestionsViewSet, AnswerViewSet, WrittenTestViewSet, EventViewSet, ResponsibleCartViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'houses', HouseViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'cardtasks', CardTaskViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'testcategories', TestCategoryViewSet)
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionsViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'writtentests', WrittenTestViewSet)
router.register(r'events', EventViewSet)
router.register(r'responsiblecarts', ResponsibleCartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
