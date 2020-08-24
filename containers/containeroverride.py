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

HelloContainerOverrideTool = j.CommandToolBuilder(
    tool="HelloContainerOverrideTool",  # <- Matching this toolID
    container="ubuntu:latest",
    version="development",
    base_command="echo",
    inputs=[j.ToolInput("inp", j.String, position=0, default="Hello, World!")],
    outputs=[j.ToolOutput("out", j.String, selector=j.standard.ReadContents(j.Stdout()))],
)

# We can swap the container out during translation (and also during running with the CLI)
# by providing the container_override={"ToolID": "containerToOverride"}
#   NB: the toolId must match what's in `tool="HelloContainerOverrideTool"`,
#   not the variable you've assigned the tool to.
#   You can also use {"*": "newcontainer"} to match all tools.

HelloContainerOverrideTool.translate(
    "wdl", container_override={"HelloContainerOverrideTool": "ubuntu:bionic"}
)

# OR bash (you might want to add --skip-digest-lookup to more easily confirm if it's the right version:
# janis translate \
#   --container-override HelloContainerOverrideTool=ubuntu:bionic \
#   --skip-digest-lookup \
#   HelloContainerOverrideTool wdl
