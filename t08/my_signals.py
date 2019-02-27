from django.dispatch import Signal

my_signal = Signal(providing_args=["cid", "nid"])