from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

JOBS = ["Software Engineer", "QA Manager", "Product Manager"]

@app.route('/')
def homepage():
    """Display homepage."""

    return render_template("index.html")


@app.route('/application-form')
def application_form():
    """Display application information fields."""

    return render_template("application-form.html", jobs=JOBS)


@app.route('/application-success', methods=["POST"])
def application_success():
    """Acknowledgement and summary of application submission"""

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    salary_req = int(request.form.get("salary_req"))
    job_title = request.form.get("job_title")

    return render_template("application-response.html", first_name=first_name,
                                                        last_name=last_name, 
                                                        salary_req=salary_req,
                                                        job_title=job_title)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
