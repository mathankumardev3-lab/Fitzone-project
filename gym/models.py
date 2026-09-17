from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="trainers/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    features = models.TextField(help_text="One feature per line")
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["price"]

    def feature_list(self):
        return [item.strip() for item in self.features.splitlines() if item.strip()]

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=80, default="bi-lightning-charge-fill")

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title or f"Gallery image #{self.pk}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.phone}"
