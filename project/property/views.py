from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView , CreateView
from .models import Property
from django.views.generic.edit import FormMixin
from .forms import PropertyBookForm
from .filters import PropertyFilter
from django_filters.views import FilterView


# Create your views here.

class PropertyList(FilterView):
    model = Property
    paginate_by = 3
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'
    ordering = ['name'] 

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('name')
    
    

class PropertyDetail(FormMixin,DetailView):
    model = Property
    form_class = PropertyBookForm

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:1]
        return context'''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_property = self.get_object()
        context["related"] = Property.objects.filter(category=current_property.category).exclude(id=current_property.id)[:4]
        context["current_category"] = current_property.category
        return context
    
    def post(self,request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.property = self.get_object()
            myForm.user = request.user
            myForm.save()
            return redirect('/')
        else:
            print('Not valid')


class AddListing(CreateView):
    pass