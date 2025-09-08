# map_overlay.py
import folium
from folium.plugins import TimestampedGeoJson

def render_map(traffic_data):
    m = folium.Map(location=[13.0827, 80.2707], zoom_start=12)

    for zone in traffic_data.get('zones', []):
        folium.Circle(
            location=zone['coords'],
            radius=zone['radius'],
            color='red' if zone['severity'] > 3 else 'orange',
            fill=True,
            fill_opacity=0.6
        ).add_to(m)

    features = [{
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [v['lon'], v['lat']]},
        "properties": {
            "time": v['timestamp'],
            "popup": f"Speed: {v['speed']} km/h"
        }
    } for v in traffic_data.get('vehicles', [])]

    TimestampedGeoJson({
        "type": "FeatureCollection",
        "features": features
    }, period="PT1M", add_last_point=True).add_to(m)

    return m
