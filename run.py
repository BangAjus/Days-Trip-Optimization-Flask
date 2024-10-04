from apps.main import app, port
import config

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=port,
            debug=config.DEBUG)