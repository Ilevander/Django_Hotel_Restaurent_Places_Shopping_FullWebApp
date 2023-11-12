from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

''' PROPERTY = DEAL( Hotel | Place | Shopping | Restaurent)=> Categories'''

'''Main Property'''
class Property(models.Model):
    owner = models.ForeignKey(User,related_name='property_owner',on_delete=models.CASCADE) #To get each property of each customer and render it into his own space
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='propertyimages/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('Place',related_name='property_place',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',related_name='property_category',on_delete=models.CASCADE)   
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True,blank=True)

    #Pour éviter la répétition en enregistrement des propriété tout en donant comme un id
    def save(self, *args, **kwargs):
        if not self.slug:   
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return self.name    
    
    def get_absolte_url(self):
        return reverse('property:property_detail',kwargs={'slug': self.slug})
    
    '''In This methos im verifying the avalbility of rooms and all properies , so we considere that [date_from...date_to]=already reserved property .
     So , the next reservation could be done and in progess if there is no previous reservation in:date_from-date_to , else if the reservation is out date_to or upper , then the room or place or
     deal is avalaibel
    '''
    def check_avalblity(self):
        all_reservation = self.book_property.all()
        now = timezone.now().date()
        for reservation in all_reservation:
            if now > reservation.date_to:
                return 'Available'
            elif now > reservation.date_from and now < reservation.date_to:
                reserved_to = reservation.date_to
                return f'In Progress until {reserved_to}'
        else:
            return 'Available'    



    def get_avg_rating(self):
            all_reviews = self.review_property.all() #related_name from PropertyReview class its the foreign key from Property class
            all_rating = 0
            if len(all_reviews)>0:
                 for review in all_reviews:
                     all_rating += review.rate
                 return round(all_rating/len(all_reviews),2) #to get the average (moyenne of all reviews)    #round to precise how much degits after the coma
            else:
                return "_"




'''Each property has a many images in details'''
class PropertyImages(models.Model):
    property = models.ForeignKey(Property,related_name='property_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propertyimages/')

    def __str__(self):
        return str(self.image)



'''Each Property has a many places or coud be situated in a many places'''
class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')

    def __str__(self):
        return str(self.name)



'''Each Property is typed as a many categories'''
class Category(models.Model):
    name = models.CharField(max_length=40)
    icone = models.CharField(max_length=30)

    def __str__(self):
        return self.name


'''Each Property could have one or many reviews or comments'''
class PropertyReview(models.Model):
    author = models.ForeignKey(User, related_name='review_auth',on_delete=models.CASCADE)
    property = models.ForeignKey(Property,related_name='review_property',on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.property)
    

COUNT = (
    (1 , 1),
    (2 , 2),
    (3 , 3),
    (4 , 4),
)

#To reservate a property (deal)
class PropertyBook(models.Model):
    user = models.ForeignKey(User, related_name='book_owner',on_delete=models.CASCADE)    
    property = models.ForeignKey(Property,related_name='book_property',on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    guest = models.IntegerField(choices=COUNT)
    children = models.IntegerField(choices=COUNT)

    def __str__(self):
        return str(self.property)

    def in_progress(self):
        now = timezone.now().date()
        return now > self.date_from and  now < self.date_to
   
    in_progress.boolean = True



