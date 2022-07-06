import io
import sys

import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets
from folium.plugins import MousePosition
from folium.plugins.measure_control import MeasureControl
from folium import plugins
import folium.features


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    m = folium.Map(
        location=[59.954809, 30.630337], zoom_start=16 
    )

    data = io.BytesIO()

    # Add custom base maps to folium
    basemaps = {
        'Google Maps': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Maps',
            overlay = True,
            control = True
        ),
        'Google Satellite': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Satellite',
            overlay = True,
            control = True
        ),
        'Google Terrain': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Terrain',
            overlay = True,
            control = True
        ),
        'Google Satellite Hybrid': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Satellite',
            overlay = True,
            control = True
        ),
        'Esri Satellite': folium.TileLayer(
            tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr = 'Esri',
            name = 'Esri Satellite',
            overlay = True,
            control = True
        )
    }

    # Add custom basemaps
    basemaps['Google Maps'].add_to(m)
    basemaps['Google Satellite Hybrid'].add_to(m)


    # Add a layer control panel to the map.
    m.add_child(folium.LayerControl())

    #fullscreen
    plugins.Fullscreen().add_to(m)

    
    #GPS
    #plugins.LocateControl().add_to(m)

    #mouse position
    fmtr = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
    plugins.MousePosition(position='topright', separator=' | ', prefix="Mouse:",lat_formatter=fmtr, lng_formatter=fmtr).add_to(m)

    #Add the draw 
    plugins.Draw(export=True, filename='data.geojson', position='topleft', draw_options=None, edit_options=None).add_to(m)  
    
   
    #Add measure tool 
    #plugins.MeasureControl(position='topright', primary_length_unit='meters', secondary_length_unit='miles', primary_area_unit='sqmeters', secondary_area_unit='acres').add_to(m)
    MeasureControl(
            position='topright', 
            primary_length_unit='meters', 
            secondary_length_unit='miles', 
            primary_area_unit='sqmeters', 
            secondary_area_unit='acres'
        ).add_to(m)
    m.add_child(folium.LatLngPopup())

    

    m.save(data, close_file=False)


    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(800, 600)
    w.show()
    #while True:
    sys.exit(app.exec_())


