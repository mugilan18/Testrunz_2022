import json
import math


class Sdic:
    def __init__(self, arg):
        self.arg = arg
    def opamp_amplification(self):
        argument = self.arg[:]
        rf = float(argument[1])
        rin =float(argument[2])
        vo1=-1*(rf/rin)*(float(argument[3])+float(argument[4]))
        vo2=-1*(rf/rin)*(float(argument[5])+float(argument[6]))
        vo3=-1*(rf/rin)*(float(argument[7])+float(argument[8]))
        vot1=-1*(float(argument[3])+float(argument[4]))
        vot2=-1*(float(argument[5])+float(argument[6]))
        vot3=-1*(float(argument[7])+float(argument[8]))
        print(json.dumps({"answer":[{"The experimental Vo are":str(vo1)+" , "+str(vo2)+" and "+str(vo3),"The theoretical Vo are":str(vot1)+" , "+str(vot2)+" and "+str(vot3)}]}))
    def logantilog(self):
        argument = self.arg[:]
        vd1=float(argument[1])-float(argument[2])
        vd2=float(argument[4])-float(argument[5])
        vd3=float(argument[7])-float(argument[8])
        vd4=float(argument[10])-float(argument[11])
        vd5=float(argument[13])-float(argument[14])
        vop1=float(argument[3])
        vop2=float(argument[6])
        vop3=float(argument[9])
        vop4=float(argument[12])
        vop5=float(argument[15])
        gain1= vop1/vd1
        gain2= vop2/vd2
        gain3= vop3/vd3
        gain4= vop4/vd4
        gain5= vop5/vd5
        vot1=round(gain1*vd1,3)
        vot2=round(gain2*vd2,3)
        vot3=round(gain3*vd3,3)
        vot4=round(gain4*vd4,3)
        vot5=round(gain5*vd5,3)
        print(json.dumps({"answer":[{"The experimental Vo are":str(vop1)+" , "+str(vop2)+" , "+str(vop3)+" , "+str(vop4)+" and "+str(vop5),"The theoretical Vo are":str(vot1)+" , "+str(vot2)+" , "+str(vot3)+" , "+str(vot4)+" and "+str(vot5)}]}))








