# usamos as para poner un alias
from .celery import app as celery_app

# Se tiene que poner la coma despues del 'celery_app' -> , // De este modo se celery reconoce la funcion (variable al proyecto)
__all__ = ('celery_app',)