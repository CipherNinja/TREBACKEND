from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, Subject
from django.http import FileResponse
from django.conf import settings
import os


@api_view(['GET'])
def course_api(request):

    course_id = request.GET.get('course_id')
    subject_id = request.GET.get('subject_id')
    pdf_request = request.GET.get('pdf') == "true"

    if not course_id and not subject_id:
        courses = Course.objects.prefetch_related('subjects').all()
        response_data = [
            {
                "id": course.id,
                "title": course.title,
                "subjects": [
                    {"id": subject.id, "title": subject.title}
                    for subject in course.subjects.all()
                ]
            }
            for course in courses
        ]
        return Response(response_data)


    try:
        course = Course.objects.prefetch_related('subjects').get(id=course_id)
        subject = Subject.objects.prefetch_related('exam_patterns', 'subject_contents').get(id=subject_id, course=course)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=404)
    except Subject.DoesNotExist:
        return Response({"error": "Subject not found"}, status=404)

    
    if pdf_request:
        if not subject.pdf_link:
            return Response({"error": "No PDF available for this subject"}, status=404)

        pdf_path = os.path.join(settings.MEDIA_ROOT, subject.pdf_link.name)
        if os.path.exists(pdf_path):
            return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
        else:
            return Response({"error": "File not found"}, status=404)

    

    response_data = {
        "course": {
            "id": course.id,
            "title": course.title,
            "description": course.description,
            "banner": course.banner.url if course.banner else None,
            "subjects": [
                {
                    "id": subject.id,
                    "title": subject.title,
                    "description": subject.description,
                    "pdf_link": subject.pdf_link.url if subject.pdf_link else None,
                    "exam_patterns": [
                        {
                            "topics": ep.topics,
                            "sub_topics": ep.sub_topics,
                            "total_questions": ep.total_questions,
                            "total_marks": ep.total_marks,
                            "duration": ep.duration
                        }
                        for ep in subject.exam_patterns.all()
                    ],
                    "subject_contents": [
                        {
                            "title": sc.title,
                            "description": sc.description,
                            "reference_links": sc.reference_links
                        }
                        for sc in subject.subject_contents.all()
                    ]
                }
            ]
        }
    }
    
    return Response(response_data)


@api_view(['GET'])
def pyq_api(request):
    file_path = request.GET.get('file')
    
    if file_path:
        absolute_path = os.path.join(settings.MEDIA_ROOT, file_path.lstrip('/media/'))
        if os.path.exists(absolute_path):
            return FileResponse(open(absolute_path, 'rb'), content_type='application/pdf')
        else:
            return Response({"error": "File not found"}, status=404)
    
    courses = Course.objects.prefetch_related('pyqs').all()
    pyq_data = {}
    
    for course in courses:
        pyq_files = [pyq.file.url for pyq in course.pyqs.all()]
        if pyq_files:
            pyq_data[course.title] = pyq_files
    
    return Response(pyq_data)
