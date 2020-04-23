from django.db import models
# from cloudinary.models import CloudinaryField
from django.urls import reverse



class ContactFormModel(models.Model):
    الاسم = models.CharField(max_length=120)
    الرقم = models.CharField(max_length=15)
    الوصف = models.CharField(max_length=500)
    # phone_number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
   
    
    class Meta:
        verbose_name_plural = ('التواصل معنا')
        
    def __str__(self):  # Python 3.3 is __str__
        return self.الرقم



class HomeImage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.TextField(blank= True, null=True)
    description = models.TextField(blank= True, null=True)

    class Meta:
        verbose_name_plural = ('الرئيسية') 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index', args=[str(self.id)])    

      

class Depart1(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.TextField(blank= True, null=True)
    description = models.TextField(blank= True, null=True)

    
    class Meta:  
        verbose_name_plural = ('قسم علاج السحر والحسد والمس')  

    def __str__(self):
        return self.title        
 

class Depart2(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.TextField(blank= True, null=True)
    description = models.TextField(blank= True, null=True)

   
    class Meta:
        verbose_name_plural = ("قسم الاعشاب النادرة" )
   
    def __str__(self):
        return self.title  

class Depart3(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.TextField(blank= True, null=True)
    description = models.TextField(blank= True, null=True)

   
    class Meta:
        verbose_name_plural = ("قسم خواتم روحانيه" )
   
    def __str__(self):
        return self.title          


class Depart4(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.TextField(blank= True, null=True)
    description = models.TextField(blank= True, null=True)

   
    class Meta:
        verbose_name_plural = ("قسم جوهرة علم الروحانيات(هيلوت)" )
   
    def __str__(self):
        return self.title           


class Opinion(models.Model):
    image = models.ImageField(upload_to='images/')
    job = models.TextField(blank= True, null=True)
    name  = models.TextField() 
    description = models.TextField()
    date = models.DateField(blank= True, null=True)
    
   
    class Meta:
        verbose_name_plural = ("الاراء" )
   
    def __str__(self):
        return self.name  



class Youtube(models.Model):
    video = models.TextField()
    description = models.CharField(max_length=200 ,blank= True, null=True)
    date = models.DateField(blank= True, null=True)
    
   
    class Meta:
        verbose_name_plural = ("فيديو الرقية الشرعية" )
   
    def __unicode__(self):
        return self.video  



# class Item(models.Model):
#     video = models.CharField(max_length=200)  # same like models.URLField()