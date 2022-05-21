#!/usr/bin/python
import json
import math

class FirstYPhysics:
    def __init__(self, arg):
        self.arg = arg

    def vibration_magnetometer(self):
        argumentP = self.arg[0:9]
        argument = self.arg[8:]
        L1 = 0.0
        for n in range(1, 10, 2):
            L1 += round(float(argument[n]) + (float(argument[n+1]) * 0.01),1)
        L1 = L1/5
        L2 = 0.0
        for n in range(11, 20, 2):
            L2 += round(float(argument[n]) + (float(argument[n+1]) * 0.01),1)
        L2 = L2/5
        
        B1 = 0.0
        for n in range(21, 30, 2):
            B1 += round((float(argument[n]) + (float(argument[n+1]) * 0.01) + (float(argumentP[6]) * 0.001)),1)
        B1 = B1/5
        
        B2 = 0.0
        for n in range(31, 40, 2):
            B2 += round((float(argument[n]) + (float(argument[n+1]) * 0.01) + (float(argumentP[8]) * 0.001)),1)
        B2 = B2/5
        
        AT1 = 0.0
        for n in range(43, 50, 3):
            AT1 += round((float(argument[n])),1)

        AT2 = 0.0
        for n in range(52, 59, 3):
            AT2 += round((float(argument[n])),1)

        I1 = round(25 * (((L1 * L1)+(B1 * B1))/12), 1)
        I2 = round(25 * (((L2 * L2)+(B2 * B2))/12), 1)
        MM = round((I1/I2) * ((AT1 * AT1)/(AT2 * AT2)), 1)
        print(json.dumps({"length":[{"length of magnet 1 using vernier caliper" : str(L1) + " cm", "length of magnet 2 using vernier caliper" : str(L2) + " cm"}], "breadth":[{"breadth of magnet 1 using screw gauge" : str(B1) + " mm", "breadth of magnet 2 using screw gauge" : str(B2) + " mm"}], "average_time":[{"Calculated average time T1 " : str(AT1/3) + " s", "Calculated average time T2" : str(AT2/3) + " s"}], "interia":[{"The moment of inertia of first magnet I1 " : str(I1) + " kgxmxm", "The moment of inertia of second magnet I2" : str(I2) + " kgxmxm"}], "moment":[{"The ratio of magnetic moment " : str(MM) + " no-units" }] }))

    def Air_wedge(self):
        argument = self.arg[0:]
        argumentP = float(argument[1])
        argumentP1 = float(argument[25])
        β = 0.0
        for n in range(2, 18, 2):
            β += round(float(argument[n]) + (float(argument[n+1]) * argumentP),1)
        β = β/8
        TR1 = 0.0
        for n in range(27, 29, 2):
            TR1 += round(float(argument[n]) + (float(argument[n+1]) * argumentP1),1)

        TR2 = 0.0
        for n in range(29, 31, 2):
            TR2 += round(float(argument[n]) + (float(argument[n+1]) * argumentP1),1)

        l = TR1 - TR2
        t =  round((float(argument[26])*l)/(2*β), 1)
        print(json.dumps({"Distance":[{"The distance between specimen 1 and the edge of contact" : str(l) + " cm"}], "bandwidth":[{"The band width for the given specimen " : str(β) + " cm"}], "tickness":[{"The thickness of the given specimen is found by forming interference fringes using air-wedge arrangement " : str(t) + " m"}]}))

    def Polarimeter(self):
        argument = self.arg[0:]
        argumentP = float(argument[2])

        tita = 0.0
        flag1 = 0
        for n in range(4, 40, 5):
            flag2=0
            flag1 += 1
            for m in range(6, 42, 5):
                flag2 += 1
                if(flag1 == flag2):
                    tita += (round(float(argument[n]) + (float(argument[n+1]) * argumentP),1) + round(float(argument[m]) + (float(argument[m+1]) * argumentP),1))/2

        tita = tita/8

        C = 0.0
        for n in range(3, 39, 5):
            C += (round(float(argument[n])))

        C = C/8
    
        S = round(tita/(argumentP*C))
        print(json.dumps({"Specific_rotation":[{"The specific rotatory power of an optically active solution is determined and found to be" : str(S) + "deg/dm"}]}))

    def Newton_Rings(self):
        argument = self.arg[0:]
        r=0.0
        intermediate = []
        flag1 = 0
        for n in range(5, 41, 5):
            flag2=0
            flag1 += 1
            for m in range(7, 43, 5):
                flag2 += 1
                if(flag1 == flag2):
                    intermediate.append((round(float(argument[m])+(float(argument[m+1])*0.001)- float(argument[n])+(float(argument[n+1])*0.001)))**2)
        (intValue1, intValue2)=(intermediate[0: (len(intermediate)//2)], intermediate[(len(intermediate)//2):])
        
        for n in [0, 1, 2, 3]:
            r += (intValue1[n]-intValue2[n])
            
        r = r/5
        R = r/(4*float(argument[1])*float(argument[2]))
        print(json.dumps({"radius":[{"The radius of curvature of the surface of the given lens R" : str(R) + "m"}], "focal":[{"The focal length of the given lens f" : str(r) + " m"}]}))

    def lee(self):
        argument = self.arg[0:]
        argumentP = float(argument[3])
        argumentp1 = float(argument[5])
        OR = 0.0
        for n in range(21, 30, 2):
            OR += round(float(argument[n]) + (float(argument[n+1]) * argumentP),1)
            CR = (OR + (argumentp1 * argumentP))
        h = CR/5
        TR = 0.0
        for m in range(31, 40, 2):
            TR += round(float(argument[m]) + (float(argument[m+1]) * argumentP),1)
        D = TR/5

        r = D/2
        K  = ((int(argument[6])*int(argument[7])*int(argument[8]))/((math.pi*r**2)*(int(argument[1]))- int(argument[2]))*((r+(2*h))/((2*r)+(2*h))))
        # x1 = [2, 6, 10, 12, 16, 20]
        # y1 = [70, 69, 68, 67, 66, 65]
        # titletext="Lee's Disc method"
        # axisXtitle="Time sec"
        # axisYtitle= "Temperature ‘c"
        # resultJson={"x1":x1,"y1":y1,"titletext":titletext,"axisXtitle":axisXtitle,"axisYtitle":axisYtitle}

        # print(json.dumps({"ans":resultJson}))
        # print(json.dumps({"Lee":[{"Thickness of metalic disc" : str(h) + " m"}], "Vernier":[{"Thickness of the bad conductor" : str(D) + "m"}], "tickness":[{"Radius of the metalic disc" : str(r) + " m"}], "Thermal":[{"Thermal conductivity of a Poor Conductor" : str(K) + " ω/m/k"}]}))
        print(json.dumps({"Coil":[{"Coil carrying current" : str(argument[3]) }] }))
    def Coil(self):
        argument = self.arg[0:]
        M = 0.0
        for n in range(6, 83, 10):
            M += round(float(argument[n]) + (float(argument[n+1]) +(float(argument[n+2])+(float(argument[n+3])+(float(argument[n+4])+(float(argument[n+5])+(float(argument[n+6])+(float(argument[n+7])))))))),1)
            Mt = math.tan(M)
        tantita = Mt/8

        X = float(argument[5])-float(argument[15])
        
        H = (float(argument[1])*float(argument[2])**2*float(argument[3]) )/ ((2*(float(argument[2])**2+ X**2)**(0.5)) * (1/tantita)) 

        print(json.dumps({"Coil":[{"Coil carrying current" : str(H) }] }))

    def Thermal(self):
        argument = self.arg[0:]
        argumentP = float(argument[5])
        Lo = 0

        for n in range(6, 7):
            Lo += round(float(argument[n]) + (float(argument[n+1]) * argumentP),1)
        Li=0
        for m in range(8, 9):
            Li += round(float(argument[m]) + (float(argument[m+1]) * argumentP),1)
        ld = Lo + Li

        r1 = ld/2*10**-2
        Ro = 0
        for n in range(10, 11):
            Ro += round(float(argument[n]) + (float(argument[n+1]) * argumentP),1)
        Ri = 0
        for m in range(12, 13):
            Ri += round(float(argument[m]) + (float(argument[m+1]) * argumentP),1)
        rd = Ro + Ri
    
        r2 = (rd/2)*10**-2
    

        t = int(argument[22]) - int(argument[21])
        titas = (int(argument[18])*int(argument[19]))/2
        K  = ((int(argument[14])*int(argument[16]))+(int(argument[15])-int(argument[14])))*int(argument[17])*((int(argument[18])- int(argument[19])/(2*math.pi*int(argument[20])*t))*(((2.302*math.log10(r2/r1)/titas)-((int(argument[18])- int(argument[19]))/2))))
    
        print(json.dumps({"LD":[{"The LD of Thermal conductivity is determined and found to be" : str(ld) + "m", "Radius 2" : str(r2) + " cm","RD 1" : str(rd) + " m","Radius 1" : str(r1) + " cm","Thermal conductivity is" : str(K) + " cm"}]}))

    def Laser_grating(self):
        argument = self.arg[0:]
        TRLA = round(float(argument[2])+(float(argument[3])* float(argument[1])))
        TRLB = round(float(argument[4])+(float(argument[5])* float(argument[1])))
        TRRA = round(float(argument[6])+(float(argument[7])* float(argument[1])))
        TRRB = round(float(argument[8])+(float(argument[9])* float(argument[1])))
        Tita_2L_A = 2*TRLA
        Tita_2L_B = 2*TRLB
        Tita_2R_A = 2*TRRA
        Tita_2R_B = 2*TRRB
        Tita_L = (Tita_2L_A+Tita_2L_B)/4
        Tita_R = (Tita_2R_A+Tita_2R_B)/4

        Tita_M = (Tita_L + Tita_R)/2

        Ltan1 = float(argument[12]) /float(argument[10])
        Ltan1p = math.atan(-1)*(Ltan1)
        #print(f' Violet: {Ltan1p}')

        Ltan2 = float(argument[16]) /float(argument[14])
        Ltan2p = math.atan(-1)*(Ltan2)

        Ltan3 =  float(argument[20]) /float(argument[18])
        Ltan3p = math.atan(-1)*(Ltan3)

        Ltan4 = float(argument[24]) /float(argument[22])
        Ltan4p = math.atan(-1)*(Ltan4)

        Ltan5 = float(argument[28]) /float(argument[26])
        Ltan5p = math.atan(-1)*(Ltan5)

        Ltan6 = float(argument[32]) /float(argument[30])
        Ltan6p = math.atan(-1)*(Ltan6)
        
        Ltan7 = float(argument[36]) /float(argument[34])
        Ltan7p = math.atan(-1)*(Ltan7)

        Rtan1 = float(argument[13]) /float(argument[10])
        Rtan1p = math.atan(-1)*(Rtan1)

        Rtan2 = float(argument[17]) /float(argument[14])
        Rtan2p = math.atan(-1)*(Rtan2)

        Rtan3 = float(argument[21]) /float(argument[18])
        Rtan3p = math.atan(-1)*(Rtan3)

        Rtan4 = float(argument[25]) /float(argument[22])
        Rtan4p = math.atan(-1)*(Rtan4)

        Rtan5 = float(argument[29]) /float(argument[26])
        Rtan5p = math.atan(-1)*(Rtan5)

        Rtan6 = float(argument[33]) /float(argument[30])
        Rtan6p = math.atan(-1)*(Rtan6)
        
        Rtan7 = float(argument[37]) /float(argument[34])
        Rtan7p = math.atan(-1)*(Rtan7)

        tita1 = (Ltan1p+Rtan1p)/2
        tita2 = (Ltan2p+Rtan2p)/2
        tita3 = (Ltan3p+Rtan3p)/2
        tita4 = (Ltan4p+Rtan4p)/2
        tita5 = (Ltan5p+Rtan5p)/2
        tita6 = (Ltan6p+Rtan6p)/2
        tita7 = (Ltan7p+Rtan7p)/2
        
        lambda1  =  ((math.sin(tita1 ))/ (Tita_M*float(argument[10])))
        lambda2  =  ((math.sin(tita2 ))/ (Tita_M*float(argument[14])))
        lambda3  =  ((math.sin(tita3 ))/ (Tita_M*float(argument[18])))
        lambda4  =  ((math.sin(tita4 ))/ (Tita_M*float(argument[22])))
        lambda5  =  ((math.sin(tita5 ))/ (Tita_M*float(argument[26])))
        lambda6  =  ((math.sin(tita6 ))/ (Tita_M*float(argument[30])))
        lambda7  =  ((math.sin(tita7 ))/ (Tita_M*float(argument[34])))
        lamdas = (lambda1+lambda2+lambda3+lambda4+lambda5+lambda6+lambda7)/7

        print(json.dumps({"GratingL":[{"Number of lines in the left grating" : str(Tita_L) }], "GratingR":[{"Number of lines in the right grating" : str(Tita_R) + "m"}], "Wavelength":[{"Wavelength of the grating" : str(lamdas) + "u"}] }))

    def Spectometer_grating(self):
        argument = self.arg[0:]
        TRLA = float(argument[1])+(float(argument[2])* 0.001)
        TRLB = float(argument[3])+(float(argument[4])* 0.001)
        TRRA = float(argument[5])+(float(argument[6])* 0.001)
        TRRB = float(argument[7])+(float(argument[8])* 0.001)
        Tita_2L_A = 2*TRLA
        Tita_2L_B = 2*TRLB
        Tita_2R_A = 2*TRRA
        Tita_2R_B = 2*TRRB
        Tita_L = (Tita_2L_A+Tita_2L_B)/4
        Tita_R = (Tita_2R_A+Tita_2R_B)/4

        Ltan1 = float(argument[9]) /float(argument[10])
        Ltan1p = math.atan(-1)*(Ltan1)
        #print(f' Violet: {Ltan1p}')

        Ltan2 = float(argument[13]) /float(argument[14])
        Ltan2p = math.atan(-1)*(Ltan2)

        Ltan3 =  float(argument[17]) /float(argument[18])
        Ltan3p = math.atan(-1)*(Ltan3)

        Ltan4 = float(argument[21]) /float(argument[22])
        Ltan4p = math.atan(-1)*(Ltan4)

        Ltan5 = float(argument[25]) /float(argument[26])
        Ltan5p = math.atan(-1)*(Ltan5)

        Ltan6 = float(argument[29]) /float(argument[30])
        Ltan6p = math.atan(-1)*(Ltan6)
        
        Ltan7 = float(argument[33]) /float(argument[34])
        Ltan7p = math.atan(-1)*(Ltan7)

        Rtan1 = float(argument[11]) /float(argument[12])
        Rtan1p = math.atan(-1)*(Rtan1)

        Rtan2 = float(argument[15]) /float(argument[16])
        Rtan2p = math.atan(-1)*(Rtan2)

        Rtan3 = float(argument[19]) /float(argument[20])
        Rtan3p = math.atan(-1)*(Rtan3)

        Rtan4 = float(argument[23]) /float(argument[24])
        Rtan4p = math.atan(-1)*(Rtan4)

        Rtan5 = float(argument[27]) /float(argument[28])
        Rtan5p = math.atan(-1)*(Rtan5)

        Rtan6 = float(argument[31]) /float(argument[32])
        Rtan6p = math.atan(-1)*(Rtan6)
        
        Rtan7 = float(argument[35]) /float(argument[36])
        Rtan7p = math.atan(-1)*(Rtan7)

        tita1 = (Ltan1p+Rtan1p)/2
        tita2 = (Ltan2p+Rtan2p)/2
        tita3 = (Ltan3p+Rtan3p)/2
        tita4 = (Ltan4p+Rtan4p)/2
        tita5 = (Ltan5p+Rtan5p)/2
        tita6 = (Ltan6p+Rtan6p)/2
        tita7 = (Ltan7p+Rtan7p)/2
        tita = (tita1 + tita2 + tita3 + tita4 + tita5 + tita6 + tita7)/7

        m = (float(argument[10])+float(argument[11])+float(argument[12])+float(argument[13])+float(argument[14])+float(argument[15])+float(argument[16]))/7
        lambda1  =  ((math.sin(tita1 ))/ (float(argument[3])*float(argument[10])))
        lambda2  =  ((math.sin(tita2 ))/ (float(argument[3])*float(argument[11])))
        lambda3  =  ((math.sin(tita3 ))/ (float(argument[3])*float(argument[12])))
        lambda4  =  ((math.sin(tita4 ))/ (float(argument[3])*float(argument[13])))
        lambda5  =  ((math.sin(tita5 ))/ (float(argument[3])*float(argument[14])))
        lambda6  =  ((math.sin(tita6 ))/ (float(argument[3])*float(argument[15])))
        lambda7  =  ((math.sin(tita7 ))/ (float(argument[3])*float(argument[16])))
        lamdas = (lambda1+lambda2+lambda3+lambda4+lambda5+lambda6+lambda7)/7

        N = (math.sin(tita) / (m*lamdas))

        print(json.dumps({"Grating":[{"Number of lines in the left grating" : str(Tita_L) }], "Grating":[{"Number of lines in the right grating" : str(Tita_R) + "m"}], "Wavelength":[{"Wavelength of the mercury using grating" : str(N) + "u"}] }))

    def Spectrometer_prism(self):
        argument = self.arg[0:]
        X1 = float(argument[3])+(float(argument[4])* 0.001)
        X2 = float(argument[5])+(float(argument[6])* 0.001)
        Y1 = float(argument[7])+(float(argument[8])* 0.001)
        Y2 = float(argument[9])+(float(argument[10])* 0.001)
        
        R1 = (X1+Y1)/4
        R2 = (X2+Y2)/4

        A = (R1+R2)/2

        XV1 = float(argument[11]) +(float(argument[12])*0.001)
        XV2 = float(argument[13]) +(float(argument[14])*0.001)
        XV = (XV1+XV2)/2

        XB1 = float(argument[15]) +(float(argument[16])*0.001)
        XB2 = float(argument[17]) +(float(argument[18])*0.001)
        XB = (XB1+XB2)/2

        XBG1 = float(argument[19]) +(float(argument[20])*0.001)
        XBG2 = float(argument[21]) +(float(argument[22])*0.001)
        XBG = (XBG1+XBG2)/2

        XG1 = float(argument[23]) +(float(argument[24])*0.001)
        XG2 = float(argument[25]) +(float(argument[26])*0.001)
        XG = (XG1+XG2)/2

        XY1 = float(argument[27]) +(float(argument[28])*0.001)
        XY2 = float(argument[29]) +(float(argument[30])*0.001)
        XY = (XY1+XY2)/2

        XR1 = float(argument[31]) +(float(argument[32])*0.001)
        XR2 = float(argument[33]) +(float(argument[34])*0.001)
        XR = (XR1+XR2)/2

        XD1 = float(argument[35]) +(float(argument[36])*0.001)
        XD2 = float(argument[37]) +(float(argument[38])*0.001)
        XD = (XD1+XD2)/2


        RV =  float((math.sin(A+XV)/2)/(math.sin(A/2)))
        RB =  float((math.sin((A+XB)/2))/(math.sin(A/2)))
        RBG =  float((math.sin((A+XBG)/2))/(math.sin(A/2)))
        RG =  float((math.sin((A+XG)/2))/(math.sin(A/2)))
        RY =  float((math.sin((A+XY)/2))/(math.sin(A/2)))
        RR =  float((math.sin((A+XR)/2))/(math.sin(A/2)))
        RD =  float((math.sin((A+XD)/2))/(math.sin(A/2)))
        Mue = (RV+RY+RR+RBG+RB+RG+RD)/7
        
        index1 = float((RB-RV)/(Mue -1))
        index2 = float((RBG-RB)/(Mue -1))
        index3 = float((RG-RBG)/(Mue -1))
        index4 = float((RY-RG)/(Mue -1))
        index5 = float((RR-RY)/(Mue -1))
        index6 = float((RD-RR)/(Mue -1))
        index=(index1+index2+index3+index4+index5+index6)/6

        print(json.dumps({"Vernier":[{"Vernier scale reading for A" : str(A) }], "index":[{"Reflextion index" : str(Mue) + "m"}], "Wavelength":[{"Wavelength of the mercury spectrum using prism" : str(index) }] }))


