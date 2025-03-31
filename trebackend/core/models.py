from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner = models.ImageField(
        upload_to='banners/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )

    def __str__(self):
        return self.title


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    pdf_link = models.FileField(
        upload_to='pdfs/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    ) 

    def __str__(self):
        return self.title


class Exam_Pattern(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exam_patterns')
    topics = models.CharField(max_length=50)  
    sub_topics = models.TextField(blank=False, null=False)
    total_questions = models.TextField(blank=False, null=False)
    total_marks = models.TextField(blank=False, null=False)
    duration = models.IntegerField()
 
    def clean(self):
        """Ensure sub_category and total_questions have the same number of elements."""
        sub_topics_list = [s.strip() for s in self.sub_topics.split(",") if s.strip()] if self.sub_topics else []
        total_questions_list = [q.strip() for q in self.total_questions.split(",") if q.strip()] if self.total_questions else []
        total_marks_list = [m.strip() for m in self.total_marks.split(",") if m.strip()] if self.total_marks else []
        if not (len(sub_topics_list) == len(total_questions_list) == len(total_marks_list)):
            raise ValidationError("Sub Topics, Total questions, and Total marks must have the same number of elements.")

    def save(self, *args, **kwargs):
        """Call clean before saving to enforce validation."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject.title} exam pattern"
    
    class Meta:
        verbose_name_plural = "Exam Pattern"
    

class Subject_Content(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_contents")
    title = models.CharField(max_length=255) 
    description = models.TextField()  
    reference_links = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject.title} - {self.title}"
    
    class Meta:
        verbose_name_plural = "Subject Content"


class PYQ(models.Model):
    course = models.ForeignKey(Course, related_name="pyqs", on_delete=models.CASCADE)
    file = models.FileField(
        upload_to="pyqs/",
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    ) 

    def __str__(self):
        return f"{self.course.title} - {self.file.name}"