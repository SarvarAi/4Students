from django.db import models
from django.urls import reverse


# Create your models here.

class University(models.Model):
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    image = models.ImageField(upload_to='university_images/')
    short_description = models.TextField()
    university_class = models.CharField(max_length=20)
    slug = models.SlugField()
    time = models.DateTimeField(auto_now_add=True)
    official_link = models.URLField()

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('university', kwargs={'slug': self.slug})


class FAQ(models.Model):
    question = models.CharField(max_length=512)
    answer = models.TextField(max_length=1024, null=True, blank=True)
    subject = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    second_email = models.EmailField(max_length=255, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.subject


class Account(models.Model):
    profile_photo = models.ImageField(upload_to='profile_photo/', blank=True, null=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=255)
    extra_telephone_number = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField()
    email = models.EmailField()
    extra_email = models.EmailField(blank=True, null=True)
    telegram_username = models.CharField(max_length=255, blank=True, null=True)


class MainCertificates(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='m_certificates')
    ielts = models.FileField(upload_to='certificates/main_certificates', blank=True, null=True)
    toefl = models.FileField(upload_to='certificates/main_certificates', blank=True, null=True)
    cefr = models.FileField(upload_to='certificates/main_certificates', blank=True, null=True)
    sat = models.FileField(upload_to='certificates/main_certificates', blank=True, null=True)
    gmat = models.FileField(upload_to='certificates/main_certificates', blank=True, null=True)
    dtm = models.FileField(upload_to='certificates/main_certificates', blank=True, null=True)

    class Meta:
        verbose_name = 'Main Certificate'
        verbose_name_plural = 'Main Certificates'

    def __str__(self):
        return self.account.username


class ExtraCertificates(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='e_certificates')
    certificate_title = models.CharField(max_length=255)
    certificate_image = models.ImageField(upload_to='certificates/extra_certificates')
    certificate_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.account.username

    class Meta:
        verbose_name = 'Extra Certificate'
        verbose_name_plural = 'Extra Certificates'


class SchoolCertificates(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='s_certificates')
    link9 = models.URLField(blank=True, null=True)
    grade9 = models.ImageField(upload_to='certificates/school_certificates', blank=True, null=True)
    link11 = models.URLField(blank=True, null=True)
    grade11 = models.ImageField(upload_to='certificates/school_certificates', blank=True, null=True)

    def __str__(self):
        return self.account.username

    class Meta:
        verbose_name = 'School Certificate'
        verbose_name_plural = 'School Certificates'
