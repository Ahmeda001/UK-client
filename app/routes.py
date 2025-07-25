from flask import Blueprint, render_template, request, redirect, flash
from .scraper import check_slots
from .extensions import mail
from flask_mail import Message

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        license_number = request.form['license']
        booking_ref = request.form['booking']
        email = request.form['email']

        available = check_slots(license_number, booking_ref)

        if available:
            msg = Message('DVSA Slot Available!',
                          sender='your_email@gmail.com',
                          recipients=[email])
            msg.body = 'A new driving test slot is available. Visit DVSA to book now.'
            mail.send(msg)
            flash('Slot found and email sent!')
        else:
            flash('No earlier slots found at this time.')

        return redirect('/')

    return render_template('index.html')
