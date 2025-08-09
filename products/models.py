from django.db import models
from django.utils.translation import gettext as _

FLAG_OPTIONS = (
    ('New', 'New'),
    ('Feature', 'Feature'),
    ('Sale', 'Sale'),
)


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Product Name"))
    subtitle = models.CharField(_("Subtitle"),max_length=500)
    skl = models.IntegerField(_("SKU"))
    desc = models.TextField(_("Description"))
    price = models.DecimalField(_("Price"))
    flag = models.BooleanField(_("Flag") ,max_length=10 , choices=FLAG_OPTIONS)
    quantity = models.IntegerField(_("Quantity"))
    brand =''
    Category = ''





class ProductImage(models.Model):
    pass

class Brand(models.Model):
    pass

class Category(models.Model):
    pass




class ProductReview(models.Model):
    pass



