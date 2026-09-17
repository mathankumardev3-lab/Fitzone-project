from django.contrib import admin
from .models import (
    Trainer,
    MembershipPlan,
    Service,
    Testimonial,
    GalleryImage,
    ContactMessage,
)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    search_fields = ("name", "role")


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "duration", "price", "featured")
    list_filter = ("featured",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    search_fields = ("name",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    search_fields = ("name", "role")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at", "is_read")
    list_filter = ("is_read",)
    search_fields = ("name", "phone", "email")
    readonly_fields = ("created_at",)
