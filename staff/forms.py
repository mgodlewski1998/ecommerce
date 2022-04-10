from re import L
from django.forms import ModelForm
from api.models import *
class NewProductModelForm(ModelForm):
    class Meta:
        model=Product
        fields= [
            
        ]

class OrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'email',
            'name',
            'surname',
            'address',
            'city',
            'state',
            'zip'
        ]
    def __init__(self, *args, **kwargs):
        super(OrderModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class QuantityModelForm(ModelForm):
    class Meta:
        model = ProductOrdered
        fields = ['quantity']
    def __init__(self, *args, **kwargs):
        super(QuantityModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'min': '1'
        })

class DeleteProductOrderedForm(ModelForm):

    # This form exists only because form in template for deleting 
    # a product from order would not work without {{form}} in it
    class Meta:
        model = ProductOrdered
        fields = ['quantity']
    def __init__(self, *args, **kwargs):
        super(DeleteProductOrderedForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'value': '1'
        })