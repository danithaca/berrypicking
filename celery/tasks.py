from celery import Celery

# to run:
# celery -A tasks worker --loglevel=info

# the `-A` finds the tasks module under PYTHON_PATH, which is in current working folder


# sqlite (filename)
BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'
CELERY_RESULT_BACKEND = 'db+sqlite:///celerydb.sqlite'

# first arg is the module to register with celery. might be other module names other than 'tasks'
# but we are using the same module for convenience.
app = Celery('tasks', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)
# app = Celery('tasks')

@app.task
def add(x, y):
    return x + y