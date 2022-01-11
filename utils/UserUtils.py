from sqlalchemy.orm import Session
from models import UserModel
from schemas import UserSchemas
from config import Security


def get_user(db: Session, user_id):
    return db.query(UserModel.Users).filter(UserModel.Users.id == user_id).first()


def create_user(db: Session, user: UserSchemas.User):

    try:
        hash_password = Security.hash_string(user.password)

        result = UserModel.Users(name = user.name, email = user.email, password = hash_password, mobile_num = user.mobile_num)
        db.add(result)
        db.commit()
        db.refresh(result)
        return True
    except Exception as e:
        return False, e


def get_user_by_email(db: Session, email: str):
    try:
        return db.query(UserModel.Users).filter(UserModel.Users.email == email).first()
    except Exception as e:
        return False, e


