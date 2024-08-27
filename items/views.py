from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime
import calendar
from .models import User, House, Team, Task, CardTask, Report, TestCategory, Test, Questions, Answer, WrittenTest, Event, ResponsibleCart
from .serializers import UserSerializer, HouseSerializer, TeamSerializer, TaskSerializer, CardTaskSerializer, ReportSerializer, TestCategorySerializer, TestSerializer, QuestionsSerializer, AnswerSerializer, WrittenTestSerializer, EventSerializer, ResponsibleCartSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

class UserTotalPointsView(generics.GenericAPIView):
    def get(self, request, user_id):
        reports = Report.objects.filter(student_id=user_id)
        total_points = reports.aggregate(Sum('total_point'))['total_point__sum'] or 0
        return Response({'user_id': user_id, 'total_points': total_points})

class MonthlyReportView(APIView):
    def get(self, request, format=None):
        today = timezone.now().date()
        first_day_of_month = today.replace(day=1)
        last_day_of_month = today.replace(day=calendar.monthrange(today.year, today.month)[1])

        reports = Report.objects.filter(dateCreated__range=[first_day_of_month, last_day_of_month])
        
        total_points = reports.aggregate(Sum('total_point'))['total_point__sum'] or 0
        
        return Response({
            'total_points': total_points,
            'total_reports': reports.count(),
            'month': today.strftime('%B %Y')
        }, status=status.HTTP_200_OK)
