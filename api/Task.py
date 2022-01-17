from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session, session
from config.config import get_db
from config import Security
from schemas import TaskSchemas
from utils import TaskUtils

router = APIRouter(
    prefix="/task",
    tags=['Task']
)

@router.post("/lists", status_code=status.HTTP_200_OK)
async def getList(data: TaskSchemas.TaskList, db:session = Depends(get_db), current_user = Depends(Security.get_current_user)):
    status, result, count= TaskUtils.get_task_lists(db, data, current_user.id)
    if status:
        return {'status': True, 'data': result, 'total_count': count}
    else:
        raise HTTPException(status_code = 400, detail = result)


@router.post('/create', status_code=status.HTTP_200_OK)
async def create(data: TaskSchemas.Task, db:session = Depends(get_db), current_user = Depends(Security.get_current_user)):
    result = TaskUtils.create_task(db, data, current_user.id)
    if result:
        return { 'status': True, 'msg': 'Task added successfully'}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Something went wrong")


@router.post('/update', status_code=status.HTTP_200_OK)
async def update(data: TaskSchemas.TaskUpdate, db: session = Depends(get_db), current_user = Depends(Security.get_current_user)):
    status, task_details = TaskUtils.get_task_by_id(db, data.id, current_user.id)
    if status:
        result = TaskUtils.update_task(db, data)
        if result == True:
            return { 'status': True, 'msg': 'Task Updated successfully'}
        else:
            raise HTTPException(status_code= 400, detail=f"Something went wrong")
    else:
        raise HTTPException(status_code= 400, detail=task_details)



@router.get('/delete/{id}', status_code=status.HTTP_200_OK)
async def delete(id: int, db: session = Depends(get_db), current_user = Depends(Security.get_current_user)):
    status, task_details = TaskUtils.get_task_by_id(db, id, current_user.id)

    if status:
        result = TaskUtils.detete_task(db, id)
        if result == True:
            return { 'status': True, 'msg': 'Task deleted successfully'}
        else:
            raise HTTPException(status_code= 400, detail=f"Something went wrong")
    else:
        raise HTTPException(status_code=400, detail=task_details)


@router.get('/get/{id}', status_code=status.HTTP_200_OK)
async def get(id: int, db: session = Depends(get_db), current_user = Depends(Security.get_current_user)):
    status, task = TaskUtils.get_task_by_id(db, id, current_user.id)

    if status:
        return {'status': True, 'msg': 'success', 'data': task}
    else:
        raise HTTPException(status_code=400, detail=task)
