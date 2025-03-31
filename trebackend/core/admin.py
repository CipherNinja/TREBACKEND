from django.contrib import admin
from django import forms
from .models import Course, Subject, Exam_Pattern, Subject_Content, PYQ

class PYQInline(admin.TabularInline):
    model = PYQ
    extra = 1  

class SubjectContentInline(admin.TabularInline):  
    model = Subject_Content
    extra = 1  

class SubjectInline(admin.TabularInline): 
    model = Subject
    extra = 1  

class ExamPatternInline(admin.TabularInline): 
    model = Exam_Pattern
    extra = 1  

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'banner')
    search_fields = ('title',)
    inlines = [SubjectInline, PYQInline]  
    ordering = ['id']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'pdf_link')
    search_fields = ('title', 'course__title')
    list_filter = ('course',)
    ordering = ['id']
    inlines = [ExamPatternInline, SubjectContentInline] 

class ExamPatternAdminForm(forms.ModelForm):
    class Meta:
        model = Exam_Pattern
        fields = '__all__'

    sub_topics = forms.JSONField(widget=forms.Textarea, required=False)
    total_questions = forms.JSONField(widget=forms.Textarea, required=False)
    total_marks = forms.JSONField(widget=forms.Textarea, required=False)