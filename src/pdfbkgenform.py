from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_pdfbkgen import Ui_PdfBkGen
from pdfbkgenerator import PdfBkGenerator
import sys


class PdfBkGenForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PdfBkGen()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_btnpdf_clicked(self):
        curpath = QDir.currentPath()
        dlgtitle = "Select a pdf file"
        filt = "pdf file (*.pdf)"
        filename, _ = QFileDialog.getOpenFileName(self, dlgtitle, curpath, filt)
        if len(filename) > 1:
            self.ui.txtpdf.setText(filename)

    @pyqtSlot()
    def on_btnbk_clicked(self):
        curpath = QDir.currentPath()
        dlgtitle = "select a text file"
        filt = "text file(*.txt *.csv) "
        filename, _ = QFileDialog.getOpenFileName(self, dlgtitle, curpath, filt)
        if len(filename) > 1:
            self.ui.txtbk.setText(filename)

    @pyqtSlot()
    def on_btnrun_clicked(self):
        try:
            s = str(self.ui.txtpdf.text()).strip()

            if len(s) < 1:
                msg = "Please specify the pdf path!"
                return

            bk = str(self.ui.txtbk.text()).strip()
            if len(bk) < 1:
                msg = "Please specify the bookmark path!"
                return

            d = s[:-4] + "_withbk.pdf"
            pdfGen = PdfBkGenerator(s, d)
            pdfGen.set_bkmark_txt(bk)
            pdfGen.add_bookmark()
        except Exception as e:
            msg = "An error occurs.\nPlease check the bookmark format, the bookmark item should be separated by TAB\nThe file should be in utf-8 encoding\n{!s}".format(
                e
            )
        else:
            msg = "Generate Bookmark successfully!"
        finally:
            QMessageBox.information(self, "HAHA", msg, QMessageBox.StandardButton.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = PdfBkGenForm()
    form.show()
    app.exec()
