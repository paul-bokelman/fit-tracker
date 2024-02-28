from datetime import date, datetime
from termcolor import colored
from lib.utils import config, subfield, success

def log_weight():
    weight = subfield('Enter weight: ')
    current_date = date.today()
    current_time = datetime.now().strftime("%H:%M:%S")

    with open('data/weight-log.csv', 'a') as f:
        f.write(f'{current_date},{current_time},{weight}\n')

    success('\nWorkout logged successfully.')


def log_workout(): 
    workout_id = input(f'Enter workout id ({colored("A", color="blue")}/{colored("B", color="yellow")}): ')
    if(workout_id != 'A' and workout_id != 'B'):
        print('Invalid workout id')
        return
    
    workout_names = []
    workout_weights = []
    
    if(workout_id == 'A'):
        for workout in config['workouts']['A']:
            weight = subfield(f'{workout} weight: ')
            workout_names.append(workout)
            workout_weights.append(weight)

    if(workout_id == 'B'):
        for workout in config['workouts']['B']:
            weight = subfield(f'{workout} weight: ')
            workout_names.append(workout)
            workout_weights.append(weight)
    
    workout_time = datetime.now().strftime("%H:%M:%S")
    workout_date = date.today()

    with open('data/workout-log.csv', 'a') as f:
        f.write(f'{workout_id},{workout_date},{workout_time},{";".join(workout_names)},{";".join(workout_weights)}\n')

    success('\nWorkout logged successfully.')