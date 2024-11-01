class Handler:
    """Abstract Handler"""

    def __init__(self, successor):
        self._successor = successor
        # define who is the next handler

    def handle(self, request):
        handled = self._handle(request)
        # if handled, stop here
        if not handled:
            # otherwise, keep going
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass!")


class ConcreteHandler1(Handler):
    """Concrete handler 1"""

    def _handle(self, request):
        # provide a condition for handling
        if 0 < request <= 10:
            print(f"Request {request} handled in handler 1")
            return True


class DefaultHandler(Handler):
    """Default handler"""

    def _handle(self, request):
        """If there is no more handler available"""
        print(f"End of chain, no handler for {request}")
        return True


class Client:
    # using handlers
    def __init__(self):
        # create handlers and use them in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler(None))
        # default handler has no successor

    # Send your requests one at a time for handlers to handle
    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


# create a client
c = Client()

# create requests
requests = [2, 5, 30]

# send the requests
c.delegate(requests)
