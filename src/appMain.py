import sys


from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

import resources_rc

from pdfbkgenform import PdfBkGenForm

app = QApplication(sys.argv)
icon = QIcon(":/icon/app.icns")
app.setWindowIcon(icon)

mainform = PdfBkGenForm()

mainform.show()

sys.exit(app.exec_())
