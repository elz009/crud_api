from rest_framework import viewsets
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
