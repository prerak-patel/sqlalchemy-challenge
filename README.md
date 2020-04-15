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


