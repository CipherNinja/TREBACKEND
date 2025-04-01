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
4. **Fetch All PYQs**
   - **URL**: `/api/v2/`
   - **Method**: `GET`
   - **Description**: Retrieves a list of all PYQs categorized by course.
5. **Get a Specific PYQ PDF**
   - **URL**: `/api/v2/?file={file_name}`
   - **Method**: `GET`
   - **Description**: If a file parameter is provided, returns the requested PDF file.

---

## Example Usage

### Fetch All Courses with Subjects
**Endpoint**: `GET /api/v1/`
**Response**:
```json
[
    {
        "id": 1,
        "title": "BPSC TRE",
        "subjects": [
            {
                "id": 1,
                "title": "PGT(11-12)"
            },
            {
                "id": 2,
                "title": "TGT(9-10)"
            }
        ]
    },
    {
        "id": 2,
        "title": "BIHAR STET",
        "subjects": [
            {
                "id": 3,
                "title": "STET 1 TGT (9-10)"
            }
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
        "title": "BPSC TRE",
        "description": "BPSC Bihar Computer Science Teacher Syllabus 2023 is released by Education Department of Bihar. Candidates must access the BPSC Bihar Computer Science Teacher Syllabus from the article below.",
        "banner": "/media/banners/Screenshot_81.png",
        "subjects": [
            {
                "id": 1,
                "title": "PGT(11-12)",
                "description": "The Bihar Computer Science Teacher Recruitment 2023 is conducted by the Education Department of Bihar. The candidates must refer to the following table for more information on the Bihar Computer Science Teacher Syllabus..",
                "pdf_link": "/media/pdfs/Reference_Income_Tax_Notes_Dec_Batch.pdf",
                "exam_patterns": [
                    {
                        "topics": "Language (Qualifying)",
                        "sub_topics": "Part - 1 English, Part - 2 Hindi / Urdu / Bengali",
                        "total_questions": "25,75",
                        "total_marks": "25,75",
                        "duration": 2
                    },
                    {
                        "topics": "Subject And General Studies",
                        "sub_topics": "Part - 1 Concerned Subject, Part - 2 General Studies",
                        "total_questions": "80, 40",
                        "total_marks": "80, 40",
                        "duration": 2
                    }
                ],
                "subject_contents": [
                    {
                        "title": "Bihar Computer Science Teacher Syllabus for Higher Secondary Teacher.",
                        "description": "Question Pattern - MCQ\r\nPaper 1 Language section is qualifying in nature.\r\nPaper 2 consists of two parts, Part-I and Part-II.\r\nPart-I is a Subject paper. Candidate has to opt for Any One of the papers i.e. Hindi, Urdu, English, Sanskrit, Bengali, Maithili, Magahi, Arabic, Persian, Bhojpuri, Pali, Prakrit, Mathematics, Physics, Chemistry, Botany, Zoology, History, Political Science, Geography, Economics, Sociology, Psychology, Philosophy, Home Science, Computer Science, Commerce Accountancy, Music & Entrepreneurship.\r\nThe questions of the subject paper will be related to the syllabus of the Higher Secondary School but it's standard according to the prescribed minimum qualification of the candidate.\r\nPart-ll is General Studies. It consists of Elementary Mathematics, General Awareness, General Science, Indian National Movements and Geography.\r\nThe Questions of General Studies will be related to the syllabus of the Higher Secondary School but it's standard according to the prescribed minimum qualification of the candidate\r\nThere is no negative marking for Language Section.",
                        "reference_links": "https://www.adda247.com/teaching-jobs-exam/bihar-computer-science-teacher-syllabus/Bihar_Computer_Science_Teacher_Syllabus_Overview"
                    },
                    {
                        "title": "Bihar Computer Science Teacher Syllabus PDF.",
                        "description": "The direct link to download Bihar Computer Science Teacher Syllabus Pdf has been given below. Candidate can download through the below link Bihar CS Teacher Syllabus PDF section wise.",
                        "reference_links": "https://www.adda247.com/teaching-jobs-exam/bihar-computer-science-teacher-syllabus/Bihar_Computer_Science_Teacher_Syllabus_Overview"
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

### Fetch All PYQs
**Endpoint**: `GET /api/v2/`
**Response**:
```json
{
    "BPSC TRE": [
        "PDF_to_Teach.pdf",
        "sample.pdf"
    ],
    "BIHAR STET": [
        "sample_NVkbLDO.pdf"
    ]
}
```

### Get a Specific PYQ PDF
**Endpoint**: `GET /api/v2/?file=sample.pdf`
**Response**: Returns the requested PDF file or an error message.
```json
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