#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_Django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(

        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# CLI directroy: C:\Users\USER\OneDrive\12.Github_repos\Topo_Assessments\website_Django>
# CLI code: python manage.py runserver 0.0.0.0:8000
# http://127.0.0.1:8000/ 