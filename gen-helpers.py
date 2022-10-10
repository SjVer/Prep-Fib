MAX_I = 19
MAX_T = 2585
MAX_R = 4182

def w(s): f.write(s + "\n")
def else_error(msg, t = 0):
    w("#" + "\t" * t + "else")
    w("#" + "\t" * t + f"\terror \"{msg}\"")
    w("#" + "\t" * t + "endif")

# i = i + 1
with open("helper_incr_i.h", "w") as f:

    w("#if false")
    for i in range(1, MAX_I):
        w(f"#elif I == {i}")
        w("#\tundef I")
        w(f"#\tdefine I {i + 1}")
    else_error("maximum inclusion depth reached")

# {r/tt} = t1 + t2
with open("helper_add_ts.h", "w") as f:

    w("#if false")
    for i in range(1, MAX_R):
        w(f"#elif T1 + T2 == {i}")
        w("#\tifdef TO_R")
        w("#\t\tundef TO_R")
        w(f"#\t\tdefine R {i}")
        w("#\tendif")

        w("#\tifdef TO_TT")
        w("#\t\tundef TO_TT")
        w(f"#\t\tundef TT")
        w(f"#\t\tdefine TT {i}")
        w("#\tendif")
    else_error("T1 + T2 overflowed")

# t2 = t1 / t2 = tt
with open("helper_copy.h", "w") as f:

    w("#ifdef T2_TO_T1")
    w("#\tundef T2_TO_T1")
    w("#\tif false")
    for i in range(1, MAX_T):
        w(f"#\telif T2 == {i}")
        w("#\t\tundef T1")
        w(f"#\t\tdefine T1 {i}")
    else_error("T2 overflowed", t = 1)
    w("#endif")

    w("#ifdef TT_TO_T2")
    w("#\tundef TT_TO_T2")
    w("#\tif false")
    for i in range(1, MAX_T):
        w(f"#\telif TT == {i}")
        w("#\t\tundef T2")
        w(f"#\t\tdefine T2 {i}")
    else_error("TT overflowed", t = 1)
    w("#endif")