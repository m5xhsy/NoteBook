import time
from celery import Celery

celery=Celery("tasks", broker = "redis://:Ass078678@192.168.239.128:6363/0", backend="redis://:Ass078678@192.168.239.128:6363/0")

@celery.task
def my_func1():
    return 1

@celery.task
def my_func2():
    print("start 2")
    time.sleep(2)
    print("end 2")
    return "2"

@celery.task
def my_func3():
    print("start 3")
    time.sleep(2)
    print("end 3")
    return "3"
