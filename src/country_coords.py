"""
country_coords.py — approximate (latitude, longitude) centroids for every
nationality appearing in the Winter Athletes dataset.

Used to build a geographic bubble map without needing internet access to
fetch shapefiles or a geocoding service — each country is plotted at its
approximate center point, sized by athlete count.
"""

COUNTRY_COORDS = {
    "Albania": (41.15, 20.17), "Algeria": (28.03, 1.66), "Andorra": (42.55, 1.60),
    "Argentina": (-38.42, -63.62), "Armenia": (40.07, 45.04), "Australia": (-25.27, 133.78),
    "Austria": (47.52, 14.55), "Azerbaijan": (40.14, 47.58), "Belarus": (53.71, 27.95),
    "Belgium": (50.50, 4.47), "Bermuda": (32.32, -64.75), "Bosnia and Herzegovina": (43.92, 17.68),
    "Brazil": (-14.24, -51.93), "Bulgaria": (42.73, 25.49), "Canada": (56.13, -106.35),
    "Cayman Islands": (19.31, -81.25), "Chile": (-35.68, -71.54), "China": (35.86, 104.20),
    "Chinese Taipei": (23.70, 121.00), "Colombia": (4.57, -74.30), "Croatia": (45.10, 15.20),
    "Cyprus": (35.13, 33.43), "Czech Republic": (49.82, 15.47), "Denmark": (56.26, 9.50),
    "Estonia": (58.60, 25.01), "Ethiopia": (9.15, 40.49), "Finland": (61.92, 25.75),
    "France": (46.23, 2.21), "Georgia": (42.32, 43.36), "Germany": (51.17, 10.45),
    "Ghana": (7.95, -1.02), "Great Britain": (55.38, -3.44), "Greece": (39.07, 21.82),
    "Hong Kong": (22.40, 114.11), "Hungary": (47.16, 19.50), "Iceland": (64.96, -19.02),
    "India": (20.59, 78.96), "Iran": (32.43, 53.69), "Ireland": (53.14, -7.69),
    "Israel": (31.05, 34.85), "Italy": (41.87, 12.57), "Jamaica": (18.11, -77.30),
    "Japan": (36.20, 138.25), "Kazakhstan": (48.02, 66.92), "Kenya": (-0.02, 37.91),
    "Kyrgyzstan": (41.20, 74.77), "Latvia": (56.88, 24.60), "Lebanon": (33.85, 35.86),
    "Liechtenstein": (47.17, 9.56), "Lithuania": (55.17, 23.88), "Macedonia": (41.61, 21.75),
    "Mexico": (23.63, -102.55), "Moldova": (47.41, 28.37), "Monaco": (43.74, 7.42),
    "Mongolia": (46.86, 103.85), "Montenegro": (42.71, 19.37), "Morocco": (31.79, -7.09),
    "Nepal": (28.39, 84.12), "Netherlands": (52.13, 5.29), "New Zealand": (-40.90, 174.89),
    "North Korea": (40.34, 127.51), "Norway": (60.47, 8.47), "Pakistan": (30.38, 69.35),
    "Peru": (-9.19, -75.02), "Poland": (51.92, 19.15), "Portugal": (39.40, -8.22),
    "Romania": (45.94, 24.97), "Russia": (61.52, 105.32), "San Marino": (43.94, 12.46),
    "Senegal": (14.50, -14.45), "Serbia": (44.02, 21.01), "Slovakia": (48.67, 19.70),
    "Slovenia": (46.15, 14.99), "South Africa": (-30.56, 22.94), "South Korea": (35.91, 127.77),
    "Spain": (40.46, -3.75), "Sweden": (60.13, 18.64), "Switzerland": (46.82, 8.23),
    "Tajikistan": (38.86, 71.28), "Turkey": (38.96, 35.24), "Ukraine": (48.38, 31.17),
    "United States": (37.09, -95.71), "Uzbekistan": (41.38, 64.59),
}
