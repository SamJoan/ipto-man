import stem
from stem.connection import connect

# https://stem.torproject.org/faq.html#how-do-i-request-a-new-identity-from-tor
def conn():
    controller = connect()
    controller.authenticate()
    return controller
