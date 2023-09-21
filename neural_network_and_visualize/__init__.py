from logger import logging
from neural_network_and_visualize.nn import BasicModel, DataAfterPredict
from neural_network_and_visualize.visualize import PieChart, BarChart, ExtraChart
import os


def build_charts(grouped_data):
    logging.info("Calling func to build graphics")
    PieChart.build(grouped_data)
    BarChart.build(grouped_data)
    ExtraChart.build(grouped_data)


def clean_static():
    logging.info("Cleaning static")
    base_part: str = os.path.abspath("./server/static")
    charts: list = [
        os.path.join(base_part, "pie_chart.png"),
        os.path.join(base_part, "extra_chart.png"),
        os.path.join(base_part, "bar_chart.png")
    ]
    for fl in charts:
        try:
            os.remove(fl)
        except FileNotFoundError:
            pass
