# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


@app.route("/api/v1.0/precipitation")
def getPrecipitationByDate():
    print("Convert the query results to a dictionary using date as the key and prcp as the value.")
    return "JSON representation of your dictionary"

@app.route("/api/v1.0/stations")
def getListOfStations():
    return "JSON list of stations from the dataset."

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