import sys
from cx_Freeze import setup, Executable

site_packages = "C:/Users/schup/OneDrive/Documents/KonfiguratorFuerOSMDaten/venv/Lib/site-packages"
pyproj_path = f"{site_packages}/pyproj.libs"
fiona_path = f"{site_packages}/Fiona.libs"

# Dependencies are automatically detected, but it might need fine tuning.
# Setup base packages
build_exe_options = {
    "packages": [
        "fiona",
        "matplotlib",
        "seaborn"
    ],
    "include_files": [
        (pyproj_path, "Lib/pyproj.libs"),
        (fiona_path, "Lib/Fiona.libs"),
        ("data", "data")
    ],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    # Meta-data
    name="Configurator for OSM-Data",
    version="1.0",
    author="Felix Weik, Jan-Philipp Hansen, Karl Bernhard, Pascal Dawideit, Simon Schupp",
    description="Configurator for OSM-Data",
    long_description="Whether it’s biking to college or driving to the supermarket, traffic effects us all. "
                     "This product uses generated geodata from the free project ‘OpenStreetMap’ (OSM) "
                     "and creates a numerical ranking of the attractiveness of geographic locations."
                     " A main focus is the configurability of the generation of this score. "
                     "Traffic planners can easily use this attractiveness score for their traffic forecasting models.",
    url="https://github.com/LuposX/KonfiguratorFuerOSMDaten",
    license="GPL-3.0",
    keywords=["osm", "traffic", "data", "GUI"],

    # Build options
    options={"build_exe": build_exe_options},
    executables=[
        Executable("src/osm_configurator/control/application_controller.py",
                   base=base,
                   targetName="configurator_for_osm_data.exe"
                   )
    ]
)
