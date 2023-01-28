
from django.db import models
from django.conf import settings


# Create your models here.

class Cause(models.Model):
    name = models.CharField(max_length=255)
    goal_amount = models.DecimalField(default=0, max_digits=100, decimal_places=2)
    raised_amount = models.DecimalField(default=0, max_digits=100, decimal_places=2, null=True, blank=True)

    image = models.ImageField(upload_to='donation/Cause/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'Causes'
        ordering = ['-id', ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class CauseContent(models.Model):
    cause = models.ForeignKey(Cause, on_delete=models.PROTECT, related_name='cause_contents')
    name = models.TextField()
    value = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'CauseContents'
        ordering = ['-id', ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class CauseContentImage(models.Model):
    cause = models.ForeignKey(Cause, on_delete=models.PROTECT, related_name='cause_content_images')
    head = models.CharField(max_length=500)
    image = models.ImageField(upload_to='donation/CauseContentImage/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'CauseContentImages'
        ordering = ('-id',)

    def __str__(self):
        return self.head

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'PaymentMethods'
        ordering = ('-id',)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.name = self.name.replace(' ', '_').lower()
        super().save(*args, **kwargs)


class PaymentMethodDetail(models.Model):
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.RESTRICT)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)

    card_number = models.CharField(max_length=50, null=True, blank=True)
    card_holder = models.CharField(max_length=50, null=True, blank=True)
    cvc_code = models.CharField(max_length=20, null=True, blank=True)
    expiry_date = models.CharField(max_length=20, null=True, blank=True)

    email = models.EmailField()

    bkash = models.CharField(max_length=15, null=True, blank=True)
    rocket = models.CharField(max_length=15, null=True, blank=True)
    nagad = models.CharField(max_length=15, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'PaymentMethodDetails'
        ordering = ('-id',)

    def __str__(self):
        return str(self.payment_method)


class Donation(models.Model):
    cause = models.ForeignKey(Cause, on_delete=models.PROTECT, null=True, blank=True)
    amount = models.DecimalField(max_digits=255, decimal_places=2)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'Donations'
        ordering = ('-id',)

    def __str__(self):
        return self.email + ': ' + str(self.amount)


class MonthlySubscription(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.PROTECT, related_name='member_subscriptions')
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    subscription_date = models.DateTimeField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="+", null=True,
                                   blank=True)

    class Meta:
        verbose_name_plural = 'MonthlySubscriptions'
        ordering = ('-id',)

    def __str__(self):
        return str(self.id)
