def w(s): f.write(s + "\n")
r = range(1, 101)
def else_error(msg, t = 0):
    w("#" + "\t" * t + "else")
    w("#" + "\t" * t + f"\tpragma error \"{msg}\"")
    w("#" + "\t" * t + "endif")

f = open("helper_sub_n.h", "w")

# n = n - 1
w("#if false")
for i in r:
    w(f"#elif N == {i}")
    w(f"#\tundef N")
    w(f"#\tdefine N {i - 1}")
else_error("N overflowed")

f.close()
f = open("helper_store_n.h", "w")

# store n / load n
w("#ifndef LOAD")
w("#\tundef N")
w("#endif\n")
w("#if false")
for i in r:
    w(f"#elif __INCLUDE_LEVEL__ == {i}")
    w("#\tifdef LOAD")
    w("#\t\tif false")
    for ii in r:
        w(f"#\t\telif N_{i} == {ii}")
        w(f"#\t\t\tdefine N {ii}")
    w("#\t\tendif")
    w("#\telse")
    w("#\t\tif false")
    for ii in r:
        w(f"#\t\telif N == {ii}")
        w(f"storing {ii} in N_{i}")
        w(f"#\t\t\tdefine N_{i} {ii}")
    w("#\t\tendif")
    w("#\tendif")
else_error("Recursion limit reached!")
w("\n#ifdef LOAD")
w("#\tundef LOAD")
w("#endif")

f.close()
f = open("helper_store_r.h", "w")

# r{1/2} = r
w("#if false")
for i in range(0, 101):
    w(f"#elif R == {i}")
    w(f"#\tif DEST == 1")
    w(f"#\t\tdefine R1 {i}")
    w(f"#\telif DEST == 2")
    w(f"#\t\tdefine R2 {i}")
    w(f"#\tendif")
else_error("R overflowed")
w("#undef DEST")
w("#undef R")

f.close()
f = open("helper_add_rs.h", "w")

# r = r1 + r2
w("#if false")
for i1 in range(0, 101):
    w(f"#elif R1 == {i1}")
    w("#\tif false")
    for i2 in range(0, 101):
        w(f"#\telif R2 == {i2}")
        w(f"#\t\tdefine R {i1 + i2}")
    else_error("R2 overflowed", 1)
else_error("R1 overflowed")
w("#undef R1")
w("#undef R2")

f.close()