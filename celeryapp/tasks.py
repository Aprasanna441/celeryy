from celery import shared_task 
import time

@shared_task
def fun():
    
    for i in range(0,10):
        print(i)
        time.sleep(3)
    return "done"