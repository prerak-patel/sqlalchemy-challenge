# 1. import Flask
from flask import Flask
import sqlalchemy
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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

    # Create our session (link) from Python to the DB
    session = Session(engine)

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
    
    session = Session(engine)
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
    print("Query the dates and temperature observations of the most active station for the last year of data.")
    return "JSON list of temperature observations (TOBS) for the previous year."

@app.route("/api/v1.0/<start>")
def getDataByStartDate():
    print("Query the dates and temperature observations of the most active station for the last year of data.")
    return "JSON list of temperature observations (TOBS)"

@app.route("/api/v1.0/<start>/<end>")
def getDataBetweenDates():
    print("Query the dates and temperature observations of the most active station for the last year of data.")
    return "JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."

if __name__ == "__main__":
    app.run(debug=True)