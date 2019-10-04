from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# create the application
app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# create the icon
icon = QIcon("icon.png")

# create the tray icon 
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# this will print a message 
def print_msg():
 print("This action is triggered connect!")

# create the menu for tray icon
menu = QMenu()

# add one item to menu 
action = QAction("This is menu item")
menu.addAction(action)
action.triggered.connect(print_msg)

# add exit item to menu 
exitAction = QAction("&Exit")
menu.addAction(exitAction)
exitAction.triggered.connect(exit)

# add the menu to the tray
tray.setContextMenu(menu)

# start application execution 
app.exec_()
