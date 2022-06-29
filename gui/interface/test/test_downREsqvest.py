import io
import sys

import folium
from folium.plugins.draw import Draw

from PyQt5.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Mapy(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):
        vbox = QVBoxLayout(self)
        self.webEngineView = QWebEngineView()
        self.webEngineView.page().profile().downloadRequested.connect(
            self.handle_downloadRequested
        )
        self.loadPage()
        vbox.addWidget(self.webEngineView)
        self.setLayout(vbox)
        self.setGeometry(600, 600, 650, 650)
        self.setWindowTitle("mapy")
        self.show()

    def loadPage(self):
        m = folium.Map(location=[51.7687323, 19.4569911], zoom_start=5)
        Draw(
            export=True,
            filename="my_data.geojson",
            position="topleft",
            draw_options={
                "polyline": False,
                "rectangle": False,
                "circle": False,
                "circlemarker": False,
            },
            edit_options={"poly": {"allowIntersection": False}},
        ).add_to(m)
        data = io.BytesIO()
        m.save(data, close_file=False)
        self.webEngineView.setHtml(data.getvalue().decode())

    def handle_downloadRequested(self, item):
        path, _ = QFileDialog.getSaveFileName(
            self, "Save File", item.suggestedFileName()
        )
        if path:
            item.setPath(path)
            item.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Mapy()
    sys.exit(app.exec_())