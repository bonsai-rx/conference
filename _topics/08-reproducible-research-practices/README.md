# 08 - Reproducible Research Practices

## Bonsai SGen demo

### Getting Started

1. Clone the repository and navigate to this document directory. This will be used as the working directory for the rest of the demo.
2. Install the dotnet tool dependencies by running `dotnet tool restore`.
3. Install python, create a virtual environment, and install pydantic by running:
```powershell
python -m venv .venv
.venv/scripts/activate
pip install pydantic
```
4. Install Bonsai from by running `.bonsai/setup.ps1`. This will bootstrap the environment with the necessary dependencies.
5. Ensure that the `src/bonsai/Extensions.csproj` defines the following dependencies:
```xml
    <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
    <PackageReference Include="YamlDotNet" Version="13.1.1" />
```

6. The repository has two demos: `demo1` and `demo2`. They can be identically. For `demo1`:
7. Compile the schema and create a valid instance by running the `./src/python/demo1.py` script.
8. Run the corresponding bonsai workflow by running the `./src/bonsai/demo1.bonsai` script.
9. Analysis for both demos can be found in the `./src/python/analysis.py` script.
