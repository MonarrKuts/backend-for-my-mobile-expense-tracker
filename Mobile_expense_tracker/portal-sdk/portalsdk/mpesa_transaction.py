
# mpesa_integration
from portalsdk import APIContext, APIMethodType, APIRequest
import time
from notification import send_notification

from django.contrib.auth.models import User  # Import the User model


def fetch_mpesa_transactions(user):
    # Set up the API context
    api_context = APIContext(api_key='your_api_key', public_key='your_public_key', ssl=True, method_type=APIMethodType.GET, address='mpesa_api_address', port=443, path='/your_endpoint')
    
    # Add parameters, such as user identification, to the API request
    api_context.add_parameter('user_id', user.id)

    # Create an API request and execute it
    api_request = APIRequest(api_context)
    try:
        result = api_request.execute()
    except Exception as e:
        print('API call failed:', e)
        return

    # Process the API response (assuming it contains transaction data)
    transactions = result.body.get('transactions', [])
    
    # Process transactions and compare them with the user's budgets
    for transaction in transactions:
        # Compare the transaction amount with the user's budget and trigger notifications as needed
        Budget = Budget.objects.get(user=user, category=transaction['category'])
        if transaction['amount'] > Budget.amount:
            # Trigger a notification for exceeding the budget
            send_notification(User, f'You have exceeded your budget for {Budget.category}.')
        else:
            # Send a congratulatory message for staying within the budget
            (User, f'Great job! You are within your budget for {Budget.category}.')

while True:
    for user in User.objects.all():
        fetch_mpesa_transactions(user)
    time.sleep(86400)  # Fetch transactions once a day

