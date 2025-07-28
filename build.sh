#!/usr/bin/env bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# ✅ TEMPORARY: Apply database migrations
python manage.py migrate
