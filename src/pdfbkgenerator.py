import PyPDF2


class PdfBkGenerator:
    def __init__(self, source, destination):
        self._source = source
        self._destination = destination
        self._bkinfo = None

    def set_bkmark_txt(self, bktxt):
        with open(bktxt, "r", encoding="utf-8") as fp:
            self._bkinfo = fp.readlines()

    def add_bookmark(self):
        reader = PyPDF2.PdfReader(self._source)
        writer = PyPDF2.PdfWriter()
        parents = [None] * 10
        for i in range(0, len(reader.pages)):
            writer.add_page(reader.pages[i])

        for l in self._bkinfo:
            l = l.strip()
            lx = l.split("\t")
            level = int(lx[0])
            title = lx[1]
            pageno = int(eval(lx[2]))
            if level == 1:
                bkitem = writer.add_outline_item(title=title, pagenum=pageno - 1)
                parents[0] = bkitem
            else:
                bkitem = writer.add_outline_item(
                    title=title, pagenum=pageno - 1, parent=parents[level - 2]
                )
                parents[level - 1] = bkitem

        with open(self._destination, "wb") as fp:
            writer.write(fp)


if __name__ == "__main__":
    s = "小学5年级数学下册.pdf"
    d = "view.pdf"
    bk = "bookmark.txt"
    tool = PdfBkGenerator(s, d)
    tool.set_bkmark_txt(bk)
    tool.add_bookmark()
