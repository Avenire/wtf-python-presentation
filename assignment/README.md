# Assignment
Gotcha: when executing tests against `functions_before.py` module we get 
`UnboundLocalError: local variable <var> referenced before assignment` errors.
By default when Python sees assigment in the body of function to label not defined in that scope it assumes
we want to create a local variable. Then, if the same label appears on the ride side of assignment, Python will
freak out as you cannot use a variable you just define! To fix it we need to use `global` and `nonlocal` keywords 
to explicitly tell python we want to mutate objects from outer scope. Notice that these keywords are not required
as long as you only read outer-scope variables (as tests do not fail at `getter()` or `a_getter()` invocations).