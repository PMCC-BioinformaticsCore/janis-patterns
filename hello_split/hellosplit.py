# Janis - Python framework for portable workflow generation
# Copyright (C) 2020  Michael Franklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# 'Hello, world!' example in Janis
#
# Inspired by the following tutorials:
#     - Nextflow: https://www.nextflow.io/docs/latest/getstarted.html
#     - Snakemake https://github.com/jperkel/Snakemake_example/edit/master/hello_world.smk


import janis_core as j

# We start with our tool definitions


class SplitText(j.PythonTool):
    @staticmethod
    def code_block(inp: str) -> dict:
        # list splits "abc" into ["a", "b", "c"]
        return {"out": list(inp)}

    def outputs(self):
        return [j.TOutput("out", j.Array(j.String()))]


class ToUpper(j.PythonTool):
    @staticmethod
    def code_block(inp: str) -> dict:
        # list splits "abc" into ["a", "b", "c"]
        return {"out": inp.upper()}

    def outputs(self):
        return [j.TOutput("out", j.String())]


# Now that we have our tool definitions, we can construct our workflow

# Workflow definition called "split_and_upper"
wf = j.WorkflowBuilder("split_and_upper")

# The workflow input, which is of type STRING
wf.input("input_text", j.String())

# Create a step called 'split', call `SplitText` that takes a string input called 'inp'.
# The output can be accessed by `wf.split.out`, which will have type Array(String).
wf.step("split", SplitText(inp=wf.input_text))

# Create a step called 'toupper', called the `ToUpper` tool which has a single
# input called 'inp'. Because we're operating on an array, we'll use the `scatter="inp"`
# argument, to scatter over the ToUpper's input called "inp".
# The output will be implicitly _gathered_, and hence `wf.toupper.out` will have type Array(String).
wf.step("toupper", ToUpper(inp=wf.split.out), scatter="inp")

# We'll use the gathered output, and use the janis `j.standard.JoinOperator(iterable, separator)`
# to join the array of strings.
wf.output("out", source=j.standard.JoinOperator(wf.toupper.out, ""))

if __name__ == "__main__":
    # Translating a workflow is great way to confirm that the workflow is correct
    wf.translate("wdl")


# Run with:
#   janis run -o $(pwd) hellosplit.py --input_text "Hello, World!"
