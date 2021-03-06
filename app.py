# 1. import Flask
from flask import Flask
import sqlalchemy
import numpy as np
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# Create our session (link) from Python to the DB
session = scoped_session(sessionmaker(engine))

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    return(f"Welcome to Climate App!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
)
    

@app.route("/api/v1.0/precipitation")
def getPrecipitationByDate():

    results = session.query(Measurement.date,Measurement.prcp).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    measurement_by_date = []
    for date, prcp in results:
        measurement = {}
        measurement["date"] = date
        measurement["prcp"] = prcp
        measurement_by_date.append(measurement)

    return jsonify(measurement_by_date)

@app.route("/api/v1.0/stations")
def getListOfStations():
    
    # session = Session(engine)
    results = (session
                .query(Station.station)
                .all()
            )
    session.close();

    # Convert list of tuples into normal list
    stations = list(np.ravel(results))

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def getMostActiveStationOfLastYear():

    # Get last date of the dataset
    for row in session.query(Measurement).order_by(Measurement.date.desc()).limit(1):
        max_date = dt.datetime.strptime(row.date,'%Y-%m-%d')

    # Calculate year before date
    year_before_max_date = max_date - dt.timedelta(12*366/12)

    # Query temperature observations of last year
    results = (session
                .query(Measurement.date, Measurement.prcp)
                .filter(Measurement.date > year_before_max_date).all())

    session.close();
    
    # Convert list of tuples into normal list
    most_active_stations_last_year = list(np.ravel(results))
    
    return jsonify(most_active_stations_last_year)

@app.route("/api/v1.0/<start>")
def getDataByStartDate(start):

    results = (session
                .query(func.max(Measurement.tobs).label('TMAX'),func.avg(Measurement.tobs).label('TAVG'),func.min(Measurement.tobs).label('TMIN'))
                .filter(Measurement.date == start)
            ).all()

    session.close();

    aggregate_data = []
    for TMAX, TAVG, TMIN in results:
        key_val = {}
        key_val["Max Temp"] = TMAX
        key_val["AVG Temp"] = TAVG
        key_val["MIN Temp"] = TMIN
        aggregate_data.append(key_val)

    return jsonify(aggregate_data)


@app.route("/api/v1.0/<start>/<end>")
def getDataBetweenDates(start,end):

    results = (session
                .query(func.max(Measurement.tobs).label('TMAX'),func.avg(Measurement.tobs).label('TAVG'),func.min(Measurement.tobs).label('TMIN'))
                .filter(Measurement.date >= start)
                .filter(Measurement.date <= end)
            ).all()

    session.close();

    aggregate_data = []

    for TMAX, TAVG, TMIN in results:
        key_val = {}
        key_val["Max Temp"] = TMAX
        key_val["AVG Temp"] = TAVG
        key_val["MIN Temp"] = TMIN
        aggregate_data.append(key_val)

    return jsonify(aggregate_data)

if __name__ == "__main__":
    app.run(debug=True)