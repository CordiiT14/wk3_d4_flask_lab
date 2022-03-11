from flask import render_template, request 
from app import app
from models.events_list import event_list, add_new_event
from models.event import Event 

@app.route('/events')
def index():
    return render_template('index.html', title="Home", event_list=event_list)

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['event_name']
    date = request.form['date']
    room_location = request.form['room_location']
    number_guests = request.form['number_guests']
    description = request.form['description']
    recurring = request.form['recurring']
    new_event = Event(date, event_name, number_guests, room_location, description, recurring)
    add_new_event(new_event)
    print(recurring)
    return render_template('index.html', title="Home", event_list=event_list)
