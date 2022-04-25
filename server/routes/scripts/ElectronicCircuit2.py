import json
import math 

class EC2:
    def __init__(self, arg):
        self.arg = arg
    def VOLTAGE(self):
        argument = self.arg[0:]
        dB1 = 20*math.log(float(argument[3])/float(argument[2]))
        dB2 = 20*math.log(float(argument[6])/float(argument[5]))
        dB3 = 20*math.log(float(argument[9])/float(argument[8]))
        dB4 = 20*math.log(float(argument[12])/float(argument[11]))
        dB5 = 20*math.log(float(argument[15])/float(argument[14]))
        dB=(dB1+dB2+dB3+dB4+dB5)/5
        print(json.dumps({"answer":[{"result":"Thus the current series feedback amplifier is designed and constructed and the  following parameters are calculated ","Ans":dB}]}))

    def SHUNT(self):
        argument = self.arg[0:]
        dB1 = 20*math.log(float(argument[3])/float(argument[2]))
        dB2 = 20*math.log(float(argument[6])/float(argument[5]))
        dB=(dB1+dB2)/2
        print(json.dumps({"answer":[{"result":"Thus the current series feedback amplifier is designed and constructed and the  following parameters are calculated ","Ans":dB}]}))

    def PHASE(self):
        print(json.dumps({"answer":[{"result":"Thus the RC phase shift oscillator was designed and its output waveform was verified"}]}))
    def HARTLEY(self):
        print(json.dumps({"answer":[{"result":"Thus the Hartley oscillator and Colpitts oscillator was designed and its output waveform was verified. "}]}))
    def ASTABLE(self):
        print(json.dumps({"answer":[{"result":"Thus the Astable multivibrator and Monostable  was designed and its output waveform was verified. "}]}))
    def BISTABLE(self):
        print(json.dumps({"answer":[{"result":"Thus the Bistable multivibrator was designed and its output waveform was verified."}]}))
    def CLASS_A(self):
        argument = self.arg[0:]
        dB1 = 20*math.log(float(argument[1])/float(argument[2]))
        dB2 = 20*math.log(float(argument[3])/float(argument[4]))
        dB3 = 20*math.log(float(argument[5])/float(argument[6]))
        dB4 = 20*math.log(float(argument[7])/float(argument[8]))
        dB5 = 20*math.log(float(argument[9])/float(argument[10]))
        dB=(dB1+dB2+dB3+dB4+dB5)/5
        print(json.dumps({"answer":[{"result":"Thus Class A complementary symmetry  power amplifier is verified","Ans":dB}]}))
    def CLASS_B(self):
        argument = self.arg[0:]
        dB1 = 20*math.log(float(argument[3])/float(argument[1]))
        dB2 = 20*math.log(float(argument[5])/float(argument[1]))
        dB3 = 20*math.log(float(argument[6])/float(argument[1]))
        dB4 = 20*math.log(float(argument[9])/float(argument[1]))
        dB5 = 20*math.log(float(argument[11])/float(argument[1]))
        print(json.dumps({"answer":[{"result":"Thus class B complementary symmetry  power amplifier is verified","Ans":dB}]}))
    def ASTABLE(self):
        print(json.dumps({"answer":[{"result":"Thus the Astable multivibrator and Monostable  was designed and its output waveform was verified. "}]}))
    def TIME(self):
        print(json.dumps({"answer":[{"result":"Thus the Astable multivibrator and Monostable  was designed and its output waveform was verified. "}]}))


