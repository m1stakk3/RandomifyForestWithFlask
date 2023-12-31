# Проект для отработки

## Краткое описание

### Что заложено в программу?
Реализует классическую задачу нейронных сетей - классификацию. В программу заложен датасет с характеристиками смартфонов по категориям, обучение происходит по атрибуту "Ценовая категория".

Также для взаимодействия используется веб-интерфейс, доступный по адресу http://localhost:8999 (адрес хоста и порт можно изменить в файле server/config.py).

### Что ожидает на входе?
Датасет без поля "Ценовая категория". В момент получения датасета модель обучается, а после выдает результирующие данные - ценовые категории по характеристикам.

### Что выводит?
Для упрощения визуализации на веб-сервер выводятся построенные круговая диаграмма и экстра чарт в разбивке по категориям.

## Как пользоваться?

* вызвать терминал (CMD) в папке с проектом
* создать виртуальное окружение **python -m venv venv**
* активировать виртуальное окружение **venv\Scripts\activate (на Windows)** или ./venv/bin/activate (на Unix-подобных)
* установить требуемые библиотеки **pip install -r requirements.txt**
* запустить приложение **python run.py**
* далее запуститься веб-браузер (если в системе есть браузер по умолчанию) со страницей http://localhost:8999. Если браузер не открылся, то можно вручную в веб-браузере ввести этот адрес.
* на главной странице доступна одна единственная кнопка для загрузки файла в формате .csv, нужно нажать и выбрать файл


## Доп. информация

Создать тестовый датасет можно в папке **create_test** вызовом из консоли при активном виртуальном окружении **python test_dataset.py**
