# Default args
Gotcha: when Python loads module and processes function definition default values are created and
stored statically in `__defaults__` attribute of function. If default value is mutable object then
when function is called with such default value bound to argument name all sorts of surprises can happen.