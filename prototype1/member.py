from datetime import datetime
from person import Person
from eventsourcing.domain.model.entity import TimestampedVersionedEntity
from eventsourcing.domain.model.decorators import attribute

class Member(TimestampedVersionedEntity):
    def __init__(self, person: Person, role: str, since=None, until=None, *args, **kwargs):
        super(Member, self).__init__(*args, **kwargs)
        self._person = person
        self._since = datetime.now() if until is None else since
        self._until = until

    @property
    def person(self):
        return self._person

    @attribute
    def since(self):
        return self._since

    @attribute
    def until(self):
        return self._until

if __name__ == "__main__":
    todd = Person.__create__(name='Todd',email='todd@earth.com')
    member = Member.__create__(person=todd, role='test')

    other = Person.__create__(name='other',email='other@earth.com')

    try:
        member.person = other
    except AttributeError as e:
        assert str(e) == 'can\'t set attribute'
    finally: 
        assert member.person is not other
