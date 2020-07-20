# data-monitoring
An API to show monitoring reports values and my skill with Python and REST

# Requirements
- Python 3 with Virtualenv
- MongoDB

# Instalation
- Clone the repo:
```
git clone https://github.com/Racafe92/data-monitoring.git
```
- Access to the project folder
```
cd data-monitoring
```
- Create a Python Virtual Environment
```
virtualenv venv
```
- Install all requirements
```
pip install -r requirements.txt
```
- Launch flask server
```
python app.py
```

# Configuration
The DB configuration is in the `setup.py` file. You can introduce your MongoDB URI and database name

# Usage
Accessing to the app, it will be shown a documentation talking about the enabled endpoints:

### POST /api/v1/data-monitoring/
It will require a csv file to be attached. All previous data in the database will be deleted and the new one will replace it. If a file is not provided, it will be returned a 400 error.

### GET /api/v1/data-monitoring/{start_date}/{end_date}
It has two parameters, start_date and end_date. These two parameters are the **timestamps** of the dates between which you want to check. It will return all data between those two timestamps.

# Technical Decissions
## Technology
Due to the simplicity of the project, the chosen framework is **Flask**. This framework, along with flask-RESTX, gives you all the necessary tools to create a complete REST api for this case without need of overcomplicate it. It also generates semi-automatically a documentation that it's quite useful when you have to show the API working.

The database, **MongoDB**, has been chosen because of the perfomance it provides when we all talking about large amounts of data. Checking the data given in the initial CSV, we can see that it generates 96 rows each day, which can escalate quite quickly if we add several others sensors or if we keep it working for several years. Also, there's no table relationships, so we don't need to create a relational DB.

## REST
Checking the front-end mock, we can see that it has a date-range-picker and several tabs showing all the information in between those days. That's why in the REST there's only one endpoint for fetching data. When the user selects a date range, it will be sent only a single HTTP petition to the server, limiting the number of querys to the DB. The front-end will be able to insert that data in the graphs in the different tabs easily, especially if it is using a single-web-application pattern. 

# Future Work
## Documentation
There's little documentation about the endpoints, it can be improved by showing the possible returns and errors a endpoint can give.
## Testing
Testing is a WIP, we should test every endpoint with all possible use cases. Also, we should be able to test the database connection and insertion of data by creating a test database.
## Authentication
As a future project, it is proposed to develop a token-based-authentication by generating a new namespace called "auth". It should have endpoints to CRUD an user and log-in, returning a token. This token would be used in the header of all request in the data-monitoring API to prevent not logged in users to access the data.
## Caching
With Flask, caching can be easily enabled with flask_cache. We could enable cache in the fetch endpoint but it could be counterproductive if the users search for a lot of different date ranges due to the amount of different caches we would need to keep
