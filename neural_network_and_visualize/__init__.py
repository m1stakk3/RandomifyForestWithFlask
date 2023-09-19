from neural_network_and_visualize.nn import BasicModel, DataAfterPredict
from neural_network_and_visualize.visualize import PieChart, BarChart, ExtraChart
import threading
import os


def build_charts(grouped_data):
    PieChart.build(grouped_data)
    ExtraChart.build(grouped_data)
    #BarChart.build(grouped_data)


def clean_static():
    charts = [os.path.join(os.path.abspath("./server/static"), "pie_chart.png"), os.path.join(os.path.abspath("./server/static"), "bar_chart.png")]
    for fl in charts:
        try:
            os.remove(fl)
        except FileNotFoundError:
            pass
