import sys

from PyQt5.QtWidgets import QApplication

from database import createConnection
from accountsgui import Window

def main():
    """Accounts main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("accounts.sqlite"):
        sys.exit(1)
        print("Error")
    # Create the main window if the connection succeeded
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()