import time
from celery import Celery


app = Celery('tasks',
        broker='redis://localhost:6379/1', 
        backend='redis://localhost:6379/2',  
        broker_connection_retry_on_startup = True
        )

@app.task
def cpu_bound_function(a, b):
    a + b
    time.sleep(0.5)

    return 'Hello World'
