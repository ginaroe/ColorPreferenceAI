# ColorPreferenceAI
an AI that learns a person's preference on colors and displays colors that s/he like and dislike

Modules needed: SKlearn, Pygame, Matplotlib

## instructions

- run **dataset.py** and see colors on the center. If you like that color, press the left arrow key. If you don't, press the right one. Your preference and its R, G, B values will be saved in csv files below. 70 answers or more than that is enough.
- run **analysis_rgb.py** and **analysis_hsv.py**, then you will see distribution of colors you like(pretty, P) and you don't(not pretty, N). You can also get a grasp of features of colors you like and dislike if you are knowledgable of color systems.
- run **colorchart_pretty.py** and **colorchart_not.py** to see colors that the AI picked up for you.
- Pygame has adopted the RGB color system. **rgb_hsv.py** translates three color components to HSV values.
- four **csv** files are database of the AI. If you want it to learn new preference, delete all the data of each files but 'r,g,b ' or 'h,s,v '.

## description on KNN algorithm

https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm

## description on RBG & HSV color system

https://en.wikipedia.org/wiki/RGB_color_model

https://en.wikipedia.org/wiki/HSL_and_HSV
