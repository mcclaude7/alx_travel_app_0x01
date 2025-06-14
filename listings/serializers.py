from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 'owner', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Booking
        fields = ['id', 'user', 'listing', 'check_in', 'check_out', 'guests']
