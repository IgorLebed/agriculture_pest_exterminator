import io
import sys

import folium
from PySide6 import QtWidgets, QtWebEngineWidgets




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    m = folium.Map(
        location=[59.939866, 30.269048], zoom_start=13   #tiles="Stamen Toner"
    )

    data = io.BytesIO()
    m.save(data, close_file=False)

    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(800, 600)
    w.show()

    sys.exit(app.exec_())