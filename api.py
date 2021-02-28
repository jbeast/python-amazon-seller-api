# Import datetime and timedelta from python's datetime module
# https://docs.python.org/3/library/datetime.html
from datetime import datetime, timedelta

# Import the Orders class from python-amazon-sp-api
from sp_api.api import Orders
from sp_api.base import SellingApiException, Marketplaces

# Fill in credential info here
credentials = dict(
    refresh_token='',
    lwa_app_id='',
    lwa_client_secret='',
    aws_secret_key='',
    aws_access_key='',
    role_arn='',
)

try:
    # Get orders created after 1 day ago
    res = Orders(credentials=credentials, marketplace=Marketplaces.GB).get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=1)).isoformat())
    print(res)

# If something goes wrong, print out the exception
except SellingApiException as ex:
    print(ex)
