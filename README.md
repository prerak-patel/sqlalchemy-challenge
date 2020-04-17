# sqlalchemy-challenge
Using SQLAlchemy ORM queries, Pandas and Matplotlib to do basic climate analysis and data exploration of hawaii climate database.

## Prerequisites

### Install dependencies below
* [pandas](https://pandas.pydata.org)
* [Matplotlib](https://matplotlib.org)
* [Jupyter Notebook](https://jupyter.org/install)
* [numpy](https://numpy.org) 
* [SciPy](https://www.scipy.org/install.html)
* [SQLAlchemy](https://pypi.org/project/SQLAlchemy)
* [Flask](https://pypi.org/project/Flask)

## Precipitation and Station Analysis using SQLAlchemy, Pandas and Matplotlib

### Setup

```
git clone https://github.com/prerak-patel/sqlalchemy-challenge.git
cd sqlalchemy-challenge
jupyter notebook
```

### Execution - Precipitation and Station Analysis

* Click and Run the climate-analysis.ipynb

### Precipitation Analysis

* No seasonal impact on precipitation can be observed on analysis of daily precipitation over last year.

![](Images/precipitation.png)

### Station Analysis
* USC00519281 recorded highest temperature observations (2772).
* Tropical but moderate temperatures observed over the year
  * Average temperature - 71.66 degrees
  * Highest temperatures - 85 degrees
  * Lowest temperatures - 54 degrees

![](Images/station-histogram.png)

## Climate App - A Flask API to perform above analysis.

```
cd sqlalchemy-challenge
python app.py
```

### Endpoints 
* 127.0.0.1:5000/api/v1.0/precipitation - Returns percipitation data for a given date.
* 127.0.0.1:5000/api/v1.0/stations - Returns list on stations under observation.
* 127.0.0.1:5000/api/v1.0/tobs - Returns most precipitation data of most active station in Hawaii.
* 127.0.0.1:5000/api/v1.0/start/end - Returns precipitation data in a particular date range.
