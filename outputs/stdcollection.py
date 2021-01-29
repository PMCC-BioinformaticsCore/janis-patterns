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

import janis_core as j


CLT = j.CommandToolBuilder(
    tool="collecting_std_outputs",
    base_command=["echo", "Hello, World"],
    version="dev", container="ubuntu:latest",
    inputs=[],
    outputs=[
        # stdout
        j.ToolOutput("out_stdout_1", j.Stdout()),
        j.ToolOutput("out_stdout_2", j.File(), selector=j.Stdout()),
        # stderr
        j.ToolOutput("out_stderr_1", j.Stderr()),
        j.ToolOutput("out_stderr_2", j.File(), selector=j.Stderr()),
    ]
)

if __name__ == "__main__":
    CLT.translate("cwl")