import folium

map = folium.Map(location=[37, 127], zoom_start=7)

marker = folium.Marker([37.562650039, 126.945578678],
                       popup='이화여자대학교',
                       icon=folium.Icon(color='green'))

marker.add_to(map)

map.save(r'project27_University_Visualization/uni_map.html')
