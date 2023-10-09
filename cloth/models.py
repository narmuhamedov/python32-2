from django.db import models

class CustomerCloth(models.Model):
    name = models.CharField("Как вас зовут?", max_length=100)
    phone = models.CharField("Ваш номер", max_length=100)
    email = models.CharField("Ваш адрес почты", max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TagCl(models.Model):
    name = models.CharField("Название тега", max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField("Название товара", max_length=100)
    description = models.TextField("Характеристика товара", blank=True)
    price = models.PositiveSmallIntegerField("Напишите цену")
    tags = models.ManyToManyField(TagCl)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ("На обработке", "На обработке"),
        ("Выехал", "Выехал"),
        ("Доставлен", "Доставлен"),
    )
    customer = models.ForeignKey(CustomerCloth, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_product"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.status
