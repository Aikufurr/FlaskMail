from flask import Flask, request, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)


def py_mail(TO, SUBJECT, BODY):
    YOUR_EMAIL = "YOUREMAIL@gmail.com"

    # To get app password:
    # https://myaccount.google.com/security
    # Scroll to `Signing in to Google`
    # Click `App passwords`
    # Select `app` and click `Mail`
    # Select `Device` click `Other` and type `FlaskMail`
    # You'll be given a string of letters
    # paste it here without spaces:

    YOUR_APP_PASSWORD = ""

    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = YOUR_EMAIL
    MESSAGE.preamble = """Your mail reader does not support the report format."""

    HTML_BODY = MIMEText(BODY, 'html')

    MESSAGE.attach(HTML_BODY)

    server = smtplib.SMTP('smtp.gmail.com:587')

    server.starttls()
    server.login(YOUR_EMAIL, YOUR_APP_PASSWORD)
    server.sendmail(YOUR_EMAIL, TO, MESSAGE.as_string())
    server.quit()


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/send", methods=["POST"])
def send():
    py_mail(request.form['sendto'], request.form['sendsubject'], request.form['sendmessage'])
    return render_template("base.html", success=1)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
