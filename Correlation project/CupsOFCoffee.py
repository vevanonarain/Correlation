import plotly.express as px
import csv
import numpy as np

def GetDataSource(data_path):
    cups_of_coffee=[]
    hours_of_sleep=[]

    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row[" Cups of Coffee"]))
            hours_of_sleep.append(float(row["Cold drink sales"]))
    return{"x":cups_of_coffee,"y":hours_of_sleep}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation in Cups of coffee and hoursof sleep",correlation[0,1])

def setup():
    data_path="./Data/cups of coffee vs hours of sleep.csv"
    dataSoure=getDataSource(data_path)
    FindCorrelation(dataSource)
setup()
