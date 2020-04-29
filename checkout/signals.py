from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(send, instance, created, **kwargs):
    """
    Update order total on line item update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def delete_on_save(send, instance, **kwargs):
    """
    Update order total on line item delete
    """
    instance.order.update_total()
