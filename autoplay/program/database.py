from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def createAccountsTable():
    """Create the accounts table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            nickname VARCHAR(100),
            username VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
        )
        """
    )
def createConnection(databaseName):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Account",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    createAccountsTable()
    return True