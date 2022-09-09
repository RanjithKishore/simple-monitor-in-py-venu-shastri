
def battery_is_ok(temperature, soc, charge_rate):
  #CALL fxns
    return isTemperatureOk(temperature) and isSocOk(soc) and isChargeRateOk(charge_rate)
def isTemperatureOk(temperature):
  if temperature >0 and temperature < 45:
    #print_string('Temperature is out of range!')
    return True
  return False
def isSocOk(soc):
  if soc > 20 and soc < 80:
    #print_string('State of Charge is out of range!')
    return True
  return False

def isChargeRateOk(charge_rate):
  if charge_rate < 0.8:
    #print_string('Charge rate is out of range! ')
    return True
  return False

def print_string(str):
  print(str)
  return None


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
