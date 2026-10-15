# 🤖 SSC_CGL_Study_agent (MVP)

A personal, private, judgement-free, and adaptive AI Study Companion for competitive exam aspirants. It guides students from beginner to exam-ready, tracking every metric until they crack the job.

---

## 🎯 Problem Statement
Competitive exam preparation in India relies heavily on large coaching batches of 100–400 students. This traditional model suffers from critical weaknesses:

*   **No Personalization:** Every student receives identical content at the exact same pace, completely ignoring individual differences in understanding, speed, and visualization.
*   **Syllabus-Driven, Not Learner-Driven:** The batch moves forward strictly based on the calendar, whether or not the students have actually mastered the current concepts.
*   **Fear of Asking Doubts:** Students frequently hide their doubts due to peer pressure and fear of ridicule, leaving critical learning gaps unaddressed.
*   **Memorization Over Concepts:** Students memorize specific "tricks" shown in class but feel completely lost and demotivated when a problem appears in an unfamiliar pattern.
*   **No Retention Tracking:** There is zero systematic tracking of what a student forgets after the critical intervals of 3, 7, or 30 days.
*   **No Individual Accountability:** Nobody tracks a student's micro-progress, strengths, or weaknesses, nor does anyone dynamically adjust the study plan relative to the final exam date.

---

## 👁️ Vision
To give every aspirant a private, zero-judgment personal AI tutor. The system acts as a persistent guide that builds deep conceptual understanding, tracks long-term retention, and dynamically changes its strategy based on the individual's learning habits.

---

## ⚙️ Proposed Solution Architecture

### Core Feature Modules

| Module | Purpose & Functionality |
| :--- | :--- |
| **Onboarding & Diagnosis** | Handles user registration for target exams (SSC, Banking, UPSC, GATE, RRB). Conducts a diagnostic test and brief interactions to assess current knowledge depth, learning style (visual, text, example-based), speed, and baseline accuracy. |
| **Learner Profile (Knowledge Graph)** | Dynamically tracks topic and subtopic mastery levels. Segregates and analyzes specific error types (conceptual, calculation, careless, time management) alongside the student's confidence trends. |
| **Roadmap & Timeline Planner** | Works backwards from the target exam date to generate structured daily/weekly goals. Packs in fixed deadlines, buffer days, spaced-repetition revision cycles, and mock tests. Automatically re-plans the trajectory if a student falls behind. |

### Backend Project Structure (FastAPI vs. Spring Boot)

| Folder / File | Architecture Role | Spring Boot Equivalent |
| :--- | :--- | :--- |
| `app/main.py` | Application Entry Point | `@SpringBootApplication` |
| `app/core/` | Configuration & DB Session | `application.properties` / `DataSource` |
| `app/api/v1/` | REST API Endpoints | `@RestController` |
| `app/schemas/` | Pydantic Request/Response Layouts | Data Transfer Objects (DTO) |
| `app/repositories/` | Database Access Layer | `JpaRepository` |
| `app/models/` | Database Tables & Schemas | `@Entity` |
| `app/domain/` | Pure Business Rules & Question Generators (No I/O) | Domain Layer |
| `tests/` | Unit & Integration Testing Suite | `src/test` |

> 🔄 **Request Flow Lifecycle:** 
> `Route` ➡️ `Service` ➡️ `(Domain Rules + Repository)` ➡️ `Database`

---

## 🚀 Execution & Deployment

### Local Development Setup
Run the following commands in your terminal to set up the virtual environment, install dependencies, and launch the hot-reloading development server:

```bash
# Set up and activate virtual environment
python -m venv .venv
source .venv/bin/activate # On Windows use: .venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --reload

# Run test suites
pytest
```
*   📝 **Interactive API Docs:** Once running, access the Swagger UI interface at [http://localhost:8000/docs](http://localhost:8000/docs)

### Docker Deployment
Containerize and deploy the application locally with a persistent volume mapping for data:

```bash
# Build the image
docker build -t study-agent .

# Run the container with volume mapping
docker run -p 8000:8000 -v data:/data study-agent
```

---

## 📡 API Endpoints (v1 Summary)

| Method | Endpoint | Action Description |
| :--- | :--- | :--- |
| `POST` | `/api/v1/students` | Registers a new student and triggers initial onboarding. |
| `GET` | `/api/v1/students/{id}/plan/today` | Fetches active daily goals, target focus topics, and due spaced-repetition reviews. |
| `GET` | `/api/v1/students/{id}/questions/{qid}/answer` | Evaluates student response inputs against a specific question ID. |
| `GET` | `/api/v1/students/{id}/status` | Pulls overall metrics, current weaknesses, and Knowledge Graph standings. |

---

## 🗺️ Roadmap & Upcoming Milestones
- [ ] Implement core **LLM + RAG Tutor Service** (`app/services/tutor_service.py`).
- [ ] Ingest and index complete **Previous-Year Question Paper Bank**.
- [ ] Set up relational database tracking using **PostgreSQL** coupled with **Alembic** migrations.
- [ ] Layer in secure **Authentication & Authorization** protocols.
- [ ] Build external delivery interfaces via **Telegram and WhatsApp client integration**.
