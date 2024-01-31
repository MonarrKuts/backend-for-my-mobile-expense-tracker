from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserSpendingCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_spending_category')
    name = models.CharField(max_length=100)
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_expense')
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(UserSpendingCategory, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    receipt = receipt = models.TextField(blank=True, null=True)
    description = models.TextField()
   
    def __str__(self):
        return self.name
    

    
    



class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_budget')
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    # Add other fields if needed


class Reports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reports')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_reports')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transactions')
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)