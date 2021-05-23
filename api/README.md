## Weather API

Restful API that provides weather data. 

Following are endpoints supported:
* /_ - shows all endpoints
* /zip - get weather by zipcode and country code
* /geo - get weather by lat/lon coordinates
* /search - get weather by searching by place names


### setup
* clone this repo
* create virtual env
* run `pip install --no-deps -r requirements.txt`

### run the server
* see `config.py` to set correct env variables
* `cd api`
* `python boot.py`

### run tests
* run `pip install -r requirements.test
* `cd api`
* `pytest`
