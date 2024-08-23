from rest_framework import serializers
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
