import time

def countdown(seconds):
  """Counts down from a given number of seconds and prints a message when the time is up."""
  while seconds > 0:
    minutes = seconds // 60
    seconds = seconds % 60
    print("{}:{}".format(minutes, seconds))
    time.sleep(1)
    seconds -= 1
  print("Time's up!")

if __name__ == "__main__":
  seconds = int(input("Enter the number of seconds to count down: "))
  countdown(seconds)
