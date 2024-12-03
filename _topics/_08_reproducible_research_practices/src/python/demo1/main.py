from pydantic import BaseModel, Field
from typing import List, Optional
from _utils import export_schema, bonsai_sgen, BonsaiSgenSerializers
from pathlib import Path


class Trial(BaseModel):
    inter_trial_interval: float = Field(
        default=1.0, ge=0, description="Interval between trials in seconds"
    )
    reward_amount: int = Field(
        default=1, ge=0, description="Amount of reward given to the animal"
    )


class Experiment(BaseModel):
    animal_id: str = Field(description="ID of the animal")
    trials: List[Trial] = Field(description="List of trials in the experiment")
    rng_seed: Optional[int] = Field(
        default=None, description="Seed for the random number generator"
    )


if __name__ == "__main__":
    json_schema = export_schema(Experiment)
    name = (Experiment.__name__).lower()
    schema_path = Path(rf"src/json/{name}-schema.json")
    with open(schema_path, "w", encoding="utf-8") as f:
        f.write(json_schema)

    bonsai_sgen(
        schema_path=schema_path,
        output_path=Path(rf"src/bonsai/Extensions/{name.capitalize()}.cs"),
        namespace=name.capitalize(),
        serializer=[BonsaiSgenSerializers.JSON, BonsaiSgenSerializers.YAML],
    )

    experiment_example = Experiment(
        animal_id="my_mouse",
        trials=[
            Trial(inter_trial_interval=1.0, reward_amount=1),
            Trial(inter_trial_interval=0.5, reward_amount=0),
        ],
    )

    with open(rf"src/json/{name}-example.json", "w", encoding="utf-8") as f:
        f.write(experiment_example.model_dump_json(indent=2))
