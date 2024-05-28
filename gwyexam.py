import sys

sys.path.append("C:/Program Files (x86)/Gwyddion/bin")

import gwy, os, glob

folder = raw_input("Folder path : ")

for filename in glob.glob(folder + "/*.plux"):

    d = gwy.gwy_app_data_browser_get_current(gwy.APP_DATA_FIELD)

    ## Remove polynomial background

    polynom = input("Polynom order : ")
    polynom = int(polynom)

    coeffs = d.fit_polynom(polynom, polynom)
    d.subtract_polynom(polynom, polynom, coeffs)
    d.data_changed()

    ## Save the file as a .bmp

    newname = os.path.splitext(filename)[0] + ".bmp"
    gwy.gwy_file_save(d, newname, gwy.RUN_IMMEDIATE)