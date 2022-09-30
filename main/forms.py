from socket import fromshare
from django import forms
from .models import InfoFormModel


class InfoForm(forms.ModelForm):
    YES_NO = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    TIMEFRAME = (
        ('1_weeks', '1 Week'),
        ('2_weeks', '2 Weeks'),
        ('3_weeks', '3 Weeks'),
        ('4_weeks_plus', '4 Weeks+'),
    )
    PAGES_NEEDED = (
        ('about_page', 'About Page'),
        ('contact_page', 'Contact Page'),
        ('blog_page', 'Blog Page'),
        ('map_page', 'Map Page'),
        ('ecommerce_page', 'Ecommerce Page'),
    )
    brand_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Business/Brand Name?'}))
    logo = forms.CharField(label='Do you have a logo?', widget=forms.RadioSelect(choices=YES_NO))
    would_you_like_one_created = forms.CharField(label='Would you like one created?', widget=forms.RadioSelect(choices=YES_NO))
    what_is_the_service = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder' : 'What service are you providing?'}))
    contact_number = forms.CharField(label='', widget=forms.NumberInput(attrs={'placeholder' : 'Contact number'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder' : 'Email address'}))
    timeframe = forms.CharField(label='When do you need this project complete?', widget=forms.RadioSelect(choices=TIMEFRAME))
    aim  = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder' : 'What will be the aim for your website?'}))
    products_product_images = forms.CharField(label='Do you have any product images?', widget=forms.RadioSelect(choices=YES_NO))
    products_info = forms.CharField(label='Do you have product info (eg, product names, pricing, descriptions etc.)?', widget=forms.RadioSelect(choices=YES_NO))
    pages_needed = forms.CharField(label="Select which pages you'll need?", widget=forms.RadioSelect(choices=PAGES_NEEDED))


    class Meta:
        model = InfoFormModel
        fields = (
            'brand_name',
            'would_you_like_one_created',
            'logo',
            'what_is_the_service',
            'contact_number',
            'email',
            'timeframe',
            'aim',
            'products_product_images',
            'products_info',
            'pages_needed',
        )

