
def battery_is_ok(temperature, soc, charge_rate,function):
    
    return isTemperatureOk(temperature,function) and isSocOk(soc,function) and isChargeRateOk(charge_rate,function)

 
def isTemperatureOk(temperature,function):
  if temperature >0 and temperature < 45:
    function("Temperature is Okay")
    return True
  return False

def isSocOk(soc,function):
  if soc > 20 and soc < 80:
    function("Temperature is Okay")
    return True
  return False

def isChargeRateOk(charge_rate,function):
  if charge_rate < 0.8:
    
    function("Temperature is Okay")
    return True
  return False


def print_string(str):
  print(str)
  return None


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7,print_string) is True)
  assert(battery_is_ok(50, 85, 0,print_string) is False)
