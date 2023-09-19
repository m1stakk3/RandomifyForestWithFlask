from server import app
from server.config import Config
from logger import logging
import webbrowser


if __name__ == "__main__":
    logging.info("Launching web server")
    app.run(host=Config.ip, port=Config.port, debug=True)
    webbrowser.open(f"http://{Config.ip}:{Config.port}/")
