
This repo is on prod at https://taxifaremodelapi.herokuapp.com/

The hosting is free, the site may take up to 30 seconds to load initially

Test predictions:
- https://taxifaremodelapi.herokuapp.com/predict_fare?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6413111&dropoff_latitude=-73.7803331&passenger_count=2
- https://taxifaremodelapi.herokuapp.com/predict_fare?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.7331166&dropoff_latitude=-73.9974078&passenger_count=2

Test prediction notebook:
- api client.ipynb

# usage

You may run this on your machine:

``` bash
env FLASK_APP=app.py flask run
```

Or through the `ifmain`:

``` bash
python app.py
```

# prod

``` bash
heroku ps:scale web=1
```
