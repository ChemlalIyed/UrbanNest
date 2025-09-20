from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    category =  models.CharField(max_length=40)
    description = models.TextField(blank=True,help_text="Add the text show in the home page, write <br> for line break")
    other = models.CharField(blank=True)
    img = models.ImageField(upload_to='home/')
    def __str__(self):
        return self.category
    
def Getcategory():
   return list(Category.objects.values_list('category', 'category'))

class Products(models.Model):
    name =  models.CharField(max_length=40)
    price = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(99999)])
    quantity=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(99999)])
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='products/')
    category  = models.CharField(choices=Getcategory)
    date= models.DateTimeField(auto_now=True)
    sizes = models.JSONField(blank=True)
    like = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(99999)])
    likers = models.JSONField(default=list,blank=True)
    colors = models.JSONField(blank=True)
    specific_design = models.BooleanField(default=False)
    price_after = models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0),MaxValueValidator(99999)])
    def __str__(self):
        return self.name

class Homepage_image(models.Model):
    name =   models.CharField(max_length=40)
    description = models.TextField(blank=True)
    color = models.CharField(blank=True)
    img = models.ImageField(upload_to='home/')
    def __str__(self):
        return self.name

class Cart(models.Model):
    token =  models.UUIDField(max_length=100)
    product = models.ForeignKey(to=Products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(99999)])
    price = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(99999)])
    color = models.CharField()
    size = models.CharField()
    specific_design = models.BooleanField(default=False)
    specific_design_img = models.ImageField(upload_to="specific_design/",blank=True,null=True)
    class Meta:
        unique_together = ('token', 'product')
    def __str__(self):
        return f"cart for user : {self.token}"
    
class User(models.Model):
    token =  models.UUIDField(max_length=100)
    banned = models.BooleanField(default=False)
    orders_number =  models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="orders")
    user_name  = models.CharField(max_length=50,blank=True)
    wilaya  = models.CharField(max_length=100,blank=True)
    baldia  = models.CharField(max_length=100,blank=True)
    Address  = models.CharField(max_length=100,blank=True)
    delivry_method  = models.CharField(max_length=100,blank=True)
    phone  = models.CharField(max_length=15,blank=True)
    product = models.ForeignKey(to=Products,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity=models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    specific_design = models.BooleanField(default=False)
    specific_design_img = models.ImageField(upload_to="specific_design/",blank=True,null=True)
    

class Phone(models.Model):
    name=models.CharField(max_length=50,blank=True)
    token=models.CharField(max_length=50,null=False,blank=False,unique=True)
