import json
class Dummy:
  def __init__(self, arg):
        self.arg = arg
  def dummy(self):
        argument = self.arg
        one = argument[0].split( )
        start=len(one)
        two = argument[1].split( )
        length=len(two)
        end=start-length
        endresult = one[1 :end]
        endresult =  " ".join(endresult)
        print(json.dumps({"result":[{"output" : str(endresult) }]}))
