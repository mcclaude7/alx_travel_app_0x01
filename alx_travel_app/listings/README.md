#  alx_travel_app

`alx_travel_app` is a Django-based travel listing platform that supports Listings, Bookings, and Reviews. It includes REST API support and database seeders for development and testing.

---

##  Project Structure

alx_travel_app/
├── alx_travel_app/
│ └── settings.py
├── listings/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── management/
│ └── commands/
│ └── seed.py
├── manage.py
└── requirements.txt

## Models Overview

### Listing
- title: CharField

- description: TextField

- location: CharField

- price_per_night: DecimalField

### Booking
- listing: ForeignKey to Listing

- check_in: DateField

- check_out: DateField

- guest_name: CharField

### Review
- listing: ForeignKey to Listing

- rating: IntegerField

- comment: TextField

## API Endpoints

Base URL: `/api/`

### Listings
- `GET /api/listings/`
- `POST /api/listings/`
- `GET /api/listings/<id>/`
- `PUT /api/listings/<id>/`
- `DELETE /api/listings/<id>/`

### Bookings
- `GET /api/bookings/`
- `POST /api/bookings/`
- `GET /api/bookings/<id>/`
- `PUT /api/bookings/<id>/`
- `DELETE /api/bookings/<id>/`

### Swagger
- `/swagger/` – Interactive API Docs
