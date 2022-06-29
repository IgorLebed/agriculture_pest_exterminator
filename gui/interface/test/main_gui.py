import io
import sys

import folium
from PySide6 import QtWidgets, QtWebEngineWidgets

class MapDisplay():
    def __init__(self, zoom_start, location):
        self.z_s = zoom_start
        self.lc = location

    def map_v(self):
        app = QtWidgets.QApplication(sys.argv)

        self.m = folium.Map(self.lc, self.z_s)#tiles="Stamen Toner")

        data = io.BytesIO()
        self.m.save(data, close_file=False)

        w = QtWebEngineWidgets.QWebEngineView()
        w.setHtml(data.getvalue().decode())
        w.resize(800, 600)
        w.show()

        sys.exit(app.exec_())

if __name__ == "__main__":
    location = [59.954809, 30.630337]
    md = MapDisplay(16, location)
    md.map_v()