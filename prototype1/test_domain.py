from expert_panel import ExpertPanel
from person import Person
from member import Member
from eventsourcing.domain.model.aggregate import BaseAggregateRoot
from eventsourcing.domain.model.events import subscribe
import pytest

def test_ExpertPanel_isinstance_of_BaseAggregateRoot():
    ep = ExpertPanel.__create__(name='test')
    assert isinstance(ep, BaseAggregateRoot)

def test_ExpertPanel_instance_has_id():
    ep = ExpertPanel.__create__(name="test")
    assert ep.id != None

def test_init_sets_expert_panel_name():
    ep = ExpertPanel.__create__(name="test panel")
    assert ep.name == 'test panel'

def test_can_update_pane_name():
    evts = []
    ep = ExpertPanel.__create__(name="test panel")
    ep.name = 'Test Panel 2'
    assert ep.name == 'Test Panel 2'

def test_can_add_a_member_to_an_expert():
    ep = ExpertPanel.__create__(name="panel")
    person = Person.__create__(name="tj ward", email="jward3@email.unc.edu")
    ep.add_member(Member.__create__(person=person, role='programmer'))

    assert len(ep.members) == 1

def test_raises_exception_when_trying_mark_ep_definition_approve_and_not_in_step_1():
    ep = ExpertPanel.__create__(name="beans")
    ep._application_step = ExpertPanel.APP_STEP_2
    with pytest.raises(ExpertPanel.ApplicationStepMismatchError):
        ep.approve_definition()

def test_sets_application_step_to_step_2():
    ep = ExpertPanel.__create__(name='test')
    ep.approve_definition()

    assert ep._application_step == ExpertPanel.APP_STEP_2

def test_raises_exception_when_trying_mark_spec_draft_approved_and_not_in_step_1():
    ep = ExpertPanel.__create__(name="beans")
    ep._application_step = ExpertPanel.APP_STEP_1
    with pytest.raises(ExpertPanel.ApplicationStepMismatchError):
        ep.approve_specifications_draft()

def test_sets_application_step_to_step_3():
    ep = ExpertPanel.__create__(name='test')
    ep._application_step = ExpertPanel.APP_STEP_2
    ep.approve_specifications_draft()

    assert ep.application_step == ExpertPanel.APP_STEP_3

def test_raises_exception_when_trying_mark_spec_draft_approved_and_not_in_step_1():
    ep = ExpertPanel.__create__(name="beans")
    ep._application_step = ExpertPanel.APP_STEP_1
    with pytest.raises(ExpertPanel.ApplicationStepMismatchError):
        ep.approve_specifications_pilot()

def test_sets_application_step_to_step_4():
    ep = ExpertPanel.__create__(name='test')
    ep._application_step = ExpertPanel.APP_STEP_3
    ep.approve_specifications_pilot()

    assert ep.application_step == ExpertPanel.APP_STEP_4
