from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["study-agent"])

def service(db.Session = Depends(get_db))-> StudentService:
    return StudentService(db)

@router.post("/students", response_model=dto.StudentStatus, status_code=status.HTTP_201_CREATED)
def register(body: dto.StudentCreate, svc: StudentService 
= Depends(service)):
    s = svc.register(body)
    return svc.status(s.id)
    

