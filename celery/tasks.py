from celery import Celery

# sqlite (filename)
BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'

# app = Celery('tasks', broker='sqla+sqlite:///celerydb.sqlite')
app = Celery('tasks')

@app.task
def add(x, y):
    return x + y