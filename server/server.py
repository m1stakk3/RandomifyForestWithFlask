from server.validators import file_is_downloaded
import os
from server.config import Config
from flask import Flask, render_template, request, flash, redirect, Response
from werkzeug.exceptions import BadRequestKeyError
from neural_network_and_visualize import DataAfterPredict, build_charts, clean_static


app = Flask(__name__)       # создание экземпляра веб-сервера

app.config['UPLOAD_FOLDER'] = Config.upload_folder      # параметр папки отгрузки
app.config['SECRET_KEY'] = Config.secret_key            # параметр секретного ключа сессии (необходим для загрузки)

file_name: str = os.path.join(app.config['UPLOAD_FOLDER'], "test.csv")      # заранее установленный путь к хранилищу
upload_available: bool = True       # если True, то кнопка загрузки активна, иначе нельзя загрузить файл
new_data: None | object = None      # данные, которые были созданы на основе классификации, по умолчанию пусты
metrics: None | list = None         # метрики по итогам генерации предиктивных данных


@app.route('/', methods=['GET', 'POST'])
def index() -> Response | str:
    # получение глобальных переменных в метод
    global new_data
    global upload_available
    global metrics

    # если будет использован метод запроса POST
    if request.method == 'POST':

        # попробовать получить файл
        try:
            file = request.files['file']

            # если расширение файла .csv, то сохранить файл
            if file.filename.endswith(".csv"):
                file.save(file_name)

                # если файл успешно сохранен, то начать обучение модели, провести классификацию,
                # создать графики и получить метрики
                if file_is_downloaded(file_name):
                    flash("Файл загружен, начинаю обучение сети и выявление выбора (классификация)")
                    upload_available = False
                    new_data = DataAfterPredict(new_dataset_path=file_name)
                    new_data.go_predict()
                    build_charts(new_data.grouped_data)
                    metrics = new_data.get_metrics()
                else:
                    flash("Попробуйте загрузить файл еще раз!")
                return redirect("/")

            elif file.filename == "":
                flash("Не был выбран файл!")
            else:
                flash("Был выбран файл, отличный от .csv")

        except BadRequestKeyError:
            pass

        # при нажатии кнопки сменить файл
        try:
            request.form['change']
        except KeyError:
            pass
        else:
            clean_static()
            upload_available = True
            new_data = None
            metrics = None

    # отрисовка страницы и передача данных в шаблонизатор Jinja
    return render_template(
            'index.html',
            new_data=new_data,
            upload_available=upload_available,
            metrics=metrics
        )


@app.errorhandler(404)
def page_not_found(_):
    return redirect("/")
