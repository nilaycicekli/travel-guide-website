from django.apps import AppConfig


class PprofileConfig(AppConfig):
    name = 'pprofile'

    def ready(self):
    	import pprofile.signals
