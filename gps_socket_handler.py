import socket, os, django, re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gt02a_tracker.settings")
django.setup()

from tracker.models import Point

def write_coordinates(s):
    n_pattern = re.compile('(?<=A)[\d\.]+(?=N)')
    e_pattern = re.compile('(?<=N)[\d\.]+(?=E)')

    try:
        n = float(n_pattern.findall(s)[0])
        e = float(e_pattern.findall(s)[0])

        lat = int(n/100) + (((float(n/100) - int(n/100)) * 100) / 60)
        lng = int(e/100) + (((float(e/100) - int(e/100)) * 100) / 60)

        data = {'lat': round(lat, 4), 'lng': round(lng, 4)}
    except IndexError:
        data = None

    if data:
        last = Point.objects.last()
        if not last or (last.lat != data['lat'] and last.lng != data['lng']):
            print 'Coordinates for point are: %s' % data
            Point.objects.create(lat=data['lat'], lng=data['lng'])

sock = socket.socket()
sock.bind(('', 8821))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    data = conn.recv(4096)
    write_coordinates(data)
    if not data: break
    conn.close()