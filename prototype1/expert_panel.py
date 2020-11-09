

from eventsourcing.domain.model.aggregate import BaseAggregateRoot
from eventsourcing.domain.model.decorators import attribute
from eventsourcing.domain.model.events import DomainEvent

from member import Member
from person import Person

class ExpertPanel(BaseAggregateRoot):
    """
    An entity representing an ExpertPanel
    """

    APP_STEP_1 = 'Definition and scoping'
    APP_STEP_2 = 'Draft Specifications'
    APP_STEP_3 = 'Pilot Specifications'
    APP_STEP_4 = 'Final Approval'

    def __init__(self, name, *args, **kwargs):
        super(ExpertPanel, self).__init__(*args, **kwargs)
        self._name = name
        self._members = []
        self._application_step = self.APP_STEP_1

    @attribute
    def name(self):
        return self._name

    @property
    def members(self):
        return self._members

    @property
    def application_step(self):
        return self._application_step


    # Commands
    def add_member(self, member: Member):
        """ Add a Member to the EP """
        self.__trigger_event__(ExpertPanel.AddMemberEvent, member=member)

    def approve_definition(self):
        if self._application_step is not ExpertPanel.APP_STEP_1:
            raise ExpertPanel.ApplicationStepMismatchError()
        
        self.__trigger_event__(ExpertPanel.ApproveDefinition)

    def approve_specifications_draft(self):
        if self._application_step is not ExpertPanel.APP_STEP_2:
            raise ExpertPanel.ApplicationStepMismatchError()

        self.__trigger_event__(ExpertPanel.ApproveSpecificationsDraft)

    def approve_specifications_pilot(self):
        if self._application_step is not ExpertPanel.APP_STEP_3:
            raise ExpertPanel.ApplicationStepMismatchError()

        self.__trigger_event__(ExpertPanel.ApproveSpecificationsPilot)


    # Events
    class Event(BaseAggregateRoot.Event):
        pass

    class AddMemberEvent(Event):
        def mutate(event, expert_panel):
            expert_panel._members.append(event.member)
        
    class ApproveDefinition(Event):
        def mutate(event, expert_panel):
            expert_panel._application_step = ExpertPanel.APP_STEP_2

    class ApproveSpecificationsDraft(Event):
        def mutate(event, expert_panel):
            expert_panel._application_step = ExpertPanel.APP_STEP_3

    class ApproveSpecificationsPilot(Event):
        def mutate(event, expert_panel):
            expert_panel._application_step = ExpertPanel.APP_STEP_4

    # Exceptions
    class ApplicationStepMismatchError(Exception):
        pass

    


    