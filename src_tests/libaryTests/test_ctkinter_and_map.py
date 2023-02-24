import customtkinter
import geopandas
import webbrowser
import os

# Tests customtkinter and geopandas mapping feature
# This is a minimal example of an custom tkinter gui with a button that creates
# an osm map from geojson data.

# creates an app
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("minimal example app")
        self.minsize(400, 300)

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button.pack(padx=20, pady=20)


        self.gdf = geopandas.read_file("../../data/partOfKarlsruhe.geojson") # load the geojson
        self.gdf["area"] = self.gdf.area # calculate the area of the "Vekehrzellen"
        self.gdf["area"]

        self.map = self.gdf.explore("area", legend=False) # creates the map
        self.map.save("build/map.html") # save the map on disk


    # the function that gets called when the button is presses
    def button_callback(self):
        print("button pressed")
        url = 'file://' + os.path.realpath("build/map.html")
        webbrowser.open(url, new=2)  # open the map in a new tab in the webbrowser


if __name__ == "__main__":
    app = App()
    app.mainloop()
