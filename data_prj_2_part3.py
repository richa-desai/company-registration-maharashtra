''' this file is for Python Data Project-2 Part 3'''
import csv
import constants as const
from functions import bar_plot_prj_2_3

def calculate(csv_file: str):
    ''' get required data from csv in dict '''

    with open(csv_file, encoding="latin-1") as inputfile:
        company_registration_districtwise = {}
        company_reader = csv.DictReader(inputfile)
        invalid_company = []

        for company in company_reader:
            try:
                temp_date = company['DATE_OF_REGISTRATION']
                year = temp_date[6]+temp_date[7]
                year = int(year)
                if year == 15:
                    temp = company['Registered_Office_Address']
                    pincode = temp[-6]+temp[-5]+temp[-4]+temp[-3]+temp[-2]+temp[-1]
                    company_registration_districtwise[pincode] = (
                            company_registration_districtwise.get(pincode, 0) + 1
                        )
            except ValueError:
                invalid_company.append(company)
            except IndexError:
                invalid_company.append(company)
    return company_registration_districtwise

def transform(company_registration_districtwise, top_n):
    ''' function to get top n zip codes and get district names'''
    num_of_registrations = list(company_registration_districtwise.values())
    num_of_registrations.sort(reverse=True)
    top_n_regs = num_of_registrations[:top_n]

    top_districts = {}
    for value in top_n_regs:
        key = list(company_registration_districtwise.keys())[
            list(company_registration_districtwise.values()).index(value)]
        top_districts[key] = company_registration_districtwise[key]

    return top_districts


def get_district_name(top_companies):
    ''' function to get district names'''

    with open("pincode.csv", encoding="latin-1") as inputfile:
        district_reader = csv.DictReader(inputfile)
        district_pincode = {}

        for district in district_reader:
            temp_zip = district['Pin Code']
            del_this_var = temp_zip[0]+temp_zip[1]+temp_zip[2]+temp_zip[3]+temp_zip[4]+temp_zip[5]
            district_pincode[del_this_var] = district['District']

    top_companies_district = top_companies.copy()

    undefined_pin = []
    for key in top_companies.keys():
        try:
            top_companies_district[key].append(district_pincode[key])
        except ValueError:
            undefined_pin.append(key)
        except KeyError:
            undefined_pin.append(key)
    print(undefined_pin)
    return top_companies_district

def execute():
    ''' function to get data to plot graphs'''
    # get required data from csv in dict and then call plot function
    company_registration_districtwise = calculate(const.MAHARASHTRA_CSV)

    top_companies_dist = get_district_name(company_registration_districtwise)
    top_companies = transform(top_companies_dist, 10)


    bar_plot_prj_2_3(top_companies.values(), top_companies.values(), const.DISTRICT,
                const.NO_OF_COMPANIES, const.COMPANY_REG_DIST)


execute()  # driver function
