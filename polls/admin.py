from polls.models import Poll
from django.contrib import admin
from polls.models import Choices

class ChoiceInline(admin.StackedInline):
	model = Choices
	extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)