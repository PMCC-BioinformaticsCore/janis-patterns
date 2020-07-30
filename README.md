# janis-patterns
A repository of common Janis patterns

This repository is _work-in-progress_. Please raise an issue if there are patterns you think would be valuable in this repository.

## Contents

<Generate this later>

## Declaring types

- Janis types
- 

> Although not preferred, Janis allows you to present Python types, for example:
> ```python
> from typing import Optional, List
> from janis_core import String, Array
> 
> workflow.input("my_string_inpuy", String())
> workflow.input("my_string_input", str)
>
> workflow.input("my_optional_str_input", String(optional=True))
> workflow.input("my_optional_str_input", Optional[str])
>
> workflow.input("my_list_of_strings_input", Array(String()))
> workflow.input("my_list_of_strings_input", List[str])
>
> workflow.input("my_optional_list_of_strings", Array(String(), optional=True))
> workflow.input("my_optional_list_of_strings", Optional[List[str]])
>
> workflow.input("my_list_of_optional_strings", Array(String(optional=True)))
> workflow.input("my_list_of_optional_strings", List[Optional[str]])
> ```

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