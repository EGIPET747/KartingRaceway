import logging

import alembic.command
import fire

logger = logging.getLogger("manager")
logger.setLevel(logging.INFO)


class __CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    purple = "\x1b[35;21m"
    blue = "\x1b[34;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    template = "%(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: purple + template + reset,
        logging.INFO: blue + template + reset,
        logging.WARNING: yellow + template + reset,
        logging.ERROR: red + template + reset,
        logging.CRITICAL: bold_red + template + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


handler = logging.StreamHandler()
handler.setFormatter(__CustomFormatter())
logger.addHandler(handler)


class Manager:
    """Project manager"""

    def make_migration(self, message: str = "migration"):
        """Создание автоматической миграции с сообщением"""
        from backend.settings import configuration

        logger.info("Make migration message: %s", message)
        alembic.command.revision(autogenerate=True, message=message, config=configuration.ALEMBIC_CFG)
        logger.info("Done")

    def upgrade_database(self):
        """Применение миграций БД"""
        from backend.settings import configuration

        logger.info("Upgrade db to heads")
        alembic.command.upgrade(revision="heads", config=configuration.ALEMBIC_CFG)
        logger.info("Upgrade db to heads completed")

    def downgrade_database(self, revision: str = "-1"):
        """Откат миграции БД до ревизии или на -1"""
        from backend.settings import configuration

        logger.info("Downgrade db to revision: %s", revision)
        alembic.command.downgrade(revision=revision, config=configuration.ALEMBIC_CFG)
        logger.info("Downgrade db to revision %s completed", revision)

    def magic(self):
        """Правит код по ruff"""

        # TODO: ruff
        logger.info("MAGIC START")
    
        pass

        logger.info("MAGIC DONE")

    def runserver(self, host: str = "127.0.0.1", port: int = 8000):
        """Запуск сервера в режиме WORKING_MODE из .env"""
        import uvicorn

        logger.info("SERVER RUN WITH %s:%s", host, port)

        parameters = {
            "host": host,
            "port": port,
        }
        # Если режим работы не продовский, то добавим удобные фичи для работы
        pass

        # Запускаемся
        uvicorn.run("backend.main:app", **parameters)


if __name__ == "__main__":
    fire.Fire(Manager)
