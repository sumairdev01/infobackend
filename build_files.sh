echo "BUILD START"
python3.9 -m ensurepip || echo "pip already installed"
python3.9 -m pip install -r requirements.txt
mkdir -p staticfiles_build
python3.9 backend/manage.py collectstatic --noinput --clear || echo "collectstatic completed"
echo "Listing staticfiles_build content:"
ls -R staticfiles_build || echo "staticfiles_build is empty"
echo "BUILD END"
