
def battery_is_ok(temperature, soc, charge_rate):
  if temperature < 0 or temperature > 45:
    print_string('Temperature is out of range!')
    return False
  elif soc < 20 or soc > 80:
    print_string('State of Charge is out of range!')
    return False
  elif charge_rate > 0.8:
    print_string('Charge rate is out of range! ')
    return False

  return True

def print_string(str):
  print(str)
  return void


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
