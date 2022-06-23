from calendar import c
import io
import sys

import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets
import clipboard
from folium.plugins import MousePosition
import folium.features
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    m = folium.Map(
        location=[59.954809, 30.630337], zoom_start=16   #tiles="Stamen Toner"
    )
    MousePosition().add_to(m)

    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"

    MousePosition(
        position="topright",
        separator=" | ",
        empty_string="NaN",
        lng_first=True,
        num_digits=20,
        prefix="Coordinates:",
        lat_formatter=formatter,
        lng_formatter=formatter,
    ).add_to(m)
    popup1 = folium.LatLngPopup()
    click = folium.ClickForMarker()
    data = io.BytesIO()
    m.add_child(popup1)
    #m.add_child(click) 

    folium.LayerControl().add_to(m)    


    m.save(data, close_file=False)


    

    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(800, 600)
    w.show()

    sys.exit(app.exec_())