class User:
    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else None
        self.mobile = kwargs['mobile'] if 'mobile' in kwargs else None
        self.email = kwargs['email'] if 'email' in kwargs else None
        self.type = kwargs['type'] if 'type' in kwargs else None
        self.password = kwargs['password'] if 'password' in kwargs else None

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
