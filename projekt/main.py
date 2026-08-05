from src.ui import WarehouseUI
from sqlalchemy import create_engine, text
from data.config import database_url


if __name__ == "__main__":
    app = WarehouseUI()
    app.mainloop()
