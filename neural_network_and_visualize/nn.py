from logger import logging
import os
from typing import Any
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


class BasicModel:

    def __init__(self):
        """
            Формирование класса с размеченными данными и определение признаков (X) и целевой переменной (y)
        """
        default_model_path: str = os.path.abspath('./data/train.csv')
        self.data = pd.read_csv(default_model_path)

        # Разделение данных на признаки (X) и целевую переменную (y)
        self.X = self.data.drop('price_range', axis=1)
        self.y = self.data['price_range']
        self.model: [RandomForestClassifier, None] = None
        logging.info("Created Basic Model")

    def educate(self) -> RandomForestClassifier:
        """
            Запуск процесса обучения сети. Внутри класса сохраняется модель
        """
        # Создание модели случайного леса
        self.model: RandomForestClassifier = RandomForestClassifier()

        # Обучение модели на обучающей выборке
        self.model.fit(self.X, self.y)
        logging.info("Model successfully educated on data")
        return self.model


class DataAfterPredict:

    def __init__(self, new_dataset_path: str):
        """
            Класс новых данных, формируется как обычный ДатаФрейм
        :param new_dataset_path: строка с путем до данных для обучения
        """
        logging.info("Init DataAfterPredict object")
        self.basic_model = BasicModel()
        new_dataset: str = os.path.abspath(new_dataset_path)
        self.data = pd.read_csv(new_dataset)
        self.X_test = self.data.drop("id", axis=1)
        self.model: RandomForestClassifier = self.basic_model.educate()
        self.y_pred: [Any, None] = None
        self.grouped_data = None

    def go_predict(self) -> None:
        """
            Предсказание на тестовой выборке
        """
        logging.info("Predict launch")
        self.y_pred: Any = self.model.predict(self.X_test)
        df = pd.DataFrame({"id": self.data["id"], "price_group": self.y_pred})
        self.grouped_data = df.groupby('price_group')['price_group'].count()

    def get_metrics(self) -> list:
        """
            Оценка производительности модели
        :return: str с обозначениями
        """
        accuracy = accuracy_score(self.basic_model.y[:1000], self.y_pred)
        precision = precision_score(self.basic_model.y[:1000], self.y_pred, average='weighted')
        recall = recall_score(self.basic_model.y[:1000], self.y_pred, average='weighted')
        f1 = f1_score(self.basic_model.y[:1000], self.y_pred, average='weighted')
        result = [f"Точность: {accuracy}", f"Погрешность: {precision}", f"Чувствительность: {recall}", f"F1 Score: {f1}"]
        logging.info("%s", result)
        return result
