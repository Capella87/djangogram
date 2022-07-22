# Djangogram
Instagram implementation written in Python Django.

## Requirements
* MariaDB 10.6
* Python 3.10 이상
#### Pypi packages
* Django 4.0 이상
* DjangoRestFramework
* Mysqlclient
* django-bootstrap-v5

## Configuration Guide

1. Clone으로 소스 코드를 받는다.
2. PyCharm에서 해당 소스코드 폴더를 로드하고 위에서 언급한 패키지를 설치한다.
3. PyCharm > Settings > Python Interpreters > Show All에서 새 venv를 만든다.
4. MariaDB나 MySQL에 접속하고 다음과 같은 작업을 한다.
    1. 데이터베이스 생성
   ```sql
    CREATE DATABASE djangogram;
    ```
    2. 데이터베이스 관리자 계정 만들기
    ```sql
    CREATE USER '<원하는 유저네임>'@'localhost' IDENTIFIED BY '<원하는 비밀번호>';
    ```
    3. 만든 계정에 권한 부여
    ```sql
    GRANT ALL PRIVILEGES ON djangogram.* TO '<생성한 유저네임>'@'localhost';   
    ```
5. dbconnection.cnf를 다음과 같이 설정해준다. 위치는 레포지토리 최상단으로 한다.
```ini
[client]
database = djangogram
user = <설정한 값>
password = <설정한 값>
default-character-set = utf8
host = 127.0.0.1
port = 3306
```
6. Django-admin을 이용해서 웹페이지 관리자 계정(superuser)을 설정해 준다. (위의 MariaDB 계정과 다름)
```bash
python manage.py createsuperuser
```

7. Migrate를 한다.
```bash
python manage.py migrate
```

8. PyCharm에서 Run 버튼을 누르거나 터미널에서 다음과 같이 입력해서 서버를 돌려 확인한다.
```bash
python manage.py runserver
```

## 참고사항
.idea 파일이 수정될 수도 있는데 커밋할 때 포함시키지 마세요. 이 부분은 차후 커밋으로 제거할 예정입니다.

## 기능

---
Copyright (c) 2022 Capella87 and his teammates.