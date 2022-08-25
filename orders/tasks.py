from multiprocessing.sharedctypes import Value
from celery import shared_task
from time import sleep
from random import randint

@shared_task(bind=True, max_retries=20, default_retry_delay=2)
def process_payment(self, order_id):
    
    print('Processing customer order: ', order_id)
    sleep(5)
    x = randint(0, 10)
    
    if x > 9:
        return 'OK'

    else:
        self.retry(countdown = 2  ** self.request.retries)
        raise ValueError('Error')
  


"""
# @app.task(bind=True, max_retries=3, default_retry_delay=10, autoretry_for=(Exception,))
@app.task(bind=True, max_retries=3, default_retry_delay=10, )
def exibir(self):
    # self.retry(countdown=self.request.retries * 2)
    return 'Exibindo tarefa'
"""