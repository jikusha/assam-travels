class User:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.mobile = kwargs['mobile']
        self.email = kwargs['email']
        self.type = kwargs['type']
        self.password = kwargs['password']

class Bus:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.number = kwargs['number']
        self.capacity = kwargs['capacity']
        self.boarding_at = kwargs['boarding_at']
        self.destination = kwargs['destination']

class Credential:
    def __init__(self, **kwargs):
        self.email = kwargs['email']
        self.password = kwargs['password']
