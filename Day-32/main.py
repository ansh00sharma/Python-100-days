import smtplib
from datetime import datetime as dt
import pandas as pd
import random
my_email = "sharma999ansh@gmail.com"
password = "lizffknojzfeosds"

today = (dt.now().month, dt.now().day)
data = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person['email'],
                            msg=f"Subject:Happy Birthday \n\n {contents}")



