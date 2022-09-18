Mutatest diagnostic summary
===========================
 - Source location: /mnt/c/Users/alfre/mi-repo/Testing/G17-Testing/T4/clock-display/src
 - Test commands: ['pytest']
 - Mode: s
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 15
 - Location sample coverage: 66.67 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.327892
 - Clean trial 2 run time: 0:00:01.537191
 - Mutation trials total run time: 0:00:50.632382

Overall mutation trial summary
==============================
 - DETECTED: 39
 - TOTAL RUNS: 39
 - RUN DATETIME: 2022-09-17 21:30:25.239278


Mutations by result status
==========================


DETECTED
--------
 - src/clock_display.py: (l: 4, c: 38) - mutation from None to True
 - src/clock_display.py: (l: 4, c: 38) - mutation from None to False
 - src/clock_display.py: (l: 8, c: 25) - mutation from <class '_ast.Sub'> to <class '_ast.Add'>
 - src/clock_display.py: (l: 8, c: 25) - mutation from <class '_ast.Sub'> to <class '_ast.Div'>
 - src/clock_display.py: (l: 8, c: 25) - mutation from <class '_ast.Sub'> to <class '_ast.Mult'>
 - src/clock_display.py: (l: 8, c: 25) - mutation from <class '_ast.Sub'> to <class '_ast.Mod'>
 - src/clock_display.py: (l: 8, c: 25) - mutation from <class '_ast.Sub'> to <class '_ast.Pow'>
 - src/clock_display.py: (l: 8, c: 25) - mutation from <class '_ast.Sub'> to <class '_ast.FloorDiv'>
 - src/clock_display.py: (l: 10, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - src/clock_display.py: (l: 10, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - src/clock_display.py: (l: 10, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - src/clock_factory.py: (l: 5, c: 26) - mutation from None to False
 - src/clock_factory.py: (l: 5, c: 26) - mutation from None to True
 - src/display_number.py: (l: 3, c: 41) - mutation from None to False
 - src/display_number.py: (l: 3, c: 41) - mutation from None to True
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Sub'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Mult'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.FloorDiv'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Pow'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Div'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Mod'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Pow'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Mult'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.FloorDiv'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Div'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Mod'>
 - src/display_number.py: (l: 9, c: 23) - mutation from <class '_ast.Add'> to <class '_ast.Sub'>
 - src/display_number.py: (l: 17, c: 8) - mutation from If_Statement to If_True
 - src/display_number.py: (l: 17, c: 8) - mutation from If_Statement to If_False
 - src/display_number.py: (l: 17, c: 11) - mutation from <class '_ast.Lt'> to <class '_ast.Gt'>
 - src/display_number.py: (l: 17, c: 11) - mutation from <class '_ast.Lt'> to <class '_ast.NotEq'>
 - src/display_number.py: (l: 17, c: 11) - mutation from <class '_ast.Lt'> to <class '_ast.GtE'>
 - src/display_number.py: (l: 17, c: 11) - mutation from <class '_ast.Lt'> to <class '_ast.LtE'>
 - src/display_number.py: (l: 17, c: 11) - mutation from <class '_ast.Lt'> to <class '_ast.Eq'>
 - src/display_number.py: (l: 22, c: 15) - mutation from <class '_ast.Lt'> to <class '_ast.LtE'>
 - src/display_number.py: (l: 22, c: 15) - mutation from <class '_ast.Lt'> to <class '_ast.NotEq'>
 - src/display_number.py: (l: 22, c: 15) - mutation from <class '_ast.Lt'> to <class '_ast.Gt'>
 - src/display_number.py: (l: 22, c: 15) - mutation from <class '_ast.Lt'> to <class '_ast.Eq'>
 - src/display_number.py: (l: 22, c: 15) - mutation from <class '_ast.Lt'> to <class '_ast.GtE'>