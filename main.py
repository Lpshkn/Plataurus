from app import app

from plataurus.utils.variables import get_env_value
from app.constants import FLASK_HOSTNAME, FLASK_PORT


if __name__ == '__main__':
    hostname = get_env_value('FLASK_HOSTNAME', FLASK_HOSTNAME)
    port = get_env_value('FLASK_PORT', FLASK_PORT)

    app.run(host=hostname, port=port)
