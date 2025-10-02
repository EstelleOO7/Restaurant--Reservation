# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Booking, Menu
from .models import Menu
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .forms import AssignForm




# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            messages.success(request, 'Your reservation has been submitted! We will contact you soon to confirm.')
            return redirect('book')  
    context = {'form':form}
    return render(request, 'book.html', context)




def menu(request):
    query = request.GET.get("q")  
    if query:
        menu_data = menu_data.objects.filter(name__icontains=query)
    else:
        menu_data = menu_data.objects.all()

    return render(request, "menu.html", {"menu_data": menu_data})


def menu(request):
    menu_data = Menu.objects.all()
    context = {'menu_data': menu_data}
    return render(request, 'menu.html', context) # Or use return render(request, 'menu.html', {'menu_data': menu_data})



def display_menu_item(request, pk=None): #
    if pk:
        menu_item = Menu.objects.get(pk=pk) 
    else:
        menu_item = ""

    return render(request, 'menu_item.html', {'menu_item': menu_item}) 
    

def assign_reservation(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == "POST":
        new_date = request.POST.get("assigned_date")
        if new_date:
            booking.assigned_date = new_date
            booking.save()
            messages.success(request, f"Reservation updated for {booking.first_name} {booking.last_name}")
    return redirect('reservation_dashboard')


# def assign_reservation(request, pk):
#     booking = get_object_or_404(Booking, pk=pk)

#     if request.method == 'POST':
#         form = AssignForm(request.POST)
#         if form.is_valid():
#             booking.assigned_date = form.cleaned_data['assigned_date']
#             booking.save()
#             return redirect('reservation_dashboard')  # back to the dashboard
#     else:
#         form = AssignForm(initial={'assigned_date': booking.assigned_date})

#     return render(request, 'assign_reservation.html', {
#         'form': form,
#         'booking': booking
#     })
    
    

@login_required
def reservation_dashboard(request):
    bookings = Booking.objects.all().order_by('-assigned_date')
    return render(request, 'restaurant/reservation_dashboard.html', {'bookings': bookings})

@login_required
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.reservation_active = True
    booking.save()
    return redirect('reservation_dashboard')

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.reservation_active = False
    booking.save()
    messages.success(request, f'Date assigned to {booking.first_name} {booking.last_name}')
    return redirect('reservation_dashboard')

@login_required
def assign_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.assigned_date = timezone.now()
    booking.save()
    return redirect('reservation_dashboard')



