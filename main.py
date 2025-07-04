import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
from time import sleep
from os import system
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = 'finance_data.csv'
    COLUMNS = ["date", "amount", "category", "description"]
    DATE_FORMAT = "%d-%m-%Y"

    @classmethod    # can access the class but not the instance of the class
    def init_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date":date,
            "amount": amount,
            "category": category,
            "description": description,
        }

        with open(cls.CSV_FILE, 'a', newline="") as csvfile:    # open to csv file to write
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)    # give the writer the csv file and the the column names
            writer.writerow(new_entry)    # adding new entry
            print("Entry added to file")

    @classmethod
    def get_trasactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.DATE_FORMAT)
        start_date = datetime.strptime(start_date, CSV.DATE_FORMAT)    # converting to datetime object for easy logic
        end_date = datetime.strptime(end_date, CSV.DATE_FORMAT)    # converting to datetime object for easy logic

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)    # creating a mask of data in range of staring and ending dates
        filtered_df = df.loc[mask]    # storing the masked data in a dataframe

        if filtered_df.empty:
            print("NO TRASACTIONS IN THE GIVEN RANGE!!")
        else:
            print(f"\nTrasaction from {start_date.strftime(CSV.DATE_FORMAT)} to {end_date.strftime(CSV.DATE_FORMAT)}:")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.DATE_FORMAT)}))

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()    # getting the sum of all the rows with category income 
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()    # getting the sum of all the rows with category expense 

            print("\nSUMMARY")
            print(f"Total Income: Rs.{total_income:.2f}")
            print(f"Total Expense: Rs.{total_expense:.2f}")
            print(f"Net Saving: Rs.{(total_income - total_expense):.2f}")
            print()

        return filtered_df

def add():
    '''To get data from the user and write it into the CSV file'''

    CSV.init_csv()    # to load or create the csv file 
    date = get_date("Enter the date of transaction (dd-mm-yy) or press enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)    # wrting data csv

def plot_transactions(df):
    df.set_index("date", inplace=True)
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)
    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10,5))
    plt.plot(income_df.index, income_df["amount"], label='Income', color ='g')
    plt.plot(expense_df.index, expense_df["amount"], label='Expense', color ='r')
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\nMAIN MENU")
        print("1. Add a new transaction.")
        print("2. View Transactions and Summary given a date range.")
        print("\nPress 'q' to quit")
        choice = input("Enter your choice :")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yy): ")
            end_date = get_date("Enter the end date (dd-mm-yy): ")
            df = CSV.get_trasactions(start_date, end_date)
            while True:
                choice = input("Press 'p' to show the plot or 'm' to go to main menu: ").lower()
                if choice == "p":
                    plot_transactions(df)
                    break
                elif choice == "m":
                    break
                else:
                    print("INVALID INPUT!!")

            system("cls")        

        elif choice == "q":
            print("PROGRAM IS QUITTING!!")
            sleep(1.5)
            break
        else:
            print("INVALID INPUT!!")

if __name__ == "__main__":
    main()