from django import forms
from lexurapp.models import Otherchefs, Book, Contact,Order,GalleryPage


class ChefsUploadForm(forms.ModelForm):
    class Meta:
        model = Otherchefs
        fields = '__all__'
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
class GalleryPageForm(forms.ModelForm):
    class Meta:
        model = GalleryPage
        fields = '__all__'








