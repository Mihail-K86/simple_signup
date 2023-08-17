from django.apps import AppConfig
import redis

class ProtectConfig(AppConfig):
    name = 'protect'

red = redis.Redis(
    host='redis-18327.c8.us-east-1-4.ec2.cloud.redislabs.com',
    port=18327,
    password='5lvf9adZAd4zLXsgcQ59GAbZ2UFzNqxf',
)