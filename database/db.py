from pathlib import Path

from PySide6.QtCore import QStandardPaths
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models.account import Base


def get_db_path() -> Path:
    app_data_dir = QStandardPaths.writableLocation(
        QStandardPaths.StandardLocation.AppDataLocation
    )
    app_folder = Path(app_data_dir) / "ApexFinance"
    app_folder.mkdir(parents=True, exist_ok=True)
    return app_folder / "apex.db"


engine = create_engine(f"sqlite:///{get_db_path()}")
Base.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
