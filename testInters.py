import navigation.intersections2 as inters2
import visualization.draw_nav as draw_nav
import visualization.GUI as GUI
import osmloading.properties as props

draw_nav.draw_lanes()
GUI.centerCamera(-10,10)
GUI.runGUI()
# inters2