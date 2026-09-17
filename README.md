# FitZone Gym - Django + Bootstrap Demo

A client-style gym business website built with Django and Bootstrap 5.

## Features

- Responsive Bootstrap design
- Dynamic services
- Membership plans
- Trainers
- Gallery
- Testimonials
- Contact/enquiry form
- Django admin panel
- Image uploads
- SQLite database for easy local development

## 1. Create virtual environment

Linux/macOS:

    python3 -m venv venv
    source venv/bin/activate

Windows:

    python -m venv venv
    venv\Scripts\activate

## 2. Install dependencies

    pip install -r requirements.txt

## 3. Create database

    python manage.py makemigrations
    python manage.py migrate

## 4. Create admin user

    python manage.py createsuperuser

## 5. Run server

    python manage.py runserver

Open:

    http://127.0.0.1:8000/

Admin:

    http://127.0.0.1:8000/admin/

## 6. Add content

Log in to `/admin/` and add:

- Services
- Membership Plans
- Trainers
- Testimonials
- Gallery Images

For the hero/about sections, put your own files inside:

    static/images/gym-hero.jpg
    static/images/gym-about.jpg

## Client customization

For a real gym client, change:

- Gym name
- Phone number
- WhatsApp number
- Address
- Membership prices
- Services
- Trainers
- Images
- About text
- Brand colors
- Social media links

Do not use the demo contact details for a real client.
