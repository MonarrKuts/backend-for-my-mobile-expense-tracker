from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Mobile_expense_tracker.views import ExpenseViewSet, CustomTokenObtainPairView, UserRegistrationView, UserLogoutView, PasswordResetView, ReportUpdateView, ReportDeleteView, ExpenseDetailView, set_budget, generate_pie_chart, create_report

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Token-related views
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', UserRegistrationView.as_view(), name='user_registration'),
    path('api/logout/', UserLogoutView.as_view(), name='user_logout'),
    path('api/password-reset/', PasswordResetView.as_view(), name='password_reset'),

    # Report-related views
    path('create_report/', create_report, name='create_report'),
    path('update_report/<int:pk>/', ReportUpdateView.as_view(), name='update_report'),
    path('reports/<int:pk>/delete/', ReportDeleteView.as_view(), name='delete_report'),

    # Expense-related views
    path('expense/<int:pk>/', ExpenseDetailView.as_view(), name='expense_detail'),

    # Other views
    path('set_budget/', set_budget, name='set_budget'),
    path('generate_pie_chart/', generate_pie_chart, name='generate_pie_chart'),
]

