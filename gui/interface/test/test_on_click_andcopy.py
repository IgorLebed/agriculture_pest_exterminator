import folium
import jinja2
from jinja2 import Template
from folium.map import Marker

tmpldata = """<!-- monkey patched Marker template -->
{% macro script(this, kwargs) %}
    var {{ this.get_name() }} = L.marker(
        {{ this.location|tojson }},
        {{ this.options|tojson }}
    ).addTo({{ this._parent.get_name() }}).on('click', onClick);
{% endmacro %}
"""

Marker._mytemplate = Template(tmpldata)
def myMarkerInit(self, *args, **kwargs):
    self.__init_orig__(*args, **kwargs)
    self._template = self._mytemplate
Marker.__init_orig__ = Marker.__init__
Marker.__init__ = myMarkerInit

location_center = [45.5236, -122.6750]
locations = [[45.5012, -122.6655],[45.5132, -122.6708],[45.5275, -122.6692],[45.5318, -122.6745]]

m = folium.Map(location_center, zoom_start=13)

for location in locations: #range(locations.shape[0]):
    folium.Marker(
        location=location,
        popup = f'<p id="latlon">{location[0]}, {location[1]}</p>'
    ).add_to(m)

el = folium.MacroElement().add_to(m)
el._template = jinja2.Template("""
    {% macro script(this, kwargs) %}
    function copy(text) {
        var input = document.createElement('textarea');
        input.innerHTML = text;
        document.body.appendChild(input);
        input.select();
        var result = document.execCommand('copy');
        document.body.removeChild(input);
        return result;
    };
    
    function getInnerText( sel ) {
        var txt = '';
        $( sel ).contents().each(function() {
            var children = $(this).children();
            txt += ' ' + this.nodeType === 3 ? this.nodeValue : children.length ? getInnerText( this ) : $(this).text();
        });
        return txt;
    };
    
    function onClick(e) {
       var popup = e.target.getPopup();
       var content = popup.getContent();
       text = getInnerText(content);
       copy(text);
    };
    {% endmacro %}
""")

display(m)