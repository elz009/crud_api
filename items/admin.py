from django.contrib import admin
from .models import (
    User, House, Team, Task, CardTask, Report, TestCategory, Test,
    Questions, Answer, WrittenTest, Event, ResponsibleCart
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'university', 'course', 'birthday', 'user_role')
    search_fields = ('fullname', 'login')

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'number_of_participants')
    search_fields = ('name', 'address')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'point', 'minimum')
    search_fields = ('name',)

@admin.register(CardTask)
class CardTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'quantity', 'local_point')
    search_fields = ('task__name',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'total_point', 'dateCreated')
    search_fields = ('student__fullname',)

@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'questionsCount')
    search_fields = ('name', 'description')

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'test')
    search_fields = ('question', 'test__name')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
    search_fields = ('question__question',)

@admin.register(WrittenTest)
class WrittenTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'test', 'quantity_correct_answer')
    search_fields = ('user__fullname', 'test__name')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    search_fields = ('name',)

@admin.register(ResponsibleCart)
class ResponsibleCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'house', 'headman', 'quantity', 'status')
    search_fields = ('house__name', 'headman__fullname')