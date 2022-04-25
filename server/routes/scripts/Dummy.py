import json
class Dummy:
  def __init__(self, arg):
        self.arg = arg
  def dummy(self):
        argument = self.arg[0:]
        dumArg =  " ".join(argument)
        print(json.dumps({"result":[{"output" : str(dumArg) }]}))
       