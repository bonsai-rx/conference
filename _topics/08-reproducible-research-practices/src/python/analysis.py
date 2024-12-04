from demo1 import Experiment, Trial
from pathlib import Path

data_path = Path(r"src/data/demo1.json")
task_spec = Path(r"src/json/experiment-example.json")
with open(data_path, "r", encoding="utf-8") as f:
    trials = [Trial.model_validate_json(x) for x in f.readlines()]

# print all trials
[print(trial) for trial in trials]
# print total reward consumed
reward_consumed = sum([trial.reward_amount for trial in trials])
print(f"Animal consumed a total of {reward_consumed} ml")

# print the task settings that gave rise to the trials
with open(task_spec, "r", encoding="utf-8") as f:
    task_settings = Experiment.model_validate_json(f.read())
print(task_settings)
