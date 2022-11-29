''' This file is for Python Data Project-2 Part 4'''
import csv
import constants as const
from functions import bar_group_plot

START_YEAR = 2008
END_YEAR = 2017


def calculate(csv_file: str):
    ''' get required data from csv in dict '''

    with open(csv_file, encoding="latin-1") as inputfile:
        registration_counts = {}
        activity_count = {}
        company_reader = csv.DictReader(inputfile)
        invalid_company = []

        for company in company_reader:
            try:
                date = company['DATE_OF_REGISTRATION']
                year = date[6] + date[7]  # because format of date is dd-mm-yy
                year = int(year)
                activity = company['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']
                if START_YEAR <= year <= END_YEAR:
                    registration_counts[year] = (
                        registration_counts.get(
                            year, {}
                        )
                    )
                    registration_counts[year][activity] = (
                        registration_counts[year].get(activity, 0) + 1
                    )
                    activity_count[activity] = (
                        activity_count.get(activity, 0) + 1)

            except ValueError:
                invalid_company.append(company)
            except IndexError:
                invalid_company.append(company)
    return registration_counts, activity_count


def transform(activitywise_counts: dict, top_n: int):
    ''' get top 5 Prinicipal Business Activity'''

    counts_activitywise = list(activitywise_counts.values())
    counts_activitywise.sort(reverse=True)
    top_counts = counts_activitywise[:top_n]

    top_business_activity = {}
    for value in top_counts:
        for activity_name, activity_count in activitywise_counts.items():
            if activity_count == value:
                top_business_activity[activity_name] = activity_count

    return top_business_activity.keys()


def get_plot_data(registration_yearwise: dict, top_business_activity: list):
    ''' get last 10 years '''
    for key in to_delete:
        del registration_yearwise[key]
        
    for year in registration_yearwise.keys():
        for company in to_delete:
            del registration_yearwise[company]

    return registration_yearwise


def execute():
    ''' function to get data to plot graphs'''
    # get required data from csv in dict and then call plot function
    registration_yearwise, activity_count = calculate(const.MAHARASHTRA_CSV)
    top_business_activity = transform(activity_count, 5)
    registration_yearwise = get_plot_data(registration_yearwise, top_business_activity)

    bar_group_plot(registration_yearwise, const.GROUP_PLOT,
                   const.NO_OF_COMPANIES, const.COMPANY_REG)


execute()  # driver function
