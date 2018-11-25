# Lines of code with the hashtag prefix are called comments.
# The computer knows to try to run them. You use them to leave notes for yourself
# so that later, you can understand what you were doing.
# This is also called documentation.

# The line below these comments are called imports statements.
# It's how you load code libraries.
# Sometimes people refer to them as libraries as "packages".
# The two terms are interchangable.
# Inside of libraries there are `modules`.  Modules are the functions.
import flask
# Code libraries let you extend the basic functionality of a programming language.
# Flask is a popular code library that makes it easy to create a webserver.
# Some extremely large sites use flask as their backend.
# For example: Pinterest is a flask app.

# When we want to use the flask library, we have to specify the module inside of
# it that we want to use, but we also have to tell python that the module in question
# is a member of that library. We do this by prefixing the module with the name
# of the library where it lives.  In this case, we are going to be only using
# two flask modules: `Flask`, and `render_template`. So, to use them, we'd need to
# write flask.Flask() and flask.render_template().

# The line below creates the app object.
# By default, it won't do anything, but as we add functions with the "@app.route"
# annotation, we can add endpoints.
# Endpoints are web page addresses that the app can serve.
# We can call the app whatever we want. It doesn't matter.
# This one is called TheBestAppEver.
# The template_folder argument tells flask.Flask where to look for our html files.
# It also doesn't matter what variable name we assign to Flask().  In this case,
# I called it `app`, but I could have called it `potatoes`, and it would work fine.
# The only difference would be that the functions below it that have the
# `@app.route` annotation would need to updated to read `@potato.route`.
app = flask.Flask("TheBestAppEver", template_folder='templates')


@app.route("/")
def serve_the_homepage():
    """
    This is the function that serves the home page html file.

    The `render_template()` function is a part of the flask library that makes it
    simple to send html files to a browser.

    All you have to is tell it the name of the file, and as long as it's in the
    template_directory that we specified earlier, it will grab it and send it
    to the user.
    """
    return flask.render_template('home.html')


@app.route("/the_other_endpoint")
def serve_the_other_page():
    """
    This is the function that serves the page that users get sent to if they
    click the button on the homepage.
    We can all the function whatever we want.  All that matters is that the
    text inside the @app.route() annotation matches the url that we write in
    the html file.
    """
    return flask.render_template('other_page.html')


@app.route("/post_request_trick")
def serve_the_post_request_page():
    """
    This is the function that serves a page with a variable.
    Flask knows that there is a variable because the .html file we are serving
    has a value inside of double curly braces: {{ value_from_the_form }}.
    You can put these anywhere in an html template.
    When you render them, you set the value that they display as an argument
    with the same name.
    So, if we wanted the variable "value_from_the_form" to be "Lobsters",
    we'd call the render_template function like this:
        flask.render_template('page_with_a_template_field.html',
                              value_from_the_form="Lobsters")

    In the case below, we are actually going to populate the the variable
    with a value we get from a post request.
    When the form on "other_page.html" is submitted, the value in the text box
    is sent to this endpoint.
    We can access the values in flask.request.args.
    Since the form field on "other_page.html" is named "form_value", thats the
    key we need to reference:
        eg: in flask.request.args['form_value']
    If we had named the field "something_very_important", we'd get the value with:
        flask.request.args['important']
    """
    return flask.render_template(
        "page_with_a_template_field.html",
        value_from_the_form=flask.request.args['form_value'])


# This line just tells python that if it's being called from the command line,
# run the application. Without it, the app wouldn't start.
app.run(port=8080)
