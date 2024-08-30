from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, HouseViewSet, TeamViewSet, TaskViewSet,
    CardTaskViewSet, ReportViewSet, TestCategoryViewSet, TestViewSet,
    QuestionsViewSet, AnswerViewSet, WrittenTestViewSet, EventViewSet,
    ResponsibleCartViewSet, UserTotalPointsView, MonthlyReportView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'houses', HouseViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'card_tasks', CardTaskViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'test_categories', TestCategoryViewSet)
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionsViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'writtentests', WrittenTestViewSet)
router.register(r'events', EventViewSet)
router.register(r'responsible_carts', ResponsibleCartViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/user-total-points/<int:user_id>/', UserTotalPointsView.as_view(), name='user-total-points'),
    path('api/monthly-report/', MonthlyReportView.as_view(), name='monthly-report'),
]
