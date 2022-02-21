#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

# import dependencies for sql alchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import dependencies for flask
from flask import Flask, jsonify

#set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the database
Base = automap_base()
Base.prepare(engine, reflect=True)

#create variables to reference our classes
Measurement = Base.classes.measurement
Station = Base.classes.measurement

#create a session link from Python to our database
session = Session(engine)

#create a flask app
app = Flask(__name__)

#define the welcome route
@app.route("/")
def welcome():
    return(
        '''Welcome to the Climate Analysis API!\n
        Available Routes:\n
        /api/v1.0/precipitation\n
        /api/v1.0/stations\n
        /api/v1.0/tobs\n
        /api/v1.0/temp/start/end'''
    )
#create another route make sure code is aligned left
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#stations route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#monthly temperature route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#stats route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results= session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravle(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))    
    return jsonify(temps)