from django.contrib import admin
from .models import User, House, Team, Task, CardTask, Report, TestCategory, Test, Questions

admin.site.register(User)
admin.site.register(House)
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(CardTask)
admin.site.register(Report)
admin.site.register(TestCategory)
admin.site.register(Test)
admin.site.register(Questions)
