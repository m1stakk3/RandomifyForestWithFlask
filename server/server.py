from flask import Flask, render_template, request, flash

app = Flask(__name__)


# Определение маршрута для загрузки файла
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if not file.filename.endswith(".csv"):
            flash("Загружаемый файл не в формате .csv")
        # Обработка загруженного файла и передача его в модель для классификации
        prediction = model.predict(file)
        return render_template('result.html', prediction=prediction)
    return render_template('upload.html')
