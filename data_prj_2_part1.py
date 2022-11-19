''' this file is for Python Data Project-2 Part 1'''
import csv
import constants as const
from functions import bar_plot_prj2_1

def calculate(csv_file: str):
    ''' get required data from csv in dict '''

    with open(csv_file, encoding="latin-1") as inputfile:
        authorized_capital_rangewise = {}
        company_reader = csv.DictReader(inputfile)
        invalid_capital_value = []

        for company in company_reader:
            try:
                temp = int(company['AUTHORIZED_CAP'])
                if temp <= 100000:
                    authorized_capital_rangewise["<= 1L"] = (
                        authorized_capital_rangewise.get("<= 1L", 0) + 1
                    )
                elif temp <= 1000000:
                    authorized_capital_rangewise["1L to 10L"] = (
                        authorized_capital_rangewise.get("1L to 10L", 0) + 1
                    )
                elif temp <= 10000000:
                    authorized_capital_rangewise["10L to 1Cr"] = (
                        authorized_capital_rangewise.get("10L to 1Cr", 0) + 1
                    )
                elif temp <= 100000000:
                    authorized_capital_rangewise["1Cr to 10Cr"] = (
                        authorized_capital_rangewise.get("1Cr to 10Cr", 0) + 1
                    )
                elif temp > 100000000:
                    authorized_capital_rangewise["> 10Cr"] = (
                        authorized_capital_rangewise.get("> 10Cr", 0) + 1
                    )
            except ValueError:
                invalid_capital_value.append(company)
    return authorized_capital_rangewise

def execute():
    ''' function to get data to plot graphs'''
    # get required data from csv in dict and then call plot function

    authorized_capital_rangewise = calculate(const.MAHARASHTRA_CSV)

    bar_plot_prj2_1(authorized_capital_rangewise, const.VALUE_OF_AUTH_CAP,
                const.NO_OF_COMPANIES, const.AUTH_CAP)


execute()  # driver function
