from server.validators import file_is_downloaded
import os
from server.config import Config
from flask import Flask, render_template, request, flash, redirect
from werkzeug.exceptions import BadRequestKeyError
from neural_network_and_visualize import DataAfterPredict
from neural_network_and_visualize import build_charts, clean_static

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = Config.upload_folder
app.config['SECRET_KEY'] = Config.secret_key
file_name = os.path.join(app.config['UPLOAD_FOLDER'], "test.csv")
upload_available: bool = True
new_data = None
metrics = None


@app.route('/', methods=['GET', 'POST'])
def index():
    global new_data
    global upload_available
    global metrics

    if request.method == 'POST':

        try:
            file = request.files['file']

            if file.filename.endswith(".csv"):
                file.save(file_name)
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

        try:
            change = request.form['change']
        except KeyError:
            pass
        else:
            clean_static()
            upload_available = True
            new_data = None
            metrics = None

    return render_template(
            'index.html',
            new_data=new_data,
            upload_available=upload_available,
            metrics=metrics
        )

