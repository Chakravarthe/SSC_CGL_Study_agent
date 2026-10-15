

class StudentService:
    def __init__(self, db: Session):
        self.repo = studentRepository(db)


    #----- helpers
    def _student(self, student_id: int) -> Student:
        s = self.repo.get(student_id)
        if not s:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        return s

    def _days_left(self, s: Student) -> int:
        return(s.exam_date - date.today()).days



    #-----use cases
    def register(self, data: dto.StudentCreate) -> Student:
        s=Student(name=data.name,exam_date=data.exam_date, hours_per_day=data.hours_per_day)
        s.progress = [topicProgress(topic=t) for t in question_bank.TOPICS]
        return self.repo.save(s)

    def status(self, student_id: int) -> dto.StudentStatus:
        s =  self._student(student_id)
        days = self._days_left(s)
        topics = sorted(s.progress, keys=lambda p:p.mastery)
        return dto.StudentStatus(
            id=s.id, name=s.name, days_left=days, phase=learning.phase_for(days), streak=s.streak, 
            topics=[dto.TopicStatus(topic=p.topic, mastery=p.mastery, next_review=p.next_review) for p in topics])

    def daily_plan(self, student_id: int) -> dto.DailyPlan: