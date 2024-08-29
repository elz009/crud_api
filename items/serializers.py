from rest_framework import serializers
from django.db.models import Sum
from .models import User, House, Team, Task, CardTask, Report, TestCategory, Test, Questions, Answer, WrittenTest, Event, ResponsibleCart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CardTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardTask
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'student', 'card_tasks', 'total_point', 'dateCreated']

class TestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCategory
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class WrittenTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenTest
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ResponsibleCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsibleCart
        fields = '__all__'

class MonthlyReportSerializer(serializers.Serializer):
    month = serializers.CharField()
    total_reports = serializers.IntegerField()
    total_points = serializers.FloatField()

class UserReportSerializer(serializers.ModelSerializer):
    total_points = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'fullname', 'total_points']

    def get_total_points(self, obj):
        reports = Report.objects.filter(student=obj)
        total_points = reports.aggregate(total=Sum('total_point'))['total'] or 0
        return total_points

# Добавляем UserTotalPointsSerializer
class UserTotalPointsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    total_points = serializers.FloatField()
