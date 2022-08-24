from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task(bind=True)
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """

    order = Order.objects.get(id=order_id)
    
    subject = f'Order nr. {order.id}'
    
    message = f"""Dear {order.first_name},\n\n' 
                You have successfully placed an order.' 
                Your order ID is {order.id}."""


    return send_mail(subject, message, 'admin@myshop.com',[order.email])

"""
# @app.task(bind=True, max_retries=3, default_retry_delay=10, autoretry_for=(Exception,))
@app.task(bind=True, max_retries=3, default_retry_delay=10, )
def exibir(self):
    # self.retry(countdown=self.request.retries * 2)
    return 'Exibindo tarefa'
"""