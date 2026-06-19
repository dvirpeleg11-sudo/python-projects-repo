def return_machpela(num1: int, num2: int) -> int:
  return num1 * num2

def return_mana(num1: int, num2: int) -> int:
  mana = 0
  # could just return num1 // num2
  # other way to do it with a while loop
  if num2 == 0:
    print("iligall")
    return
  while num1 >= num2 and num2 != 0:
    num1 -= num2
    mana += 1
  return mana
