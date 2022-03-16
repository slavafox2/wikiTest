from behave import given, when, then


@given('Tap on search screen')
def tap_search(context):
    context.app.first_setting_page.skip_button()
    context.app.main_page.tap_search()


@when('Enter {search_phrase} into a search field')
# @when(u'Enter python into a search field')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When Enter python into a search field')
def input_search(context, search_phrase):
    context.app.search_page.input_search(search_phrase)


@then('Top result {search_phrase} is shown')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Top result is shown')
def verify_search_result(context, search_phrase):
    context.app.search_page.verify_search_result(search_phrase)


@then("'{search_phrase}' is shown")
def verify_search_result_empty(context, search_phrase):
    context.app.search_page.verify_search_result_empty(search_phrase)