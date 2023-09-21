from logger import logging
import os
import matplotlib.pyplot as plt

plt.switch_backend('agg')
save_path: str = os.path.abspath("./server/static")


class PieChart:

    @staticmethod
    def build(grouped_data) -> None:
        logging.info("Building Pie Chart")
        print(grouped_data.values)
        plt.pie(grouped_data.values, labels=["Категория {}".format(num) for num in range(1, len(grouped_data.values) + 1)], autopct='%1.1f%%')
        plt.title('Круговая диаграмма в разбивке по категориям стоимости')
        plt.axis('equal')
        plt.savefig(fname=os.path.join(save_path, "pie_chart.png"), format="png")
        plt.close('all')
        return


class BarChart:

    @staticmethod
    def build(grouped_data) -> None:
        logging.info("Building Bar Chart")
        plt.plot(grouped_data.index, grouped_data.values)
        plt.xlabel('Количество')
        plt.ylabel('Номер категории')
        plt.title('График множественного выбора в разбивке по категориям стоимости')
        plt.savefig(fname=os.path.join(save_path, "bar_chart.png"), format="png")
        plt.close('all')
        return


class ExtraChart:

    @staticmethod
    def build(groupped_data) -> None:
        logging.info("Building Extra Chart")
        plt.figure()
        groupped_data.plot()
        plt.legend(loc='best')
        plt.savefig(fname=os.path.join(save_path, "extra_chart.png"), format="png")
        plt.close('all')
        return
