import pandas as pd
import folium

file_path = "rain_garden_maintenance_priority.ods"
df = pd.read_excel(file_path, engine="odf")


# Center map
center_lat = df["lat"].mean()
center_lon = df["lon"].mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles="OpenStreetMap")

for _, r in df.iterrows():
    prio = int(r["priority"])
    color = "green" if 1 <= prio <= 5 else "orange"
    
    popup = folium.Popup(f"ID: {int(r['id'])}<br>Priorité: {prio}", max_width=250)
    
    # Pin-like marker (FontAwesome)
    folium.Marker(
        location=[r["lat"], r["lon"]],
        popup=popup,
        icon=folium.Icon(color=color, icon="map-marker", prefix="fa"),
    ).add_to(m)

out_path = "carte_points_priorites.html"
m.save(out_path)

out_path
