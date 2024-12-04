import json
from pydantic import BaseModel

class Gratings(BaseModel):
    x: float
    y: float
    orientation: float

class Trial(BaseModel):
    stimuli: list[Gratings]

class Experiment(BaseModel):
    trials: list[Trial]

if __name__ == "__main__":
    model_schema = Experiment.model_json_schema()
    with open("Experiment.json", 'w', encoding="utf-8") as fp:
        schema_json = json.dumps(model_schema, indent=2)
        fp.write(schema_json)