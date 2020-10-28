# Kanban Project - Hiring Process

By Zhiheng Jiao

A full-stack kanban project from scratch for hiring process. Completed in two days. Learned Vue.js on the fly.

Demo on AWS EC2: http://3.83.234.159:8080/

## Key Features

- Six board with draggable applicant cards
- Add new cards with basic information and duplication checking
- Drag card across boards to change applicant's status
- Rate applicants from 1 to 5 star. Display the average score
- Write comment to each card and display
- Expand/collapse detail information of cards by click the button

## Libraries
| Frontend                | Backend           |
| ----------------------- | ----------------- |
| Framework: Vue.js 2     | Framework: Django |
| Style: Bootstrap-vue    | Database: mongoDB |
| Form: vue formulate     | ORM: Djongo       |
| Drag-drop: vuedraggable |                   |
| API call: axios         |                   |
| Host: nginx             |                   |



## RESTful API

| Endpoint                               | Method | Description                                                  |
| -------------------------------------- | ------ | ------------------------------------------------------------ |
| localhost:8000/get-all-applicants      | GET    | Query all applicants information in database                 |
| localhost:8000/get-applicant           | GET    | Check existance of this contact number                       |
| localhost:8000/add-applicant           | POST   | Add a new applicant                                          |
| localhost:8000/add-rate                | POST   | Add a new rate for current applicant and return the average rating |
| localhost:8000/add-comment             | POST   | Add a new comment to the applicant                           |
| localhost:8000/update-applicant-status | POST   | Update the status of the applicant                           |

Support CORS



## Database Schema

```json
# Sample Data
{
    "_id" : ObjectId("5f98cdf79e8d3f4c2ba4decb"),
    "id" : 30,
    "name" : "Henry",
    "education" : "Carnegie Mellon University",
    "contact" : 1234567890,
    "status" : "Applied",
    "rate" : 3.5,
    "rate_number" : 4,
    "comment" : [
      {
        "author" : "HR",
      	"content" : "He is great"
      },
      {
        "author" : "Engineer",
      	"content" : "He is great"
      },
    ]
}
```



## Deployment

Deployed with docker. Since the local environment of my laptop has undefined bug with docker-compose, most of the deployment is done with Dockerfile or Manually.

The dev deployment is on AWS EC2.

Demo link: http://3.83.234.159:8080/

### Deployment for local test

Requirement:

- mongoDB running on localhost:27017
- npm
- Python 3.6 or above and Pip 

Frontend

```
cd ./frontend
npm install
npm run serve
```

Backend

```
cd ./backend/kanban
pip install -r requirements.txt
python manage.py runserver
```



## Development Log

```
* 6dba512 - (HEAD -> master, origin/master) Finished the project (17 seconds ago) <Zhiheng Jiao>
* cdb7f1d - Add frontend .sh (9 hours ago) <Zhiheng Jiao>
* ec5d687 - Deployment on AWS (9 hours ago) <Zhiheng Jiao>
* 588dfc9 - Update (9 hours ago) <Zhiheng Jiao>
* dff68be - Adding deployment configuration (10 hours ago) <Zhiheng Jiao>
* c3594cd - Adding deployment config (10 hours ago) <Zhiheng Jiao>
* bb10804 - Removed redundent frontend component (12 hours ago) <Zhiheng Jiao>
* 1cebe2f - Finished applicant adding duplication checking feature. Applicants with same contact cannot be added (12 hours ago) <Zhiheng Jiao>
* 0d5c8e0 - Finished Comment display and synchonize of frontend and backend (14 hours ago) <Zhiheng Jiao>
* 87908d1 - Finished applicants dragging status synchorizing with the Applicant database (14 hours ago) <Zhiheng Jiao>
* 83810a4 - Finished rating and comment submission in backend and frontend. Solved conflictions (22 hours ago) <Zhiheng Jiao>
* 1ee7b43 - Modified detail / abstract view switch for better experience (34 hours ago) <Zhiheng Jiao>
* bf0f9a8 - Mounted page elements to Database. Auto refresh changes (34 hours ago) <Zhiheng Jiao>
* 65ce6ce - Solved CORS issue (35 hours ago) <Zhiheng Jiao>
* a625aca - Updated readme (2 days ago) <Zhiheng Jiao>
* 5fd54b8 - Initiate backend. Modify file structure (2 days ago) <Zhiheng Jiao>
* 64e2e85 - Finished collasp card (2 days ago) <Zhiheng Jiao>
* 5f70ac4 - Added formulate for rich information creation (2 days ago) <Zhiheng Jiao>
* 3b352fd - Initialize VueFormulate (2 days ago) <Zhiheng Jiao>
* b7c7280 - Added ADD feature (2 days ago) <Zhiheng Jiao>
* 8b61df2 - Create basic draggable kanban view (2 days ago) <Zhiheng Jiao>
* 624e700 - init (2 days ago) <Zhiheng Jiao>
```



