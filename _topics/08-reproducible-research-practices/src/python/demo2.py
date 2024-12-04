from pydantic import BaseModel, Field
from typing import List, Optional, Annotated, Union, Literal
from _utils import (
    export_schema,
    bonsai_sgen,
    BonsaiSgenSerializers,
    pascal_to_snake_case,
)
from pathlib import Path

from typing_extensions import TypeAliasType


class _TrialBase(BaseModel):
    trial_type: str
    inter_trial_interval: float = Field(
        default=1.0, ge=0, description="Interval between trials in seconds"
    )
    reward_amount: int = Field(
        default=1, ge=0, description="Amount of reward given to the animal"
    )


class GoTrial(_TrialBase):
    trial_type: Literal["go_trial"] = "go_trial"
    cue: str = Field(description="Cue presented to the animal")


class NoGoTrial(_TrialBase):
    trial_type: Literal["nogo_trial"] = "nogo_trial"
    penalty: int = Field(description="Penalty for incorrect response")


Trial = TypeAliasType(
    "Trial", Annotated[Union[GoTrial, NoGoTrial], Field(discriminator="trial_type")]
)


class ExperimentGoNoGo(BaseModel):
    animal_id: str = Field(description="ID of the animal")
    trials: List[Trial] = Field(description="List of trials in the experiment")
    rng_seed: Optional[int] = Field(
        default=None, description="Seed for the random number generator"
    )


if __name__ == "__main__":
    json_schema = export_schema(ExperimentGoNoGo)
    schema_name = ExperimentGoNoGo.__name__
    schema_path = Path(rf"src/json/{pascal_to_snake_case(schema_name)}-schema.json")
    with open(schema_path, "w", encoding="utf-8") as f:
        f.write(json_schema)

    bonsai_sgen(
        schema_path=schema_path,
        output_path=Path(rf"src/bonsai/Extensions/{schema_name.capitalize()}.cs"),
        namespace=schema_name.capitalize(),
        serializer=[BonsaiSgenSerializers.JSON, BonsaiSgenSerializers.YAML],
    )

    experiment_example = ExperimentGoNoGo(
        animal_id="my_mouse",
        trials=[
            GoTrial(inter_trial_interval=1.0, reward_amount=1, cue="light"),
            NoGoTrial(inter_trial_interval=0.5, reward_amount=0, penalty=10),
        ],
    )

    with open(
        rf"src/json/{pascal_to_snake_case(schema_name)}-example.json",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(experiment_example.model_dump_json(indent=2))
