pip3 install PyInstaller -i https://pypi.tuna.tsinghua.edu.cn/simple<br/>

xcode-select --install<br/>

pyinstaller -n "Pdf Bookmark Generator" --windowed src/appMain.py<br/>

--add icon<br/>
app = BUNDLE(<br/>
    coll,<br/>
    name='Pdf Bookmark Generator.app',<br/>
    <font color="dd0000">icon='src/ico/app.icns'</font>,<br/>
    bundle_identifier=None,<br/>
)