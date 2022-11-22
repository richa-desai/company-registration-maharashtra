''' this file is for Python Data Project-2 Part 2'''
import csv
import constants as const
from functions import bar_plot


def calculate(csv_file: str):
    ''' get required data from csv in dict '''

    with open(csv_file, encoding="latin-1") as inputfile:
        company_registration_yearwise = {}
        company_reader = csv.DictReader(inputfile)
        invalid_company = []

        for company in company_reader:
            try:
                date = company['DATE_OF_REGISTRATION']
                year = date[6]+date[7]  # because format of date is dd-mm-yy
                year = int(year)
                company_registration_yearwise[year] = (
                    company_registration_yearwise.get(year, 0) + 1
                )
            except ValueError:
                invalid_company.append(company)
            except IndexError:
                invalid_company.append(company)
    return company_registration_yearwise


def execute():
    ''' function to get data to plot graphs'''
    # get required data from csv in dict and then call plot function
    company_registration_yearwise = calculate(const.MAHARASHTRA_CSV)

    bar_plot(company_registration_yearwise, const.REG_YEAR,
             const.NO_OF_COMPANIES, const.COMPANY_REG)


execute()  # driver function
