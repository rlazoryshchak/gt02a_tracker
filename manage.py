#!/usr/bin/env python
import os
import sys
from subprocess import Popen


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gt02a_tracker.settings")

    # if sys.argv[1] == 'runserver':
    #     Popen('python gps_socket_handler.py', shell=True)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
