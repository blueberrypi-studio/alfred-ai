from skills import *

def get_skills():
    
    return [x for x in globals() if hasattr(globals()[str(x)], '__custom__')]


run_skill = "Read_Notes"

m = globals()[run_skill]()


if run_skill in skills:
    func = getattr(m, run_skill.lower())()

