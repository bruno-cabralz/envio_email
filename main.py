from controllers.email import Email
from controllers.config import Config


def start():
    config = Config.get_config()
    email = Email(config['email']['destinatarios'],
                  config['email']['usuario'], config['email']['senha'])
    email.enviar_email()


if __name__ == '__main__':
    start()
