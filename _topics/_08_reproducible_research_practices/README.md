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
    <PackageReference Include="YamlDotNet" Version="16.2.1" />
```

