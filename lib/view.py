import pandas as pd
from termcolor import colored
from lib.utils import config
from matplotlib import pyplot as plt
plt.style.use('ggplot')

def view_progress():
    weights_df = pd.read_csv('data/weight-log.csv')
    workouts_df = pd.read_csv('data/workout-log.csv')
    weights_df['date'] = pd.to_datetime(weights_df['date']).dt.strftime('%m/%d')
    workouts_df['date'] = pd.to_datetime(workouts_df['date']).dt.strftime('%m/%d')
    weights_df.set_index('date', inplace=True)
    workouts_df.set_index('date', inplace=True)
    
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax[0].plot(weights_df.index, weights_df['weight'], color='black')
    ax[0].set_title('Weight Progress')
    ax[0].set_xlabel('Date')
    ax[0].set_ylabel('Weight (lbs)')

    # todo: plot workouts (by weight and workout name) together
    ax[1].plot(workouts_df.index, workouts_df['weights'], color='blue')
    ax[1].set_title('Workout Progress')
    ax[1].set_xlabel('Date')
    ax[1].set_ylabel('Weight (lbs)')


    # for (index, name) in enumerate(config['workouts']['A']):
    #     ax[1, 0].plot(workouts_df.index, workouts_df['weights'].str.split(';').str[index].astype(int), label=name)
    # ax[1, 0].set_title('Workout A Progress')
    # ax[1, 0].set_xlabel('Date') 
    # ax[1, 0].set_ylabel('Weight (lbs)')
    # ax[1, 0].legend( borderaxespad=0, bbox_to_anchor=(1.04, 1))

    plt.show()

def view_previous_workout():
    print(colored("Previous workouts:", color="yellow", attrs=["bold"]))
    workouts_df = pd.read_csv('data/workout-log.csv')
    mask_A, mask_B = workouts_df['id'] == "A", workouts_df['id'] == "B"
    workout_A = workouts_df[mask_A][-1:].drop(columns=['id', 'time'])
    workout_B = workouts_df[mask_B][-1:].drop(columns=['id', 'time'])
    weights_A, weights_BB = workout_A['weights'].iloc[0].split(";"), workout_B['weights'].iloc[0].split(";")
    
    print(colored(f"\nWorkout A ({workout_A['date'].iloc[0]}):", color="white", attrs=["bold"]))
    for (index, name) in enumerate(config['workouts']['A']):
        print(f"{colored(name, color='grey')}: {weights_A[index]} lbs")
    
    print(colored(f"\nWorkout B ({workout_B['date'].iloc[0]}):", color="white", attrs=["bold"]))
    for (index, name) in enumerate(config['workouts']['B']):
        print(f"{colored(name, color='grey')}: {weights_BB[index]} lbs")

    

def view_previous_weight():
    print(colored("Weight Log:\n", color="yellow", attrs=["bold"]))
    weights_df = pd.read_csv('data/weight-log.csv')[-5:]
    pd.options.display.date_dayfirst = True
    weights_df.drop(columns=['time'], inplace=True)
    print(weights_df.to_string(index=False))