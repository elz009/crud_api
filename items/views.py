from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime
import calendar
from .models import User, House, Team, Task, CardTask, Report, TestCategory, Test, Questions, Answer, WrittenTest, Event, ResponsibleCart
from .serializers import UserSerializer, HouseSerializer, TeamSerializer, TaskSerializer, CardTaskSerializer, ReportSerializer, TestCategorySerializer, TestSerializer, QuestionsSerializer, AnswerSerializer, WrittenTestSerializer, EventSerializer, ResponsibleCartSerializer, UserTotalPointsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def total_points(self, request, pk=None):
        user = self.get_object()  # Get the specific user
        total_points = Report.objects.filter(student=user).aggregate(Sum('total_point'))['total_point__sum'] or 0
        return Response({'total_points': total_points})
    
class MonthlyReportView(APIView):
    def get(self, request, *args, **kwargs):
        # Return a simple response to check if the view is working
        return Response({"message": "Monthly report endpoint is working"}, status=status.HTTP_200_OK)

class UserTotalPointsView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            total_points = user.get_total_points()  # Or however you calculate this
            return Response({'total_points': total_points}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CardTaskViewSet(viewsets.ModelViewSet):
    queryset = CardTask.objects.all()
    serializer_class = CardTaskSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    @action(detail=False, methods=['get'])
    def monthly_summary(self, request):
        year = int(request.query_params.get('year', datetime.now().year))
        month = int(request.query_params.get('month', datetime.now().month))
        summary = Report.get_monthly_report(year, month)
        return Response(summary)

class TestCategoryViewSet(viewsets.ModelViewSet):
    queryset = TestCategory.objects.all()
    serializer_class = TestCategorySerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class WrittenTestViewSet(viewsets.ModelViewSet):
    queryset = WrittenTest.objects.all()
    serializer_class = WrittenTestSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ResponsibleCartViewSet(viewsets.ModelViewSet):
    queryset = ResponsibleCart.objects.all()
    serializer_class = ResponsibleCartSerializer
