# This server for tracking gt02a gps tracker

###Instructions:
- Add mapbox token into settings.py os.environ.setdefault("MAPBOX_ACCESS_TOKEN", 'pk.test')
- `git clone git@github.com:rlazoryshchak/gt02a_tracker.git`
- `virtualenv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`
- `cd gt02a_tracker`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python gps_socket_handler & python manage.py runserver 0.0.0.0:8000`

### Demo coordinates:
- open new terminal tab and simulate gsp tracker socket request `python gps_socket_sender.py`
- navigate http://server.ip/2016-01-14 you will see demo 

###Usage:
- configure your gps device to server ip and port 8821, run server and waiting for coordinates receiving

![alt text][logo]

[logo]: https://github.com/rlazoryshchak/gt02a_tracker/blob/master/demo1.png 'Demo'
