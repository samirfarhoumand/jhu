The data set we use consists of 252 men with estimates of the percentage of body fat determined by underwater
weighing, biologic data, and various body circumference measurements. 

When run, bodyfat.py will download the data from online and distribute it into a table Body_Fat in database bodyfat.db. Bodyfat.sql characterizes the the sole table, Body_Fat, which is the cleaned data that was directly uploaded from online and cleaned and transformed. 

During EDA, we add fixed columns which impossible data, dropped an observations and add derived features. At the end of the EDA, we upload this data to table Body_Fat2 Table Body_Fat2 is only filled after running body_fat_explore.ipynb, our EDA file. This dataset is subsequently used for modeling.

Bodyfat_get.ipynb is an additional file that describes the process used to pull the origianl data in jupyter notebook format with added commentary.

The link for the video presentation is available: https://youtu.be/D0EMGZmkwyc