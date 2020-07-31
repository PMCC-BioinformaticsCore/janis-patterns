# janis-patterns

This is a place for documenting common patterns that you might want to achieve using Janis. This repository is _work-in-progress_. Please raise an issue if there are patterns you think would be valuable in this repository.

## Contents

<Generate this later>

## Quick debugging tip

The quickest way to verify whether your janis workflow / command tool is connected correctly, is to translate it to CWL or WDL. There are two quick ways to do that:

> We usually recommend WDL to verify, as it's intuitive to compare the command line and connections.

1. Add the following block of code to your python file, then run the file:
    ```python
    if __name__ == "__main__":
        YourWorkflowOrTool().translate(
            "wdl", to_console=True
        )
    ```

2. OR, translate using the command line:

    ```bash
    $ janis translate yourpythonfile.py wdl # or cwl
    ```


## Declaring types

- Janis types
- Python Types (types/pythontypes.py)



## Command line declaration

### Regular

- Positional arguments
- Arguments with a prefix

- Array arguments:
    - Separator
    - 

### Advanced

- Joining multiple commmands together

## Scatter execution

The [scatter](#https://github.com/PMCC-BioinformaticsCore/janis-patterns/blob/master/scatter) folder 

- Regular scatter (by a single field).
- Scatter by multiple fields:
    - Dot Product - For each corresponding entries in the inputs (must have the same length).
    - Cross product - For every combination of items (distributive).


## Workflow vs Workflow Builder