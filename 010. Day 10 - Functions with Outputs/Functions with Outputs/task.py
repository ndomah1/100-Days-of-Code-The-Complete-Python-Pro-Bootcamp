# Using print()
def format_name(f_name, l_name):
    """
    print(f_name.title())
    print(l_name.title())
    """
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    print(f"{formatted_f_name} {formatted_l_name}")

format_name("nIlEsH", "DomAH")

# Using return
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("nIlEsH", "DomAH"))

# return allows you to save the output and re_use
formatted_name = format_name("nIlEsH", "DomAH")
print(formatted_name)
