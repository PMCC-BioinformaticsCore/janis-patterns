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

import os, operator
from typing import Dict, Optional, List, Any

import janis_core as j
from janis_core.tool.test_classes import (
    TTestPreprocessor,
    TTestExpectedOutput,
    TTestCase,
)


def new_lines_diff_operator(cls, output_diff, expected_new_lines):
    """
    Used to process the results of the TTestPreprocessor.FileDiff,
    and confirm the diff contains the expected_new_lines.
    """
    new_lines = []
    for diff_line in output_diff:
        prefix = diff_line[0:3]
        if prefix in ["+++", "---", "@@ "]:
            continue

        if diff_line.startswith("+"):
            diff_line = diff_line.strip()
            diff_line = diff_line[1:]

            new_lines.append(diff_line)

    return new_lines == expected_new_lines


class InsertLineTool(j.PythonTool):
    @staticmethod
    def code_block(
        in_file: j.File, line_to_insert: str, insert_after_line: int
    ) -> Dict[str, Any]:

        dst = "./output.txt"

        with open(in_file, "r") as fin, open(dst, "w") as fout:
            count = 0
            for line in fin:
                count += 1
                fout.write(line)

                if count == insert_after_line:
                    fout.write(line_to_insert + "\n")

        line_count = count + 1

        return {"out_file": dst, "line_count": line_count, "misc_files": [dst]}

    def friendly_name(self) -> Optional[str]:
        return "Insert line to a text file"

    def outputs(self) -> List[j.TOutput]:
        return [
            j.TOutput("out_file", j.File, doc="Single file to compare"),
            j.TOutput("line_count", j.Int, doc="Number of lines in the file"),
            j.TOutput("misc_files", j.Array(j.File), doc="array of output file, to show array index"),
        ]

    def id(self) -> str:
        return "InsertLine"

    def version(self):
        return "v0.1.0"

    def tests(self):
        return [
            TTestCase(
                name="insert-one-line",
                input={
                    "in_file": os.path.join(self.test_data_path(), "input.txt"),
                    "line_to_insert": "abc",
                    "insert_after_line": 1,
                },
                output=[
                    TTestExpectedOutput(
                        tag="out_file",
                        preprocessor=TTestPreprocessor.FileMd5,
                        operator=operator.eq,
                        expected_value="85d7c20f3e0c7af4510ca5d1f4997b9f",
                    ),
                    TTestExpectedOutput(
                        tag="out_file",
                        preprocessor=TTestPreprocessor.FileDiff,
                        file_diff_source=os.path.join(
                            self.test_data_path(), "expected_output_1.txt"
                        ),
                        operator=operator.eq,
                        expected_value=[],
                    ),
                    TTestExpectedOutput(
                        tag="out_file",
                        preprocessor=TTestPreprocessor.FileContent,
                        operator=operator.eq,
                        expected_value="test\nabc\nsame\nsame\nlast line\n",
                    ),
                ],
            ),
            TTestCase(
                name="append-one-line",
                input={
                    "in_file": os.path.join(self.test_data_path(), "input.txt"),
                    "line_to_insert": "my new line",
                    "insert_after_line": 4,
                },
                output=[
                    TTestExpectedOutput(
                        tag="line_count",
                        preprocessor=TTestPreprocessor.Value,
                        operator=operator.eq,
                        expected_value="5",
                    ),
                    TTestExpectedOutput(
                        tag="out_file",
                        preprocessor=TTestPreprocessor.FileDiff,
                        file_diff_source=os.path.join(
                            self.test_data_path(), "input.txt"
                        ),
                        operator=new_lines_diff_operator,
                        expected_value=["my new line"],
                    ),
                    TTestExpectedOutput(
                        tag="misc_files",
                        array_index=1,
                        preprocessor=TTestPreprocessor.FileContent,
                        operator=operator.eq,
                        expected_value="test\nsame\nsame\nlast line\nmy new line\n",
                    ),
                    TTestExpectedOutput(
                        tag="out_file",
                        preprocessor=TTestPreprocessor.FileMd5,
                        operator=operator.eq,
                        expected_value="d680893100be1181c8a7071618ff4524",
                    ),
                ],
            ),
        ]


if __name__ == "__main__":
    # TODO: Add single InsertLineTool().test() method
    pass
