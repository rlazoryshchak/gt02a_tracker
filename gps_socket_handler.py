import socket, os, django, re
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gt02a_tracker.settings")
django.setup()

from tracker.models import Point

HOURS = 3

def write_coordinates(s):
    n_pattern = re.compile('(?<=A)[\d\.]+(?=N)')
    e_pattern = re.compile('(?<=N)[\d\.]+(?=E)')
    date_pattern = re.compile('(?<=BR[\d]{2})[\d]+(?=A)')
    time_pattern = re.compile('(?<=E[\d\.]{5})[\d]{6}')

    try:
        n = float(n_pattern.findall(s)[0])
        e = float(e_pattern.findall(s)[0])

        lat = int(n/100) + (((float(n/100) - int(n/100)) * 100) / 60)
        lng = int(e/100) + (((float(e/100) - int(e/100)) * 100) / 60)

        date = date_pattern.findall(s)[0]
        time = time_pattern.findall(s)[0]
        created_at = datetime.strptime(date + time, '%y%m%d%H%M%S') + timedelta(hours=HOURS)

        point = {'lat': round(lat, 4), 'lng': round(lng, 4), 'created_at': created_at}
    except IndexError:
        return None

    last = Point.objects.last()
    if not last or last.created_at < point['created_at'] - timedelta(seconds=30):
        created_point = Point.objects.create(lat=point['lat'], lng=point['lng'], created_at=point['created_at'])
        updated_point = Point.snap_to_road(created_point)
        with open('log', 'a+') as log:
            log.write('Coordinates for point are: %s\n' % [updated_point.lat, updated_point.lng])
                    


sock = socket.socket()
sock.bind(('', 8821))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    data = conn.recv(4096)
    with open('log', 'a+') as log:
        log.write('Received data is: %s\n' % data)
    write_coordinates(data)
    if not data: break
    conn.close()
