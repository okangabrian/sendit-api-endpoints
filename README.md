[![Coverage Status](https://coveralls.io/repos/github/okangabrian/sendit-api-endpoints/badge.svg?branch=develop)](https://coveralls.io/github/okangabrian/sendit-api-endpoints?branch=develop)

# Sendit

Sendit is a parcel delivery service

## Getting Started

Quite simple to get get up and running.

### Prerequisites

python 3.6
Set up a virtual environment

```
```

### Installing

1.Clone the repo 

```
https://github.com/okangabrian/sendit-api-endpoints
```

2.Create and actvate your virtual environment.

```
virtualenv env --python=python3.6

source env/bin/activate
```
3.Install the project dependencies

```
pip install -r requirements.txt
```
4.Run the application

```
-Export the app to flask   export FLASK_APP = run.py
-Start the server 
-Run the app     flask run
```


##  Working endpoints

    Post '/auth/signup' Register a new user
    Post '/auth/login'  user login
    Post '/parcel'     Post a new parcel
    Get  '/parcels'   Get all parcels
    Get  '/parcels/<int:parcel_id>' Get specific parcel
    Get  '/users/<int:user_id>/parcels' get a users all parcels
    Put  '/<int:parcel_id>/cancel'   Cancel a parcel order
    

## post new parcel
```
{
	"price":500,
	"name":"suit",
	"pickup_location":"juja",
	"destination":"Athi river",
	"weight":2
}

```

### Running tests
```
nosetests

- Testing with coverage

nosetests --with-coverage --cover-package=app

```


## Authors

* **Brian Okanga** 

.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

=======
# sendit-api-endpoints
-initial

