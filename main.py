from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# MySQL 연결 설정
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '0000',
    'database': 'testdb',
    'port' : 3306
}

# SQLAlchemy 엔진 생성
engine = create_engine(f"mysql+mysqlconnector://{mysql_config['user']}:{mysql_config['password']}@{mysql_config['host']}:{mysql_config['port']}/{mysql_config['database']}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# 사용자 모델 정의
class User(Base):
    __tablename__ = "test"
    a = Column(String(255), primary_key=True, index=True)
    b = Column(String(255))

# 테이블 생성
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/users")
async def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return {"users": users}