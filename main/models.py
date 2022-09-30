from email.policy import default
from random import choices
from django.db import models


class InfoFormModel(models.Model):
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
    PHOTOGRAPHER = (
        ('')
    )
    brand_name = models.CharField(
        blank=False, null=False, max_length=500, default='')
    logo = models.CharField(choices=YES_NO, blank=False,
                            null=False, max_length=500, default='no')
    would_you_like_one_created = models.CharField(choices=YES_NO, blank=False, null=False, max_length=100, default='yes')
    what_is_the_service = models.TextField(
        blank=False, null=False, max_length=5000, default='')
    contact_number = models.BigIntegerField(blank=True, null=True, default='')
    email = models.EmailField(blank=True, null=True,
                              max_length=300, default='')
    timeframe = models.CharField(
        choices=TIMEFRAME, max_length=100, blank=False, null=False, default='')
    aim = models.TextField(blank=False, null=False,
                           max_length=5000, default='')
    products_product_images = models.CharField(
        choices=YES_NO, blank=False, max_length=500, null=False, default='')
    products_info = models.CharField(
        choices=YES_NO, blank=False, null=False, max_length=500, default='')
    pages_needed = models.CharField(
        choices=PAGES_NEEDED, blank=True, null=True, max_length=500, default='')

    def __str__(self):
        return self.brand_name
