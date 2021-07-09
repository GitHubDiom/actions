import math
import time
cold = True

def main(args):
    global cold
    was_cold = cold
    cold = False
    name = args.get("name", "stranger")
    greeting = "Hello " + name + " from python!"
    time.sleep(5)
    return {"greeting": greeting}
