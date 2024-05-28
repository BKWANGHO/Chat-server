
#초기화 파일 맨처음 실행된다. 

from app.api.titanic.service.titanic_service import TitanicService


if __name__ == "__main__":

    service = TitanicService()
    service.preprocess()

