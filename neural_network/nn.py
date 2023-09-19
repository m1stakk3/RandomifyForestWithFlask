import os

from typing import Any

import pandas as pd
import matplotlib.pyplot as plt

from pandas.core.base import DataFrame, NDFrameT
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


class BasicModel:

    def __init__(self):
        """
            Формирование класса с размеченными данными и определение признаков (X) и целевой переменной (y)
        """
        default_model_path: str = os.path.abspath('../data/train.csv')
        self.data: DataFrame = pd.read_csv(default_model_path)

        # Разделение данных на признаки (X) и целевую переменную (y)
        self.X: DataFrame = self.data.drop('price_range', axis=1)
        self.y: DataFrame = self.data['price_range']
        self.model: [RandomForestClassifier, None] = None

    def educate(self) -> None:
        """
            Запуск процесса обучения сети. Внутри класса сохраняется модель
        """
        # Создание модели случайного леса
        self.model: RandomForestClassifier = RandomForestClassifier()

        # Обучение модели на обучающей выборке
        self.model.fit(self.X, self.y)


class DataAfterPredict(BasicModel):

    def __init__(self, new_dataset_path: str):
        """
            Класс новых данных, формируется как обычный ДатаФрейм
        :param new_dataset_path: строка с путем до данных для обучения
        """
        new_dataset: str = os.path.abspath(new_dataset_path)
        self.data: DataFrame = pd.read_csv(new_dataset)
        self.X_test: DataFrame = self.data.drop("id", axis=1)
        self.y_pred: [Any, None] = None
        self.grouped_data: [NDFrameT, None] = None

    def go_predict(self) -> None:
        """
            Предсказание на тестовой выборке
        """
        self.y_pred: Any = self.model.predict(self.X_test)
        df: DataFrame = pd.DataFrame({"id": self.data["id"], "price_group": self.y_pred})
        self.grouped_data: NDFrameT = df.groupby('price_group')['price_group'].count()

    def build_pie_chart(self):      # todo bool return
        plt.pie(self.grouped_data.values, labels=["Категория {}".format(num) for num in range(1, 5)], autopct='%1.1f%%')
        plt.title('Круговая диаграмма в разбивке по категориям стоимости')
        plt.axis('equal')
        plt.show()

    def get_metrics(self) -> str:
        """
            Оценка производительности модели
        :return: str с обозначениями
        """
        accuracy = accuracy_score(self.y[:1000], self.y_pred)
        precision = precision_score(self.y[:1000], self.y_pred, average='weighted')
        recall = recall_score(self.y[:1000], self.y_pred, average='weighted')
        f1 = f1_score(self.y[:1000], self.y_pred, average='weighted')
        result = "Точность: {}\nПогрешность: {}\nЧувствительность: {}\nF1 Score: {}".format(
            accuracy, precision, recall, f1
        )
        return result
