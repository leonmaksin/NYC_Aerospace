import os
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from datetime import datetime
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
import time
import ssl
import helpers
import smtplib

# Configure application
app = Flask(__name__)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    response.headers["Access-Control-Allow-Credentials"] = 'true'
    response.headers["Access-Control-Allow-Methods"] =  "GET, POST, DELETE, PUT, OPTIONS"
    response.headers["access-control-allow-headers"] = "Content-Type, Authorization, Content-Length, X-Requested-With"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# TODO: Configure database connection

@app.route("/")
def index():
    """Return landing page"""
    return render_template("home.html")

@app.route("/join", methods=["GET", "POST"])
def join():
    """Return join page"""
    if request.method == "GET":
        if request.args.get("type"):
            if request.args.get("type") == "school":
                return render_template("school_join.html")
            if request.args.get("type") == "student":
                return render_template("student_join.html")
            if request.args.get("type") == "team":
                return render_template("team_join.html")
        else:
            return render_template("join_gate.html")
    elif request.method == "POST":
        if request.form.get("type"):
            if request.form.get("type") == "school":
                name = "Name: " + str(request.form.get("firstname")) + " " + str(request.form.get("lastname"))
                email = "Email: " + str(request.form.get("email"))
                school = "School: " + str(request.form.get("school"))
                location = "School Location: " + str(request.form.get("school-location"))
                tarc = "Tarc: " + str(request.form.get("tarc"))
                rocked = "RockED: " + str(request.form.get("rocked"))
                cubesat = "CubeSat: " + str(request.form.get("cubesat"))
                rocketry = "High-Power Rocketry: " + str(request.form.get("hprocketry"))
                weather_balloon = "Weather Balloon: " + str(request.form.get("weather_balloon"))
                fund = "Sponsor Interest: " + str(request.form.get("fund"))
                suggestions = "Other Projects: " + str(request.form.get("suggestions"))
                preteam = "Pre-Existing Team: " + str(request.form.get("preteam"))
                questions = "Questions/Comments: " + str(request.form.get("questions"))
                contents = name+"<br>"+email+"<br>"+school+"<br>"+location+"<br>"+tarc+"<br>"+cubesat+"<br>"+rocketry+"<br>"+weather_balloon+"<br>"+rocked+"<br>"+suggestions+"<br>"+preteam+"<br>"+fund+"<br>"+questions
                helpers.sendmail(contents, "New school join form submission", "slarbi10@stuy.edu")
                helpers.sendmail(contents, "New school join form submission", "lmaksin00@stuy.edu")
                helpers.sendmail(contents, "New school join form submission", "nycaerospace@gmail.com")
                return render_template("success.html")
            if request.form.get("type") == "student":
                name = "Name: " + str(request.form.get("firstname")) + " " + str(request.form.get("lastname"))
                email = "Email: " + str(request.form.get("email"))
                school = "School: " + str(request.form.get("school"))
                student_address = "Student Address: " + str(request.form.get("address"))
                tarc = "Tarc: " + str(request.form.get("tarc"))
                rocked = "RockED: " + str(request.form.get("rocked"))
                cubesat = "CubeSat: " + str(request.form.get("cubesat"))
                rocketry = "High-Power Rocketry: " + str(request.form.get("hprocketry"))
                weather_balloon = "Weather Balloon: " + str(request.form.get("weather_balloon"))
                suggestions = "Other Projects: " + str(request.form.get("suggestions"))
                ambassador = "Ambassador: " + str(request.form.get("ambassador"))
                school_address = "School Address: " + str(request.form.get("school_address"))
                skillset = "Skillset: " + str(request.form.get("skills"))
                comments_questions = "Comments/Questions: " + str(request.form.get("comments-questions"))
                contents=name+"<br>"+email+"<br>"+school+"<br>"+school_address+"<br>"+student_address+"<br>"+tarc+"<br>"+cubesat+"<br>"+rocketry+"<br>"+weather_balloon+"<br>"+rocked+"<br>"+suggestions+"<br>"+ambassador+"<br>"+skillset+"<br>"+comments_questions
                helpers.sendmail(contents, "New student join form submission", "slarbi10@stuy.edu")
                helpers.sendmail(contents, "New student join form submission", "lmaksin00@stuy.edu")
                helpers.sendmail(contents, "New student join form submission", "nycaerospace@gmail.com")
                return render_template("success.html")
            if request.form.get("type") == "team":
                name = "Name: " + str(request.form.get("firstname")) + " " + str(request.form.get("lastname"))
                location = "Location: " + str(request.form.get("location"))
                schools = "Schools: " + str(request.form.get("schools"))
                school_address = "School Addresses: " + str(request.form.get("school_address"))
                names = "Student Names: " + str(request.form.get("names"))
                experience = "Experience: " + str(request.form.get("expirience"))
                email = "Email: " + str(request.form.get("email"))
                tarc = "Tarc: " + str(request.form.get("tarc"))
                rocked = "RockED: " + str(request.form.get("rocked"))
                cubesat = "CubeSat: " + str(request.form.get("cubesat"))
                rocketry = "HP Rocketry: " + str(request.form.get("hprocketry"))
                weather_balloon = "Weather Balloon: " + str(request.form.get("weather_balloon"))
                ambassador = "Any Members Interested in Becoming Ambassadors: " + str(request.form.get("ambassador"))
                suggestions = "Other Projects: " + str(request.form.get("suggestions"))
                questions = "Questions/Comments: " + str(request.form.get("questions"))
                contents = name+"<br>"+email+"<br>"+location+"<br>"+schools+"<br>"+school_address+"<br>"+names+"<br>"+experience+"<br>"+tarc+"<br>"+cubesat+"<br>"+rocketry+"<br>"+weather_balloon+"<br>"+rocked+"<br>"+suggestions+"<br>"+ambassador+"<br>"+questions
                helpers.sendmail(contents, "New team join form submission", "slarbi10@stuy.edu")
                helpers.sendmail(contents, "New team join form submission", "lmaksin00@stuy.edu")
                helpers.sendmail(contents, "New team join form submission", "nycaerospace@gmail.com")
                return render_template("success.html")
        else:
            return render_template("join_gate.html")

@app.route("/rocketry")
def rocketry():
    """Return rocketry info page"""
    return render_template("rocketry.html")

@app.route("/cubesat")
def cubesat():
    """Return cubesat info page"""
    return render_template("cubesat.html")

@app.route("/iav")
def iav():
    """Return iav info page"""
    return render_template("iav.html")

@app.route("/tarc")
def tarc():
    """Return tarc info page"""
    return render_template("tarc.html")

@app.route("/electronics")
def electronics():
    """Return electronics info page"""
    return render_template("ev.html")

@app.route("/rocked")
def rocked():
    """Return RockED info page"""
    return render_template("rocked.html")

@app.route("/summer-program")
def summer_program():
    """TODO: return Summer Program info page"""
    return render_template("coming_soon.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        """return contact page"""
        return render_template("contact.html")
    elif request.method == "POST":
        name = request.form.get("firstname") + " " + request.form.get("lastname")
        email = request.form.get("email")
        message = request.form.get("message")
        contents = name+"<br>"+email+"<br>"+message
        filename = request.form.get("firstname")+"_"+request.form.get("lastname")+str(datetime.now().isoformat())+".txt"
        path = os.path.join("inquiries", filename)
        file = open(path, "w+")
        file.write(contents)
        file.close()
        helpers.sendmail(contents, "New contact form submission", "slarbi10@stuy.edu")
        helpers.sendmail(contents, "New contact form submission", "lmaksin00@stuy.edu")
        helpers.sendmail(contents, "New contact form submission", "nycaerospace@gmail.com")
        return render_template("success.html")

@app.route("/sponsor", methods=["GET", "POST"])
def sponsor():
    if request.method == "GET":
        """return sponsor page"""
        return render_template("sponsor.html")
    elif request.method == "POST":
        name = "Name: " + request.form.get("firstname") + " " + request.form.get("lastname")
        email = "Email: " + request.form.get("email")
        message = "Comments/questions: " + request.form.get("message")
        company_name = "Company Name: "+ request.form.get("c_name")
        promotion = "Promotion Requests: "+ request.form.get("promotions")
        contents = name+"<br>"+email+"<br>"+company_name+"<br>"+promotion+"<br>"+message
        filename = request.form.get("firstname")+"_"+request.form.get("lastname")+str(datetime.now().isoformat())+".txt"
        path = os.path.join("inquiries", filename)
        file = open(path, "w+")
        file.write(contents)
        file.close()
        helpers.sendmail(contents, "New sponsor form submission", "slarbi10@stuy.edu")
        helpers.sendmail(contents, "New sponsor form submission", "lmaksin00@stuy.edu")
        helpers.sendmail(contents, "New sponsor form submission", "nycaerospace@gmail.com")
        return render_template("success.html")

@app.route("/our-team")
def leadership():
    """Return leadership info page"""
    return render_template("our_team.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
