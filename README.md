## structure of project:

###### apps:
- `authentication`: Account of user and authentication

###### fixtures:
This folder contain file data to seeding when init project

###### TemplateDjango:
This folder contain file config of this app
- `setting.py`:  setting of this app, read config env and setting app
- `urls.py`: Router of this project (handle router)
- `wsgi.py`: File handle deploy using wsgi

###### media:
This folder contain media resource default

###### nginx:
This folder contain file config nginx

###### templates:
This folder contain template email(html)

###### structure of a app:
- `migrations`: folder contain migrations of this app (query to create database)
- `admin`: add model to admin handle
- `version`: create multi version (current default v1)
- `models`: file model of this app
- `filter`: handle filter for api of this app
- `task`: create task to run when handle process background

###### config docker to run thi app
- docker-compose-dev.yml: docker-compose file run for developer, using .env/.develop config
- docker-compose-beta.yml: docker-compose file run for beta environment, using .env/.develop beta
- docker-compose-prod.yml: docker-compose file run for developer, using .env/.develop config

## Start project

###### required:
- docker & docker compose
- python >= 3.6

###### build local debug:
- setting virtualenv
- activate virtualenv
- install package in requirements.txt `pip install -r requirements.txt` 
- start docker-compose for dev: `docker-compose -f docker-compose-dev.yml up`
- run server: `./manage.py runserver 127.0.0.1:8000`

###### import data:
- run file to seeding data: `./entry-point.sh`

## Convention response

request success: 
+ http code = 2XX (200, 201, 204,...)
+ status_code = 0 (response data)

request fail:
+ http code = 4XX (400, 401, 404, 403), 5XX (500, 502)
+ status_code > 0 (response data)

file error_code:


