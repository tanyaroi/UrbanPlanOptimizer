from random import randrange, choice
from string import ascii_lowercase
from openpyxl import Workbook, chart

''' for 10 files do:
    - Create new workbook
    - Generate first line (labels)
    - Generate remaining 49 lines
        - for 49 rows do:
            - generate random id
            - generate random name:
                - create "seed" list of N names
                - choose name randomly
            - generate random grade
            - generate row with random values
            - append row to workbook
    - Write to new .xlsx file
'''


def main():

    # predefined list of male and female names
    male_names_list = [
        "James",
        "John",
        "Robert",
        "Michael",
        "William",
        "David",
        "Richard",
        "Joseph",
        "Thomas",
        "Charles",
        "Christopher",
        "Daniel",
        "Matthew",
        "Anthony",
        "Donald",
        "Mark",
        "Paul",
        "Steven",
        "Andrew",
        "Kenneth",
        "Joshua",
        "Kevin",
        "Brian",
        "George",
        "Edward",
        "Ronald",
        "Timothy",
        "Jason",
        "Jeffrey",
        "Ryan",
        "Jacob",
        "Gary",
        "Nicholas",
        "Eric",
        "Jonathan",
        "Stephen",
        "Larry",
        "Justin",
        "Scott",
        "Brandon",
        "Benjamin",
        "Samuel",
        "Frank",
        "Gregory",
        "Raymond",
        "Alexander",
        "Patrick",
        "Jack",
        "Dennis",
        "Jerry",
        "Tyler",
        "Aaron",
        "Jose",
        "Henry",
        "Adam",
        "Douglas",
        "Nathan",
        "Peter",
        "Zachary",
        "Kyle",
        "Walter",
        "Harold",
        "Jeremy",
        "Ethan",
        "Carl",
        "Keith",
        "Roger",
        "Gerald",
        "Christian",
        "Terry",
        "Sean",
        "Arthur",
        "Austin",
        "Noah",
        "Lawrence",
        "Jesse",
        "Joe",
        "Bryan",
        "Billy",
        "Jordan",
        "Albert",
        "Dylan",
        "Bruce",
        "Willie",
        "Gabriel",
        "Alan",
        "Juan",
        "Logan",
        "Wayne",
        "Ralph",
        "Roy",
        "Eugene",
        "Randy",
        "Vincent",
        "Russell",
        "Louis",
        "Philip",
        "Bobby",
        "Johnny",
        "Bradley"
    ]
    female_names_list = [
        "Mary",
        "Patricia",
        "Jennifer",
        "Linda",
        "Elizabeth",
        "Barbara",
        "Susan",
        "Jessica",
        "Sarah",
        "Karen",
        "Nancy",
        "Lisa",
        "Margaret",
        "Betty",
        "Sandra",
        "Ashley",
        "Dorothy",
        "Kimberly",
        "Emily",
        "Donna",
        "Michelle",
        "Carol",
        "Amanda",
        "Melissa",
        "Deborah",
        "Stephanie",
        "Rebecca",
        "Laura",
        "Sharon",
        "Cynthia",
        "Kathleen",
        "Amy",
        "Shirley",
        "Angela",
        "Helen",
        "Anna",
        "Brenda",
        "Pamela",
        "Nicole",
        "Samantha",
        "Katherine",
        "Emma",
        "Ruth",
        "Christine",
        "Catherine",
        "Debra",
        "Rachel",
        "Carolyn",
        "Janet",
        "Virginia",
        "Maria",
        "Heather",
        "Diane",
        "Julie",
        "Joyce",
        "Victoria",
        "Kelly",
        "Christina",
        "Lauren",
        "Joan",
        "Evelyn",
        "Olivia",
        "Judith",
        "Megan",
        "Cheryl",
        "Martha",
        "Andrea",
        "Frances",
        "Hannah",
        "Jacqueline",
        "Ann",
        "Gloria",
        "Jean",
        "Kathryn",
        "Alice",
        "Teresa",
        "Sara",
        "Janice",
        "Doris",
        "Madison",
        "Julia",
        "Grace",
        "Judy",
        "Abigail",
        "Marie",
        "Denise",
        "Beverly",
        "Amber",
        "Theresa",
        "Marilyn",
        "Danielle",
        "Diana",
        "Brittany",
        "Natalie",
        "Sophia",
        "Rose",
        "Isabella",
        "Alexis",
        "Kayla",
        "Charlotte"
    ]
    names_lists_tuple = (male_names_list, female_names_list)

    # filename indices limits
    min_index = 1
    max_index = 11

    # generate files
    for index in range(min_index, max_index):

        # Create new workbook
        wb = Workbook()
        ws = wb.active

        # Generate first line (labels)
        labels = ["id", "name", "grade"]
        ws.append(labels)

        # Generate remaining 49 lines (actual values)
        min_row = 2
        max_row = 51
        for row in range(min_row, max_row):
            # generate random uid
            min_uid = 10**8
            max_uid = 10**9
            random_uid = randrange(min_uid, max_uid)

            # generate random name
            random_list = choice(names_lists_tuple)
            random_name = choice(random_list)

            # generate random grade
            min_grade = 0
            max_grade = 101
            random_grade = randrange(min_grade, max_grade)

            # generate row with random values
            random_row = (random_uid, random_name, random_grade)

            # append row to workbook
            ws.append(random_row)

        # generate grades distribution chart
        min_col = max_col = labels.index("grade") + 1
        grades_values = chart.Reference(ws, min_col, min_row, max_col, max_row)
        grades_chart = chart.BarChart()
        grades_chart.add_data(grades_values)

        # add generated chart to worksheet
        chart_row = 1
        chart_col = ascii_lowercase[len(labels)]
        ws.add_chart(grades_chart, f"{chart_col}{chart_row}")

        # Write to new .xlsx file
        filename = f"data\\students{index}.xlsx"
        wb.save(filename)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
