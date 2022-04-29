import visualization.draw_osm as draw_prop
import visualization.GUI as GUI
import osmloading.properties as props

draw_prop.draw_roads()
draw_prop.draw_buildings()
GUI.centerCamera(-10,10)
GUI.runGUI()