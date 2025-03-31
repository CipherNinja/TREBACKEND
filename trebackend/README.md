# TRE-Backend

---

### Key Endpoints
1. **Fetch All Courses with Subjects**
   - **URL**: `/api/v1/`
   - **Method**: `GET`
   - **Description**: Retrieves a list of all courses along with their subjects.
2. **Fetch Specific Course and Subject Details**
   - **URL**: `/api/v1/?course_id={course_id}&subject_id={subject_id}`
   - **Method**: `GET`
   - **Description**: Retrieves details of a specific course and subject, including exam patterns and subject contents. 
3. **Get a PDF File**
   - **URL**: `/api/v1/?course_id={course_id}&subject_id={subject_id}&pdf=true`
   - **Method**: `GET`
   - **Description**: Downloads a PDF file for the requested subject if available.

---

## Example Usage

### Fetch All Courses with Subjects
**Endpoint**: `GET /api/v1/`
**Response**:
```json
[
    {
        "id": 1,
        "title": "Course 1",
        "subjects": [
            {"id": 1, "title": "Subject 1"},
            {"id": 2, "title": "Subject 2"}
        ]
    },
    {
        "id": 2,
        "title": "Course 2",
        "subjects": [
            {"id": 3, "title": "Subject 1"},
            {"id": 4, "title": "Subject 2"}
        ]
    }
]
```

### Fetch Specific Course and Subject Details
**Endpoint**: `GET /api/v1/?course_id=1&subject_id=1`
**Response**:
```json
{
    "course": {
        "id": 1,
        "title": "Course 1",
        "description": "Description of Course",
        "banner": "/media/banners/image.png",
        "subjects": [
            {
                "id": 1,
                "title": "Subject 1",
                "description": "Description of Subjects",
                "pdf_link": "/media/pdfs/subject.pdf",
                "exam_patterns": [
                    {
                        "topics": "Language (Qualifying)",
                        "sub_topics": [
                            "Part - 1 English",
                            " Part - 2 Hindi / Urdu / Bengali"
                        ],
                        "total_questions": [
                            25, 75
                        ],
                        "total_marks": [
                            25, 75
                        ],
                        "duration": 2
                    },
                    {
                        "topics": "Subject And General Studies",
                        "sub_topics": [
                            "Part - 1 Concerned Subject",
                            " Part - 2 General Studies"
                        ],
                        "total_questions": [
                            80, 40
                        ],
                        "total_marks": [
                            80, 40
                        ],
                        "duration": 2
                    }
                ],
                "subject_contents": [
                    {
                        "title": "Content Heading",
                        "description": "Description of Subject Content",
                        "reference_links": [
                            "https://www.adda247.com/teaching-jobs-exam/bihar-syllabus/Bihar_Syllabus_Overview"
                        ]
                    },
                    {
                        "title": "Content Heading",
                        "description": "Description of Subject Content",
                        "reference_links": [
                            "https://www.adda247.com/teaching-jobs-exam/bihar-syllabus/Bihar_Syllabus_Overview"
                        ]
                    }
                ]
            }
        ]
    }
}
```

### Get a PDF File
**Endpoint**: `GET /api/v1/?course_id=1&subject_id=2&pdf=true`
**Response**:  Returns the requested PDF file if found else returns an error.
```json
{
    "error": "No PDF available for this subject"
}
{
    "error": "File not found"
}
```


---

## Project setup
### Navigate to root of the project
```
cd ./
```

### Create and Activate Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```


### Install Dependencies
```
python -m pip install Django
pip install djangorestframework
pip install pillow
```

### Run the Migrations
Navigate to the Django project directory:
```
cd trebackend
```

Run the following commands:
```
python manage.py makemigrations
python manage.py migrate
```

### Run Django Server
```
python manage.py runserver
```