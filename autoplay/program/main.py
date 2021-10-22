import sys

from PyQt5.QtWidgets import QApplication

from database import createConnection
from accountsgui import Window

def main():
    """This program allows users to store their accounts on a local database and
    automatically log into their accounts, navigate the league client,
     queue for a game, and accept the queue."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("accounts.sqlite"):
        sys.exit(1)

    # Create the main window if the connection succeeded
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()