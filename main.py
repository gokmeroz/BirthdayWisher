import smtplib
import datetime as dt
import random
import pandas


myEmail=input("Please type the sender's e-mail address: ")

password=input("Please type your app password: ")
today=dt.datetime.now()

today_tuple = (today.month, today.day)
data=pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdayPerson=birthdays_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
           contents=file.read()
           contents=contents.replace("[NAME]", birthdayPerson["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myEmail,password=password)
        connection.sendmail(
            from_addr=myEmail,
            to_addrs=birthdayPerson["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
        connection.close()

