from django.db import models 
from django.db.models import Sum
from datetime import datetime

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(models.Model):
    USER_ROLES = [
        ('student', 'студент'),
        ('assistant', 'Ассистент'),
        ('leader', 'Староста'),
        ('accountant', 'Бухгалтер'),
        ('helper', 'Помощник'),
    ]

    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    course = models.CharField(max_length=50)
    birthday = models.DateField()
    user_role = models.CharField(max_length=20, choices=USER_ROLES)
    questions = models.TextField()
    login = models.CharField(max_length=20, unique=True)  
    password = models.CharField(max_length=128)
    house = models.CharField(max_length=255)  
    team = models.CharField(max_length=255)   

    def __str__(self):
        return self.fullname
    
class House(models.Model):
    id = models.AutoField(primary_key=True)
    headman = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='headman_of_house')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number_of_participants = models.IntegerField()
    payment_date = models.CharField(max_length=50)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    participants = models.ManyToManyField(User, related_name='houses')
    description = models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    accountant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='accountant_of_team')
    houses = models.ManyToManyField(House, related_name='teams')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    point = models.IntegerField()
    minimum = models.IntegerField()
    short_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CardTask(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    local_point = models.IntegerField()

    def __str__(self):
        return f"{self.task.name} - {self.quantity}"
    
class Report(models.Model):
    # Проверьте, нет ли рекурсивных отношений
    student = models.ForeignKey('User', on_delete=models.CASCADE)
    card_tasks = models.ManyToManyField('CardTask')
    total_point = models.IntegerField()
    dateCreated = models.DateField(auto_now_add=True)
    
class TestCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='test_icons/')
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE, related_name='tests')
    questionsCount = models.IntegerField()

    def __str__(self):
        return self.name
    
class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    varA = models.CharField(max_length=255)
    varB = models.CharField(max_length=255)
    varC = models.CharField(max_length=255)
    varD = models.CharField(max_length=255)
    varE = models.CharField(max_length=255, blank=True, null=True)
    correct_answer = models.CharField(max_length=1)  # Assume A, B, C, D, or E
    photo = models.ImageField(upload_to='question_photos/', blank=True, null=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return f"Question for {self.test.name}"

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey('Questions', on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()

    def __str__(self):
        return f"Answer to {self.question.question[:50]}"

class WrittenTest(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='written_tests')
    test = models.ForeignKey('Test', on_delete=models.CASCADE, related_name='written_tests')
    answers = models.ManyToManyField(Answer, related_name='written_tests')
    quantity_correct_answer = models.IntegerField()

    def __str__(self):
        return f"Written Test by {self.user.fullname} for {self.test.name}"

class Event(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    responsible_cart = models.ManyToManyField('ResponsibleCart')  
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    date = models.DateField()
    deadline = models.DateField()
    quantity = models.IntegerField()
    amount_left = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class ResponsibleCart(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    id = models.AutoField(primary_key=True)
    house = models.ForeignKey('House', on_delete=models.CASCADE, related_name='responsible_carts')
    headman = models.ForeignKey('User', on_delete=models.CASCADE, related_name='responsible_carts')
    quantity = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"Responsible Cart for {self.house.name} by {self.headman.fullname}"
