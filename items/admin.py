from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from items import views  
from items.views import UserTotalPointsView  # Импортируем ваш APIView

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'houses', views.HouseViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'card_tasks', views.CardTaskViewSet)
router.register(r'reports', views.ReportViewSet)
router.register(r'test_categories', views.TestCategoryViewSet)
router.register(r'tests', views.TestViewSet)
router.register(r'questions', views.QuestionsViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'written_tests', views.WrittenTestViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'responsible_carts', views.ResponsibleCartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/user-total-points/<int:user_id>/', UserTotalPointsView.as_view(), name='user-total-points'),  # Добавляем маршрут
]
