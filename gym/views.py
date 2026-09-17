from django.contrib import messages
from django.shortcuts import redirect, render

from .models import (
    ContactMessage,
    GalleryImage,
    MembershipPlan,
    Service,
    Testimonial,
    Trainer,
)


def home(request):
    context = {
        "trainers": Trainer.objects.all(),
        "plans": MembershipPlan.objects.all(),
        "services": Service.objects.all(),
        "testimonials": Testimonial.objects.all(),
        "gallery": GalleryImage.objects.all()[:6],
    }
    return render(request, "gym/home.html", context)


def contact(request):
    if request.method != "POST":
        return redirect("home")

    name = request.POST.get("name", "").strip()
    phone = request.POST.get("phone", "").strip()
    email = request.POST.get("email", "").strip()
    message = request.POST.get("message", "").strip()

    if not name or not phone or not message:
        messages.error(request, "Please fill in your name, phone and message.")
        return redirect("home")

    ContactMessage.objects.create(
        name=name,
        phone=phone,
        email=email,
        message=message,
    )

    messages.success(request, "Thanks! Your enquiry has been received.")
    return redirect("home")
