## FAST API PROJECT 
Structured the MVP as a layered FastAPI App, Similar to spring Boot controller, service, repository, and entity layers. it will be dockerized and have tests.
app/
  **main.py** entry point( like @SpringBootApplication)
  **core/** config.py, database.py (like application.properties, datasource)
  **api/v1/routes.py**  REST endpoints (like @RestController)
  **schemas/dto.py** request and response models (like DTOs)
  **Services/** business use cases (like @service)
  **repositories/** database access (like JPA Repository)
  **Models/Entity.py** database tables (like @Entity)
  **Domain/** Question Generators and learn rules with no I/O
**tests/test_api.py** Pytest for the full flow
Dockerfile, requirement.txt, .gitignore, Readme.md

Each request goes from the route to the service, then to the domain rules and the repository, and finally to the database. 

API:
* POST /api/v1/students registers a student.
* GET /api/v1/students/{id}/plan/today returns the due reviews and todays focus topic.
* GET /api/v1/questions/{id}/answer checks an answer and updates mastery and the review date.
* GET /api/v1/students/{id}/status returns mastery per topic and the streak.
* GET /health is the health check.

## The correct answers stay on the server, and each question can only be answered once. it uses SQLite for now, and DATABASE_URL switches it to postgresql without code changes.





