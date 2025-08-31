#Functions with output

def function1():
    result = 3+2
    return result
 # Return is the output keyword

function1()


def format_name(f_name, l_name):
    if f_name == "" or l_name =="":
        return ""
    formated_f = f_name.title()
    formated_l = l_name.title()
    return f"{formated_f} {formated_l}"

format_name("MoIn", "KhAn")


#Return is basically the end of a function. No line of code in the function will be executed after it.
#However, based on the indentation and it's use case, you can have multiple return in the function as well. 
# E.G: inside and if statement and if the statement is true, you can have an empty return there as well to stop the rest of the function.


