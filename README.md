# Kanban project

By Zhiheng Jiao

A full-stack kanban project from scratch for hiring process. Completed in two days. Learned Vue.js on the fly.

Demo link: http://3.83.234.159:8080/

## Key features

- Six board with draggable applicant cards
- Add new cards with basic information and duplication checking
- Drag card across boards to change applicant's status
- Rate applicants from 1 to 5 star. Display the average score
- Write comment to each card and display
- Expand/collapse detail information of cards

## Libraries
| Frontend                | Backend           |
| ----------------------- | ----------------- |
| Framework: Vue.js 2     | Framework: Django |
| Style: Bootstrap-vue    | Database: mongoDB |
| Form: vue formulate     | ORM: Djongo       |
| Drag-drop: vuedraggable |                   |
| API call: axios         |                   |
| Host: nginx             |                   |

## Deployment

Deployed with docker. Since the local environment of my laptop has undefined bug with docker-compose, most of the deployment is done with Dockerfile or Manually.

The dev deployment is on AWS EC2.

Demo link: http://3.83.234.159:8080/

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



## Development Log





```
git clone https://github.com/ZH-Jiao/Kanban-Henry.git
cd Kanban-Henry/

```

docker

```
docker pull mongo:latest
docker images
docker run -itd --name mongo -p 27017:27017 mongo
docker exec -it mongo mongo admin
> db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});
> db.auth('admin', '123456')
```



mongodb

```
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
sudo systemctl status mongod
```

python

```
sudo apt install python3.8
sudo apt install python3-pip
```

