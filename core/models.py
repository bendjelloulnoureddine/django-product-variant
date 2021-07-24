from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class OptionTypes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    product = models.ForeignKey('core.Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class OptionValues(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    option = models.ForeignKey('core.OptionTypes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


# class OptionValuesVariants(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, editable=False,
#                           unique=True, primary_key=True)
#     option_value = models.ForeignKey(
#         'core.OptionValues', on_delete=models.CASCADE)


class Variants(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    options = models.ManyToManyField('core.OptionValues')
    product = models.ForeignKey('core.Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
