from django.forms import ModelForm, CharField, TextInput, DateField, DateInput, DateTimeField, DateTimeInput
from .models import Tag, Quotes, Author

class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=25, required=True, widget=DateInput())
    born_location = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    description = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    #created_at = DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
    #                    widget=DateTimeInput(
    #                        attrs={'type': 'datetime-local'},
    #                        format='%I:%M %p %d-%b-%Y'))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']

class QuoteForm(ModelForm):

    quote = CharField(min_length=10, max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Quotes
        fields = ['quote']
        exclude = ['tags']
