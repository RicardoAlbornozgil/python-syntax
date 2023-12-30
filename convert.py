def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0

    celsius -> farenheit
     (temp * 1.8) + 32

     farenheit -> celsius
     (temp - 32) / 1.8

    """

    if unit_in != "c" and unit_in != "f":
        print("Error 1")
        return f"Invalid unit [{unit_in}]"
    
    elif unit_out != "c" and unit_out != "f":
        print("Error 2")
        return f"Invalid unit [{unit_out}]"
  
    elif unit_in == unit_out:
        print("Error 3")
        return temp
    else:  
        if unit_in == "c":
            print("Error 4")
            return (temp * 1.8) + 32
        else:
            print("Error 5")
            return (temp - 32) / 1.8
    
  
    


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

