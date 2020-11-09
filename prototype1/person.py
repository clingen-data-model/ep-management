from eventsourcing.domain.model.entity import TimestampedVersionedEntity

class Person(TimestampedVersionedEntity):
    def __init__(self, name: str, email: str, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        self.name = name
        self.email = email
