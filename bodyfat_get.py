#import necessary modules
import csv
import sqlite3
import requests
import io

def brozeks(D):
    """
    Converts body density to body fat percentage via Brozek's equation
    
    """
    bodyfat =  ((4.570/float(D) - 4.142) * 100)
    bodyfat = float(str(round(bodyfat, 1)))
    return (bodyfat)

def main():
    """
    Function pulls in data and transforms and cleans it for our data warehouse
    """
    
    #connect to database
    conn = sqlite3.connect('bodyfat.db')
    cur = conn.cursor()
    
    #pull data into list
    url = 'http://staff.pubhealth.ku.dk/~tag/Teaching/share/data/Bodyfat.csv'
    r = requests.get(url)
    buff = io.StringIO(r.text)
    dr = csv.DictReader(buff)
    for row in dr:
        #find all the variables
        density = row["Density"]
        bodyfat_siri = row["bodyfat"]
        bodyfat_brozek = brozeks(row["Density"])
        age = row["Age"]
        height = row["Height"]
        weight = row["Weight"]
        neck = row["Neck"]
        chest = row["Chest"]
        abdomen = row["Abdomen"]
        hip = row["Hip"]
        thigh = row["Thigh"]
        knee = row["Knee"]
        ankle = row["Ankle"]
        biceps = row["Biceps"]
        forearm = row["Forearm"]
        wrist = row["Wrist"]

        #insert into table
        sql = f"""INSERT INTO Body_Fat (BodyFat_siri, Density, Age, Height, 
            Weight, Neck, Chest, Abdomen, Hip, Thigh, BodyFat_brozek,
            Knee, Ankle, Biceps, Forearm, Wrist)
                VALUES ('{bodyfat_siri}', '{density}', '{age}', '{height}',
                '{weight}', '{neck}', '{chest}', '{abdomen}', '{hip}',
                '{thigh}', '{bodyfat_brozek}','{knee}', '{ankle}', '{biceps}',
                '{forearm}','{wrist}');
            """
        cur.execute(sql)
    conn.commit()
    
if __name__ == '__main__':
    main()

