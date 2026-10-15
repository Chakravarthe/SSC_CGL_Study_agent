# SSC_CGL_Study_agent (MVP)
| Folder | Role | Spring Equivalent |
|------  | ----- | ----------| 
| app/main.py | entri point | @springBootApplication |
| app/core/ | Config, DB session | application.properties, Datasource |
| app/api/v1/ | Rest Endpoints | @RestController |
|app/schemas | request/response/model | DTO |
| app/repositories | DB access | JPARepository |
| app/models | DB Tables | @Entity |
|app/domain | pure Rules and question generators(no I/O) | Domain Layer |
| Tests/ | Pytest | src/test |

## reqest flow: route -> service -> (domain rules + repository ) -> DB.

## Run
python -m venv .venv ; .venv\scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload    # docs: http://localhost:8000/docs
pytest

## Docker 
docker build -t study-agent . ; docker run -p 8000:8000 -v data:/data study-agent.

## API
  POST /api/v1/students register
  GET /api/v1/students/{id}/plan/today due reviews + focus topic
  GET /api/v1/students/{id}/questions/{qid}/answer
  GET /api/v1/students/{id}/status

## ROAD Map
LLM + RAG Tutor Service (app/services/tutor_service.py), previous-year paper abnk, Postgres + Alembic, auth, telegram/Whatsapp Client.


