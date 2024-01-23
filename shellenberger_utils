'''
This is a showcase for Shellenberger Analytics Consulting.
It is still being updated as I gain more experience.
Last updated 1/9/2024
'''

import statistics

def main(): # This will be the main function for displaying the information.
    print(byline)

# here are all the variables
company_name: str = "Shellenberger Analytics Consulting"
rate_dollars_per_hour: float = 62.99
years_spent_in_data: int = 3 # years spent learning and using data effectively 
has_a_masters: bool = False
soft_skills: list = ["Hard Working", "Problem-Solver", "Communicative", "Open-Minded"]
top_ratings_out_of_five: list = [5, 4.6, 4.5, 4, 4.3, 4.3, 4.7]

rate_per_hour_string = f"Rate Per Hour: ${rate_dollars_per_hour}"
# Extracting each soft skill to make it print more professional.
soft_skills_string = f"Skills Include: {soft_skills[0]}, {soft_skills[1]}, {soft_skills[2]}, and {soft_skills[3]}"
has_a_masters_string = f"Has Masters Degree: {has_a_masters}"

smallest_rating = min(top_ratings_out_of_five)
highest_rating = max(top_ratings_out_of_five)
average_rating = round(statistics.mean(top_ratings_out_of_five),2) #round to 2 decimal places
number_of_ratings = len(top_ratings_out_of_five)
standard_deviation = statistics.stdev(top_ratings_out_of_five)

# This is where the basics will be stored and can be called in one print function.
byline: str = f"""
{company_name}
{rate_per_hour_string}
{soft_skills_string}
{has_a_masters_string}
Years in the Field: {years_spent_in_data}
Average Rating: {average_rating}
Max Rating: {highest_rating}
"""

# This code can only run from this script.
if __name__ == "__main__":
    main()
