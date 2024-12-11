from django.shortcuts import render, redirect


from lexurapp.models import Contact, Otherchefs, Book, Order, GalleryPage
from lexurapp.forms import ChefsUploadForm, GalleryPageForm, BookForm, OrderForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def starter(request):
    return render(request, 'starter-page.html')

def events(request):
    return render(request, 'events.html')

def menu(request):
    return render(request, 'menu.html')

def rooms(request):
    return render(request, 'rooms.html')
def order(request):
    if request.method == 'POST':
        myorders=Order(
            name=request.POST['name'],
            email=request.POST['email'],
            menu=request.POST['menu'],
            guests=request.POST['guests'],
            conference=request.POST['conference'],
            arrival=request.POST['arrival'],
        )
        myorders.save()
        return redirect('/showorder')
    else:
        return render(request, 'orders.html')
def showorder(request):
    allorders= Order.objects.all()
    return render(request, 'showorder.html', {'order': allorders})


def editcontact(request, id):
    allcontacts= Contact.objects.get(id=id)
    return render(request, 'editcontact.html', {'contact' : allcontacts})
def editorders(request, id):
    allorders= Order.objects.get(id=id)
    return render(request, 'editorders.html', {'order' : allorders})


def book(request):
    if request.method=='POST':
        mybook=Book(
            name=request.POST['name'],
            email=request.POST['email'],
            room=request.POST['room'],
            menu=request.POST['menu'],
            arrival=request.POST['arrival'],
            departure=request.POST['departure'],
            message=request.POST['message'],
        )
        mybook.save()
        return redirect('/bookingdetails')
    else:
        return render(request,'book.html')
def bookingdetails(request):
    allbook = Book.objects.all()
    return render(request, 'bookingdetails.html', {'book': allbook})
def edit(request, id):
    editbook=Book.objects.get(id=id)
    return render(request, 'edit.html', {'book': editbook})




def showcontact(request):
    allcontact = Contact.objects.all()
    return render(request, 'showcontact.html', {'contact': allcontact})

def update(request, id):
    updateinfo = Book.objects.get(id=id)
    form=BookForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/bookingdetails')
    else:
        return render(request, 'edit.html')
def updatecontact(request, id):
    updateinfo=Order.objects.get(id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=updateinfo)
        if form.is_valid():
            form.save()
            return redirect('/showorder')
        else:
            form = OrderForm(instance=updateorders)
        return render(request, 'editorders.html', {'form': form})
def updateorders(request, id):
    updateinfo=Order.objects.get(id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=updateinfo)
        if form.is_valid():
            form.save()
            return redirect('/showorder')
        else:
            form = OrderForm(instance=updateorders)
        return render(request, 'editorders.html', {'form': form})



def contact(request):
    if request.method == 'POST':
        mycontact=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/showcontact')
    else:
        return render(request, 'contact.html')



def upload_image(request):
    if request.method == 'POST':
        form = ChefsUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/chef')
    else:
        form = ChefsUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def chef(request):
    images = Otherchefs.objects.all()
    return render(request, 'chef.html', {'images': images})
def gallery(request):
    images = GalleryPage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def update_gallery(request):
    if request.method == 'POST':
        form = GalleryPageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/gallery')
    else:
        form = GalleryPageForm()
    return render(request, 'update_gallery.html', {'form': form})


def delete(request, id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')
def delete_contact(request, id):
    contact=Contact.objects.get(id=id)
    contact.delete()
    return redirect('/showcontact')
def delete_room(request, id):
    rooms=Book.objects.get(id=id)
    rooms.delete()
    return redirect('/bookingdetails')
def delete_order(request, id):
    order=Order.objects.get(id=id)
    order.delete()
    return redirect('/showorder')

