#Emily Rusch
#Q31
def e_function(x):
    count = 0
    for ch in x:
        if ch == "e":
            count = count + 1
    print(count)

e_function("unforeseeable")
