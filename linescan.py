# dataline example from the gwyddion website
import sys

sys.path.append("C:/Program Files (x86)/Gwyddion/bin")

import gwy, os, glob
import numpy as np

sys.path.append("C:\Program Files (x86)\Gwyddion\share\gwyddion\pygwy")
import gwyutils

folder = raw_input("Folder path : ")
# input polynomial order
polynom = -1
while polynom <= 0 or polynom > 12:
    polynom = input("Polynomial order to remove : ")
    polynom = int(polynom)

for filename in glob.glob(folder + "/*.dat"):
    # print the filename
    print "Processing file: ", filename, "\n"

    container = gwy.gwy_file_load(filename,gwy.RUN_IMMEDIATE)
    gwy.gwy_app_data_browser_add(container)

    dfields = gwyutils.get_data_fields_dir(container)
    for key in dfields.keys():    # goint through datafields, i.e. channels
        datafield = dfields[key]
        datafield_id = key.split('/')[1]
        
         ## Remove polynomial background
        coeffs = datafield.fit_polynom(polynom, polynom)
        datafield.subtract_polynom(polynom, polynom, coeffs)
        datafield.data_changed()

        data = gwy.gwy_app_data_browser_get_current(gwy.APP_DATA_FIELD)

        ## get some data from the datafield
        xres = datafield.get_xres()
        yres = datafield.get_yres()

        zmin, zmax = datafield.get_min_max()

        ## print the xres, yres, zmin and zmax
        print "xres: ", xres
        print "yres: ", yres
        print "zmin: ", zmin
        print "zmax: ", zmax, "\n"

        col1 = 1
        row1 = 1
        col2 = 1
        row2 = 100
        npoints = -1
        thickness = 1
        interpolation = gwy.INTERPOLATION_LINEAR
        dl = gwy.DataLine(1, 1)
        for i in range(6):
            col1 += 500
            col2 = col1
            datafield.get_column(dl, col1)
            # get length of the data line
            y = np.arange(0, len(dl.get_data()))*dl.get_dx()
            profile = np.asarray(dl.get_data())
            data_profile = np.column_stack((y, profile))  
            # save the data to a csv file
            np.savetxt(os.path.splitext(filename)[0] + "_dh_c" + str(polynom) + "_col" + str(col1) + ".csv", data_profile, fmt='%8.4f,%8.4f', delimiter=',')
            #@note: This is more advanced way to get the profile,
            #       but currently it is not working properly -- ivt 28.05.2024
            #lines = datafield.get_profile(col1, row1, col2, row2, npoints, thickness, interpolation)
            #print lines 
            #print lines[0].get_dx(), lines[0].get_min_max(), lines[0].get_avg()
