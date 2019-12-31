import os
from pathlib import Path

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_DIR = Path(CURRENT_DIR).parent.absolute()


ui_list = {
    'mainwindow.ui' : 'ui_mainwindow.py',
    'budgetwidget.ui' : 'ui_budgetwidget.py',
    'comptepage.ui' : 'ui_comptepage.py',
    #'propertieswindow.ui' : 'ui_propertieswindow.py'
}


for ui_file, py_file in ui_list.items():
    cmd = "pyside2-uic -x {} -o {}".format(PROJECT_DIR.joinpath('qt_ui').joinpath(ui_file), PROJECT_DIR.joinpath('ui').joinpath(py_file))
    print(cmd)
    os.system(cmd)
