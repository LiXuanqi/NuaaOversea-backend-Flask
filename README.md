# NuaaOversea-backend-Flask

![](https://img.shields.io/github/license/LiXuanqi/NuaaOversea-backend-Flask.svg?style=flat)

NuaaOversea is a studying aboard information sharing platform, which collects information about the admission of students from [NUAA](http://iao.nuaa.edu.cn/) and students' GPA, Language score(TOEFL, IELTS), GRE, etc. 

Provide students with data and similar cases for reference and help them make more informed decisions.

Created with ❤️

This repository stores the code for backend. You can visit the frontend code [here](https://github.com/LiXuanqi/NuaaOversea-frontend-React)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- python >=3.7.0
- docker
- docker-compose

### Setup Database
we use docker to setup the MariaDB as development database. you can implement this part with any sql server.
You can config the database in `docker-compose.yml`.
In the root directory, run command as bellow.
```shell
docker-compose up -d
flask init-db
```
The database runs on **http://localhost:3306**

### Run Server
You can config the server in `config.py`
```shell
git clone https://github.com/LiXuanqi/NuaaOversea-backend-Flask.git
cd NuaaOversee-backend-Flask
pip install -r requirements.txt
flask run
```
The backend server runs on http://localhost:5000

## Running the tests

```shell
pytest
```

## Built With
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1200px-Flask_logo.svg.png)
- [Flask](http://flask.pocoo.org/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- MariaDB

# Task lists

- [ ] add unit tests, achieve >90% code coverage.
- [ ] show REST APIs using Swagger UI.

## Authors

* **Xuanqi Li** - *Initial work*

See also the list of [contributors](https://github.com/LiXuanqi/NuaaOversea-backend-Flask/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
