from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .my_signals import my_signal

def before_save(sender, **kwargs):
    print(sender)
    print(kwargs)

pre_save.connect(before_save)

@receiver(post_save)
def my_post(sender, **kwargs):
    print("post save function")
    print(sender)
    print(kwargs)

@receiver(my_signal)
def my_fun(sender, **kwargs):
    print("我的信号")
    print(sender)
    print(kwargs)