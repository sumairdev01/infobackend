#!/bin/bash

# Build script for Vercel deployment
echo "Building Django application..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python backend/manage.py collectstatic --noinput

# Run migrations
python backend/manage.py migrate --noinput

echo "Build completed successfully!"
