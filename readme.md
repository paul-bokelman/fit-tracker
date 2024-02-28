# Local fitness tracker

A simple fitness tracker that allows you to track and visualize your daily workouts and weight.

## Features

- Log Weight
- Log Workout
- View Previous Workouts
- View Weights
- View Progress (graphs)

## Usage

```bash
python3 tracker.py
```

### Local files

All data is stored in local files. The following files are used:

`data/weight-log.csv`

```csv
date,time,weight
x,x,x
```

`data/workout-log.csv`

```csv
id,date,time,names,weights
x,x,x,x,x
```

`config.json`

```json
{
  "maintenance_calories": 2200,
  "workouts": {
    "A": ["Bench", "Incline Bench", "Overhead Press", "Squat"],
    "B": ["Pull-up", "Barbell Row", "Deadlift", "Curl"]
  }
}
```
