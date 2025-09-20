from django.dispatch import receiver
from django.db.models.signals import post_save
from . import models
import os
import requests
@receiver(post_save,sender=models.Order)
def send_message(sender, instance, created,**kwargs):
    if instance.user_name and instance.wilaya and instance.specific_design and instance.specific_design_img:
        text = f"""
        Product Name : {instance.product}\nOrder id : {instance.id}\nUser Name :{instance.user_name}\nWilaya : {instance.wilaya} \nBaldia : {instance.baldia}\nAddress: {instance.Address}\ndelivry Method : {instance.delivry_method}\nPhone Number: {instance.phone}\nUser token : {instance.user.token}\n Quantity : {instance.quantity}\nColor : {instance.color}\nSize : {instance.size}\n Price : {instance.price}DZD,\nspecific_design:{instance.specific_design}
    """
        instance.user.orders_number+=1
        instance.user.save()
        token = os.environ.get("token")
        chat_id = os.environ.get("chat_id")
        domin = "http://127.0.0.1:5000/"
        photo= f"{domin}{instance.specific_design_img.url}"
        url=f"https://api.telegram.org/bot{token}/sendPhoto"
        data= {
           'chat_id':chat_id,
           "photo":photo,
           "caption":text
        }
        r = requests.post(url,data=data)
    elif instance.user_name and instance.wilaya:
     token = os.environ.get("token")
     chat_id = os.environ.get("chat_id")
     text = f"""
        Product Name : {instance.product}\nOrder id : {instance.id}\nUser Name :{instance.user_name}\nWilaya : {instance.wilaya} \nBaldia : {instance.baldia}\nAddress: {instance.Address}\ndelivry Method : {instance.delivry_method}\nPhone Number: {instance.phone}\nUser token : {instance.user.token}\n Quantity : {instance.quantity}\nColor : {instance.color}\nSize : {instance.size}\n Price : {instance.price}DZD\nspecific_design:{instance.specific_design}
    """
     url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
     requests.get(url)
     notiurl = "https://api.expo.dev/v2/push/send"
     phones = models.Phone.objects.all()
     for phone in phones:
      print(phone.token)
      body = {
        "to": phone.token,
        "title": "ORDER",
        "body": "you have a new order"
      }
      requests.post(notiurl,body)