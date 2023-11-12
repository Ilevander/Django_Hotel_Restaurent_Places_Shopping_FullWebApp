from django.shortcuts import render
from property.models import Property,Place,Category
from django.db.models.query_utils import Q  
from django.db.models import Count
from blog.models import Post
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    category = Category.objects.all()

    #Rendring and tiltering the categories from all properties into html template
    restaurant_list = Property.objects.filter(category__name='Restaurant')[:5]#Rendring 5 restaurents
    hotels_list = Property.objects.filter(category__name='Hotel')[:4] #Rendring 4 hotels
    place_list = Property.objects.filter(category__name='Places')[:4] #Rendring 4 places

    recent_posts = Post.objects.all()[:4]#Posting 4 posts

    #Rendering and filtering and counting categories from properties to Show statistics of data onto html template
    users_count = User.objects.all().count()
    places_count  = Property.objects.filter(category__name='Places').count()
    restaurant_count = Property.objects.filter(category__name='Restaurant').count()
    hotels_count = Property.objects.filter(category__name='Hotel').count()

    return render(request, 'settings/home.html',{
        'places' : places,
        'category' : category,
        'restaurant_list': restaurant_list,
        'hotels_list' : hotels_list ,
        'place_list' : place_list,
        'recent_posts' : recent_posts,
        'users_count' : users_count,
        'places_count' : places_count,
        'restaurant_count' : restaurant_count,
        'hotels_count' : hotels_count,
    })




def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    property_list = Property.objects.filter(
        Q(name__icontains= name ) &
        Q(place__name__icontains = place)
    )

    return render(request, 'settings/home_search.html',{'property_list' : property_list}) 


def category_filter(request, category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category=category)
    return render(request, 'settings/home_search.html',{'property_list' : property_list}) 


def contact_us(request):
    if request.method == "POST":
        message_name = request.POST.get('message-name', '')
        message_email = request.POST.get('message-email', '')
        message_subject = request.POST.get('message-subject', '')
        message_content = request.POST.get('message', '')

        # Send mail:
        subject = f'Contact Form - {message_subject}'
        message = f'Name: {message_name}\nEmail: {message_email}\n\n{message_content}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]  # Change this to your recipient email address

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False
        )

        return render(request, 'settings/contact.html', {})
    else:
        return render(request, 'settings/contact.html', {})