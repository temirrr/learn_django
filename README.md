# learn_django
Take-home assignment after interview at Remarcable

## Run instructions

I used Python 3.11 from Conda to have the latest version of Python. I'll assume the user has one of the latest Python versions and proper virtual environment created and activated before running this.

Then run the following commands

```
pip install -r requirements.txt
cd learn_django
python manage.py populate_data
python manage.py runserver
```

Open the browser at http://127.0.0.1:8000/devices

Then you can try to play around and make some queries

## Notes

This project is not ideal. There are some things which could've been done better:

- Make the imports cleaner
- More type annotations
- Make the normal FE page with asynchronous queries, instead of reloading page on every query, which is what Django templates do
- Etc

But I decided to stop here, as the purpose was to just make simple Django app with several model queries.
