import inquirer
from termcolor import colored
from lib.log import log_weight, log_workout
from lib.view import view_progress, view_previous_workout, view_previous_weight

choices = {
    'Log Weight': 'weight',
    'Log Workout': 'workout',
    "View Previous Workouts": "view_workouts",
    "View Weights": "view_weights",
    'View Progress': 'progress',
    colored("Exit", color="red"): "exit"
}

print(colored("\nWorkout Tracker", color="green", attrs=["bold", "underline"]))

while True:
    print("")
    questions = [inquirer.List('option', message="Choose an option", choices=[key for key in choices.keys()])]
    answers = inquirer.prompt(questions) 

    if answers:
        option = choices[answers['option']]
        match option:
            case 'weight':
                log_weight()
            case 'workout':
                log_workout()
            case 'view_workouts':
                view_previous_workout()
            case 'view_weights':
                view_previous_weight()
            case 'progress':
                view_progress()
            case 'exit':
                exit(0)
    else:
        exit(1)