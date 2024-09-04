from alembic.config import Config as AlembicConfig

from backend.settings.database import DB_URL

TITLE = "KRW"
TITLE_FULL = "Karting Raceway"
VERSION = "0.0.1"

ALEMBIC_CFG = AlembicConfig("alembic.ini")
ALEMBIC_CFG.set_main_option("sqlalchemy.url", DB_URL)
