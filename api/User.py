from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from schemas import UserSchemas
from config.config import get_db
from utils.UserUtils import create_user, get_user_by_email
from config import Security
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post("/register", status_code=status.HTTP_200_OK)
async def regiser_user(user: UserSchemas.User, db: Session = Depends(get_db)):
    check_email = get_user_by_email(db,user.email)
    if not check_email:
        result = create_user(db, user)
        if result:
            return {'status': True, 'msg': 'User created sucessfully'}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Something went wrong")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Email already exists')



@router.post("/login", status_code=status.HTTP_200_OK, response_model=UserSchemas.Token)
async def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_details = get_user_by_email(db, user.username)
    print('user_details', user_details)
    if not user_details:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': 'email not exists'})

    
    if not Security.verify_hash(user.password, user_details.password):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail={'error': 'Invalid password'})


    create_token = Security.generate_access_token(data={'user_id': user_details.id})

    return {'status': True, 'msg': 'Login Sucessfully', 'access_token': create_token, 'token_type': 'bearer'}


