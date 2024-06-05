import inspect

def goober():
    goob_name = "g_o_o_b_e_r".replace("_", "")
    print(f"This function should not be named {goob_name} anymore")
    function_name = inspect.stack()[0][3]
    print(f"Function name is: {function_name}")

goober()
