from behave import *
from AreTheySame import feature

@given('')
def given_impl(context):
    pass

@when('')
def when_impl(context):
    assert (main("") is True)

@then('')
def then_impl(context):
