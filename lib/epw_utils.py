# EPW parsing functionality
# Read past this if you don't care for code.
import pandas as pd
import datetime

import matplotlib.pyplot as plt
import seaborn as sns
cmap = sns.color_palette("hls", 8)

def get_datetime(row):
    # Compute datetime from month, day and hour values in row
    # Assume year is 2017
    return datetime.datetime(year=2017, month=row['Month'], day=row['Day'], hour=row['Hour']-1)


def get_doy(row):
    # Compute day of year from month and day of month values in row
    monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(monthDays[:row['Month']]) + row['Day']


# def inplace_change(filename, old_string, new_string):
#     # Safely read the input filename using 'with'
#     with open(filename) as f:
#         s = f.read()
#         if old_string not in s:
#             #             print '"{old_string}" not found in {filename}.'.format(**locals())
#             return

#     # Safely write the changed content, if found in the file
#     with open(filename, 'w') as f:
#         #         print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
#         s = s.replace(old_string, new_string)
#         f.write(s)


def epw_to_df(epw_path, skiprows=8):
    # Read EPW file and return a pandas dataframe 

    # inplace_change(epw_path, '\n\n', '\n')

    df = pd.read_csv(epw_path, skiprows=skiprows, header=None)
    df = df.reset_index()

    epw_columns = ['Index',
                   'Year',
                   'Month',
                   'Day',
                   'Hour',
                   'Minute',
                   'Remove',
                   'Dry_Bulb_Temperature',
                   'Dew_Point_Temperature',
                   'Relative_Humidity',
                   'Atmospheric_Station_Pressure',
                   'Extraterrestrial_Horizontal_Radiation',
                   'Extraterrestrial_Direct_Normal_Radiation',
                   'Horizontal_Infrared_Radiation_Intensity',
                   'Global_Horizontal_Radiation',
                   'Direct_Normal_Radiation',
                   'Diffuse_Horizontal_Radiation',
                   'Global_Horizontal_Illuminance',
                   'Direct_Normal_Illuminance',
                   'Diffuse_Horizontal_Illuminance',
                   'Zenith_Luminance',
                   'Wind_Direction',
                   'Wind_Speed',
                   'Total_Sky_Cover',
                   'Opaque_Sky_Cover',
                   'Visibility',
                   'Ceiling_Height',
                   'Present_Weather_Observation',
                   'Present_Weather_Codes',
                   'Precipitable_Water',
                   'Aerosol_Optical_Depth',
                   'Snow_Depth',
                   'Days_Since_Last_Snowfall',
                   'Albedo',
                   'Liquid_Precipitation_Depth',
                   'Liquid_Precipitation_Quantity']

    df.columns = epw_columns

    return df


def heatmap_matrix(df, value):
    hm = df.pivot(index='Hour', columns='doy')[value]
    hm = hm.reindex(index=hm.index[::-1])
    return hm


def yearly_heatmap_plot(df, value, title=None, plt=plt):
    plt.figure(figsize=(24, 6))

    ax = sns.heatmap(heatmap_matrix(df, value), cmap=cmap)

    ax.hlines([8, 17], *ax.get_xlim())

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    day_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    end_of_months = [sum(day_per_month[:i+1])
                     for i, x in enumerate(day_per_month[:-1])]
    mid_month_days = [sum(day_per_month[:i]) + x/2 for i,
                      x in enumerate(day_per_month)]

    ax.vlines(end_of_months, *ax.get_ylim())
    ax.set_xticks(mid_month_days)
    ax.set_xticklabels(months)
    ax.set_xlabel('Month')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)

    if title == None:
        title = value
    ax.set_title(title, fontsize=20)


