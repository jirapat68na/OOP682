from .repositories import ITaskRepository
from .models import TaskCreate
from fastapi import HTTPException, status

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # 🔴 Validation: ห้าม title ซ้ำ
        existing_task = self.repo.get_by_title(task_in.title)
        if existing_task:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Task title already exists"
            )

    def mark_task_complete(self, task_id: int):
        task = self.repo.get_by_id(task_id)
        if not task:
            return None
        return self.repo.mark_complete(task_id)