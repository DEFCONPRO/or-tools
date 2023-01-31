#!/usr/bin/env python3
# Copyright 2010-2022 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Non linear example.

Finds a rectangle with maximum available area for given perimeter using
AddMultiplicationEquality().
"""

from ortools.sat.python import cp_model


def non_linear_sat():
    """Non linear sample."""
    perimeter = 20

    model = cp_model.CpModel()

    x = model.NewIntVar(0, perimeter, 'x')
    y = model.NewIntVar(0, perimeter, 'y')
    model.Add(2 * (x + y) == perimeter)

    area = model.NewIntVar(0, perimeter * perimeter, 's')
    model.AddMultiplicationEquality(area, x, y)

    model.Maximize(area)

    solver = cp_model.CpSolver()

    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print('x = %i' % solver.Value(x))
        print('y = %i' % solver.Value(y))
        print('s = %i' % solver.Value(area))
    else:
        print('No solution found.')


non_linear_sat()
