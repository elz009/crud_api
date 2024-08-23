from django.contrib import admin
from .models import User, House,Item,Answer, Team, Task, CardTask,ResponsibleCart, Report,Event,WrittenTest, TestCategory, Test, Questions

admin.site.register(User)
admin.site.register(House)
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(CardTask)
admin.site.register(Report)
admin.site.register(TestCategory)
admin.site.register(Test)
admin.site.register(Questions)
admin.site.register(ResponsibleCart)
admin.site.register(Event)
admin.site.register(WrittenTest)
admin.site.register(Item)
admin.site.register(Answer)
