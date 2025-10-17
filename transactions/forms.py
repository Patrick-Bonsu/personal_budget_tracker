from django import forms
from .models import Transaction, Category

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'transaction_type', 'category', 'description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
