from account_service.domain.account import Account
from account_service.domain.errors import CustomerNotFound


def get_account(account_number, account_repository):
    return account_repository.fetch_by_account_number(account_number)


def create_account(customer_id, account_repository, customer_client):
    if not customer_client.has_customer_with_id(customer_id):
        raise CustomerNotFound()

    account = Account(customer_id=customer_id, account_status='active')

    account_repository.store(account)

    return account.formatted_account_number
