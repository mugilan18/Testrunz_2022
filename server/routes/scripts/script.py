#!/usr/bin/python
import sys, getopt, time
import json
from Dummy import Dummy
from FirstYearPhysics import FirstYPhysics
from physics_acet import PHY_acet
from FirstYearChemistry import FirstYChemistry
from Chemistry_acet import Chem_acet
from EnvironmentEngineeringLab import EVS
from MaterialTesting2 import MT2
from FluidMechanics import FML
# from BEE import BEE
from FirstYearCivil import FirstYCivil
from MaterialAndMetallorgy import MAM
from Dom import Dom
from ManufacturingProcess1 import MP1
from ManufacturingProcess2 import MP2
from CommunicationLab1 import CL1
from Network import NT
from CommunicationLab2 import Com2
from CommunicationLab3 import com3
from PowerElec import PowerElec
from ElectronicDeviceCircuit import EDC
from ElectronicCircuit1 import EC
from ElectronicCircuit2 import EC2
from ElectronicMachinary1 import EM1
from ElectronicMachinary2 import EM2
from ThermalEngineeringLab1 import TE1
from FirstYearGeotechnical import FirstYGtech
from Electronic2 import E2
from Electronic1 import EL1
from ElectricElectronic import EE
def main(argv,title):
    argument = ''
    usage = 'usage: script.py -f <sometext>'
    try:
        opts, args = getopt.getopt(argv,"hf:",["foo="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ("-f", "--foo"):
            argument = arg.split()
            try:
                if((argument[len(argument) -1] == "Vibrational_magnetometer_acet")):
                    PHY_acet(argument).VB_Mag()
                elif((argument[len(argument) -1] == "Prism_acet")):
                    PHY_acet(argument).prism()  
                elif((argument[len(argument) -1] == "Air_wedge_acet")):
                    PHY_acet(argument).Air_wed()
                elif((argument[len(argument) -1] == "Laser_acet")):
                    PHY_acet(argument).laser()
                elif((argument[len(argument) -1] == "Newton_ring_acet")):
                    PHY_acet(argument).newton()
                elif((argument[len(argument) -1] == "Radial_flow_acet")):
                    PHY_acet(argument).Radial()
                elif((argument[len(argument) -1] == "Grating_acet")):
                    PHY_acet(argument).grating()
                elif((argument[len(argument) -1] == "Deflection_mag_acet")):
                    PHY_acet(argument).Deflection()
                elif((argument[len(argument) -3] == "Lee's")and (argument[len(argument)-2]=="Disc")and (argument[len(argument) -1]=="Method_acet")):
                    PHY_acet(argument).lee()
                elif((argument[len(argument) -1] == "Polarimeter_acet")):
                    PHY_acet(argument).half()
                elif((argument[len(argument) -2] == "Acetic") and(argument[len(argument) -1] == "acid_acet") ):
                    Chem_acet(argument).Acetic_acid()
                elif((argument[len(argument) -2] == "Dissolved")and(argument[len(argument) -1] == "Oxygen_acet") ):
                    Chem_acet(argument).oxygen()
                elif((argument[len(argument) -2] == "EDTA")and(argument[len(argument) -1] == "Water_acet") ):
                    Chem_acet(argument).edta()
                elif((argument[len(argument) -1] == "Carbonates_acet")):
                    Chem_acet(argument).Carbonate()
                elif((argument[len(argument) -1] == "MOHR_acet")):
                    Chem_acet(argument).mohr()
                elif((argument[len(argument) -2] == "Bleaching")and (argument[len(argument)-1 ]== "powder_acet")):
                    Chem_acet(argument).Bleaching_powder()
                elif((argument[len(argument) -1] == "Copper_acet")):
                    Chem_acet(argument).copper()
                elif((argument[len(argument) -1] == "Conductometric_acet")):
                    Chem_acet(argument).Conductometry()
                elif((argument[len(argument) -2] == "EDTA")and(argument[len(argument)-1]=="Magnesium_acet")):
                    Chem_acet(argument).Magnesium()
                elif((argument[len(argument) -1] == "Calcium_acet")):
                    Chem_acet(argument).calcium()
                elif((argument[len(argument) -1] == "Permanganometry_acet")):
                    Chem_acet(argument).ferrous()
                elif((argument[len(argument) -2] == "Vibration") and (argument[len(argument) -1] == "Magnetometer")):
                    FirstYPhysics(argument).vibration_magnetometer()
                elif((argument[len(argument) -3] == "Air") and (argument[len(argument) -2] == "Wedge") and (argument[len(argument) -1] == "Experiment")):
                    FirstYPhysics(argument).Air_wedge()
                elif((argument[len(argument) -1] == "Polarimeter")):
                    FirstYPhysics(argument).Polarimeter()
                elif((argument[len(argument) -2] == "Newton") and (argument[len(argument) -1] == "Rings")):
                    FirstYPhysics(argument).Newton_Rings()
                elif((argument[len(argument) -3] == "Lee's") and (argument[len(argument) -2] == "Disc") and (argument[len(argument) -1] == "Method")):
                    FirstYPhysics(argument).lee()
                elif((argument[len(argument) -2] == "Magnetic") and (argument[len(argument) -1] == "Field")):
                    FirstYPhysics(argument).Coil()
                elif((argument[len(argument) -2] == "Thermal") and (argument[len(argument) -1] == "Conductivity")):
                    FirstYPhysics(argument).Thermal()
                elif((argument[len(argument) -2] == "Laser") and (argument[len(argument) -1] == "Grating")):
                    FirstYPhysics(argument).Laser_grating()
                elif((argument[len(argument) -2] == "Spectrometer") and (argument[len(argument) -1] == "Grating")):
                    FirstYPhysics(argument).Spectometer_grating()
                elif((argument[len(argument) -2] == "Spectrometer") and (argument[len(argument) -1] == "Prism")):
                    FirstYPhysics(argument).Spectrometer_prism()
                elif((argument[len(argument) -2] == "Dissolved") and (argument[len(argument) -1] == "Oxygen")):
                    FirstYChemistry(argument).oxygen()
                elif((argument[len(argument) -2] == "EDTA") and (argument[len(argument) -1] == "Water")):
                    FirstYChemistry(argument).EDTA_Water()
                elif((argument[len(argument) -2] == "EDTA") and (argument[len(argument) -1] == "Magnesium")):
                    FirstYChemistry(argument).EDTA_Magnesium()
                elif((argument[len(argument) -2] == "Acetic") and (argument[len(argument) -1] == "acid_acid")):
                    FirstYChemistry(argument).Acetic_acid()
                elif((argument[len(argument) -1] == "Copper")):
                    FirstYChemistry(argument).Copper()
                elif((argument[len(argument) -1] == "Conductometric")):
                    FirstYChemistry(argument).Conductometric()
                elif( (argument[len(argument) -2] == "Bleaching") and (argument[len(argument) -1] == "Powder")):
                    FirstYChemistry(argument).Bleaching_Powder()
                elif((argument[len(argument) -1] == "Permanganometry")):
                    FirstYChemistry(argument).Permanganometry()
                elif((argument[len(argument) -1] == "Colorimetry")):
                    FirstYChemistry(argument).Colorimetry()
                elif((argument[len(argument) -1] == "COD")):
                    FirstYChemistry(argument).COD()
                elif((argument[len(argument) -1] == "MOHR")):
                    FirstYChemistry(argument).MOHR()
                elif((argument[len(argument) -1] == "Alkalinity")):
                    FirstYChemistry(argument).Alkalinity()
                elif((argument[len(argument) -4] == "Determination") and  (argument[len(argument) -3] == "of") and  (argument[len(argument) -2] == "total") and  (argument[len(argument) -1] == "solids")):
                    EVS(argument).total_solids()
                elif((argument[len(argument) -3] == "Determination") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "alkalinity")):
                    EVS(argument).alkalinity()
                elif((argument[len(argument) -3] == "Determination") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "chloride")):
                    EVS(argument).chloride()
                elif((argument[len(argument) -3] == "Determination") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "TH")):
                    EVS(argument).total_hardness()
                elif((argument[len(argument) -3] == "Determination") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "RC")):
                    EVS(argument).chlorine()
                elif((argument[len(argument) -3] == "Determination") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "DO")):
                    EVS(argument).dissolved_oxygen()
                elif((argument[len(argument) -4] == "Specific") and  (argument[len(argument) -3] == "gravity") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "cement")):
                    MT2(argument).Gravity()
                elif((argument[len(argument) -4] == "Specific") and  (argument[len(argument) -3] == "gravity") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "fine")):
                    MT2(argument).Fine_aggregate()
                elif((argument[len(argument) -4] == "Specific") and  (argument[len(argument) -3] == "gravity") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "coarse")):
                    MT2(argument).coarse_aggregate()
                elif((argument[len(argument) -4] == "Size") and  (argument[len(argument) -3] == "distribution") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "coarse")):
                    MT2(argument).Size_aggregate()
                elif((argument[len(argument) -4] == "Size") and  (argument[len(argument) -3] == "distribution") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "fine")):
                    MT2(argument).particle_aggregate()
                elif((argument[len(argument) -4] == "Consistency") and  (argument[len(argument) -3] == "of") and  (argument[len(argument) -2] == "standard") and  (argument[len(argument) -1] == "cement")):
                    MT2(argument).Consistency()
                elif((argument[len(argument) -4] == "Setting") and  (argument[len(argument) -3] == "time") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "cement")):
                    MT2(argument).Setting_time()
                elif((argument[len(argument) -4] == "Bulking") and  (argument[len(argument) -3] == "of") and  (argument[len(argument) -2] == "fine") and  (argument[len(argument) -1] == "aggregate")):
                    MT2(argument).Bulk()
                elif((argument[len(argument) -3] == "VEE") and  (argument[len(argument) -2] == "BEE") and  (argument[len(argument) -1] == "Consistometer")):
                    MT2(argument).Vee_Bee()
                elif((argument[len(argument) -3] == "Compaction") and  (argument[len(argument) -2] == "factor") and  (argument[len(argument) -1] == "test")):
                    MT2(argument).compaction()
                elif((argument[len(argument) -3] == "Slump") and  (argument[len(argument) -2] == "cone") and  (argument[len(argument) -1] == "test")):
                    MT2(argument).Slump()
                elif((argument[len(argument) -4] == "Compressive") and  (argument[len(argument) -3] == "strength") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "cement")):
                    MT2(argument).compression()
                elif((argument[len(argument) -4] == "Flexural") and  (argument[len(argument) -3] == "strength") and  (argument[len(argument) -2] == "of") and  (argument[len(argument) -1] == "concrete")):
                    MT2(argument).Flexural()
                elif((argument[len(argument) -3] == "Flow") and  (argument[len(argument) -2] == "Through") and  (argument[len(argument) -1] == "Pipes")):
                    FML(argument).Through_Pipe()
                elif((argument[len(argument) -3] == "Pelton") and  (argument[len(argument) -2] == "Wheel") and  (argument[len(argument) -1] == "Turbine")):
                    FML(argument).pelton()
                elif((argument[len(argument) -3] == "Flow") and  (argument[len(argument) -2] == "Through") and  (argument[len(argument) -1] == "Venturimeter")):
                    FML(argument).Venturimeter()
                elif((argument[len(argument) -3] == "Jet") and (argument[len(argument) -2] == "On") and (argument[len(argument) -1] == "Plate")):
                    FML(argument).Jet()
                elif((argument[len(argument) -2] == "Centrifugal") and  (argument[len(argument) -1] == "Pump")):
                    FML(argument).Centrifugal()
                elif((argument[len(argument) -2] == "Performance") and  (argument[len(argument) -1] == "RP")):
                    FML(argument).Reciprocating()
                elif((argument[len(argument) -1] == "Test_on_RP")):
                    FML(argument).Test_Reciprocating()
                elif((argument[len(argument) -2] == "Submersible") and  (argument[len(argument) -1] == "Pump")):
                    FML(argument).Submersible()
                elif((argument[len(argument) -4] == "Determination") and  (argument[len(argument) -3] == "of") and  (argument[len(argument) -2] == "Minor") and  (argument[len(argument) -1] == "Losses")):
                    FML(argument).Minor_Loss()
                elif((argument[len(argument) -3] == "Flow") and  (argument[len(argument) -2] == "Through") and  (argument[len(argument) -1] == "Orifice")):
                    FML(argument).Orifice()
                elif((argument[len(argument) -3] == "Cathode") and  (argument[len(argument) -2] == "Ray") and  (argument[len(argument) -1] == "Oscilloscope")):
                    BEE(argument).CRO()
                elif((argument[len(argument) -3] == "Impact") and (argument[len(argument) -2] == "test") and (argument[len(argument) -1] == "Charpy")):
                    MAM(argument).Impact_test_charpy()
                elif((argument[len(argument) -3] == "Brinell") and (argument[len(argument) -2] == "Hardness") and (argument[len(argument) -1] == "Test")):
                    MAM(argument).Brinell()
                elif((argument[len(argument) -3] == "Impact") and (argument[len(argument) -2] == "test") and (argument[len(argument) -1] == "Izod")):
                    MAM(argument).Impact_test_diode()
                elif((argument[len(argument) -2] == "Torsion") and (argument[len(argument) -1] == "test")):
                    MAM(argument).Torsion()
                elif((argument[len(argument) -4] == "Erichsen") and (argument[len(argument) -3] == "Sheet") and (argument[len(argument) -2] == "Metal") and (argument[len(argument) -1] == "Test")):
                    MAM(argument).Erichsen_sheet_metal_test()
                elif((argument[len(argument) -2] == "Hardness") and (argument[len(argument) -1] == "test")):
                    MAM(argument).Hardness_test()
                elif((argument[len(argument) -2] == "Rockwell") and (argument[len(argument) -1] == "hardness")):
                    MAM(argument).Rock_well_hardness()
                elif((argument[len(argument) -2] == "Bend") and (argument[len(argument) -1] == "Test")):
                    MAM(argument).Bend()
                elif((argument[len(argument) -2] == "Tension") and (argument[len(argument) -1] == "test")):
                    MAM(argument).Tension_test()
                elif((argument[len(argument) -3] == "Annealing") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "Steel")):
                    MAM(argument).Annealing()
                elif((argument[len(argument) -3] == "Normalizing") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "Steel")):
                    MAM(argument).Normalizing()
                elif((argument[len(argument) -3] == "Heat") and (argument[len(argument) -2] == "Treatment") and (argument[len(argument) -1] == "Processes")):
                    MAM(argument).Heat()
                elif((argument[len(argument) -3] == "Hardening") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "Steel")):
                    MAM(argument).Hardening()
                elif((argument[len(argument) -3] == "Microstructure") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "Material")):
                    MAM(argument).Microstructure()
                elif((argument[len(argument) -2] == "Metallurgical") and (argument[len(argument) -1] == "Microscope")):
                    MAM(argument).Metallurgical()
                elif((argument[len(argument) -2] == "Microscopic") and (argument[len(argument) -1] == "Examination")):
                    MAM(argument).Microscopic()
                elif((argument[len(argument) -3] == "Study") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "Etchants")):
                    MAM(argument).Etchants()
                elif((argument[len(argument) -3] == "Measurement") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "Hardenability")):
                    MAM(argument).Hardenability()
                elif((argument[len(argument) -3] == "Helical") and (argument[len(argument) -2] == "Spring") and (argument[len(argument) -1] == "System")):
                    Dom(argument).Single_Helical()
                elif((argument[len(argument) -4] == "Torsional") and (argument[len(argument) -3] == "Single") and (argument[len(argument) -2] == "Rotor") and (argument[len(argument) -1] == "System")):
                    Dom(argument).Torsional()
                elif((argument[len(argument) -3] == "Two") and (argument[len(argument) -2] == "Rotor") and (argument[len(argument) -1] == "System")):
                    Dom(argument).Two_Rotor()
                elif((argument[len(argument) -3] == "Radius") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "Gyration")):
                    Dom(argument).Radius()
                elif((argument[len(argument) -2] == "Bifilar") and (argument[len(argument) -1] == "Suspension")):
                    Dom(argument).Bifilar()
                elif((argument[len(argument) -3] == "Damping") and (argument[len(argument) -2] == "Co") and (argument[len(argument) -1] == "Efficient")):
                    Dom(argument).Damping()
                elif((argument[len(argument) -4] == "Equivalent") and (argument[len(argument) -3] == "Spring") and (argument[len(argument) -2] == "Mass") and (argument[len(argument) -1] == "System")):
                    Dom(argument).Equivalent()
                elif((argument[len(argument) -2] == "Watt") and (argument[len(argument) -1] == "Governor")):
                    Dom(argument).Watt()
                elif((argument[len(argument) -2] == "Porter") and (argument[len(argument) -1] == "Governor")):
                    Dom(argument).Porter()
                elif((argument[len(argument) -2] == "Proell") and (argument[len(argument) -1] == "Governors")):
                    Dom(argument).Proell()
                elif((argument[len(argument) -2] == "Hartnell") and (argument[len(argument) -1] == "Governors")):
                    Dom(argument).Hartnell()
                elif((argument[len(argument) -4] == "Static") and (argument[len(argument) -3] == "And") and (argument[len(argument) -2] == "Dynamics") and (argument[len(argument) -1] == "Balancing")):
                    Dom(argument).Static()
                elif((argument[len(argument) -3] == "Whirling") and (argument[len(argument) -2] == "Of") and (argument[len(argument) -1] == "Shaft")):
                    Dom(argument).Whirling()
                elif((argument[len(argument) -3] == "Gyroscopic") and (argument[len(argument) -2] == "Couple") and (argument[len(argument) -1] == "Verification")):
                    Dom(argument).Gyroscopic()
                elif((argument[len(argument) -3] == "Journal") and (argument[len(argument) -2] == "Bearing") and (argument[len(argument) -1] == "Pressure")):
                    Dom(argument).Journal()
                elif((argument[len(argument) -2] == "Cam") and (argument[len(argument) -1] == "Analysis")):
                    Dom(argument).Cam()
                elif((argument[len(argument) -2] == "Lathe") and (argument[len(argument) -1] == "Machine")):
                    MP1(argument).Lathe()
                elif((argument[len(argument) -2] == "V") and (argument[len(argument) -1] == "Shaping")):
                    MP1(argument).V_Shaping()
                elif((argument[len(argument) -2] == "Cube") and (argument[len(argument) -1] == "Milling")):
                    MP1(argument).Cube()
                elif((argument[len(argument) -2] == "Cube") and (argument[len(argument) -1] == "Shaping")):
                    MP1(argument).Cube_Shaping()
                elif((argument[len(argument) -4] == "Facing") and (argument[len(argument) -3] == "and") and (argument[len(argument) -2] == "Plain") and (argument[len(argument) -1] == "Turning")):
                    MP1(argument).Facing()
                elif((argument[len(argument) -2] == "Step") and (argument[len(argument) -1] == "Milling")):
                    MP1(argument).Step()
                elif((argument[len(argument) -2] == "Step") and (argument[len(argument) -1] == "Turning")):
                    MP1(argument).Turning()
                elif((argument[len(argument) -4] == "Taper") and (argument[len(argument) -3] == "Turning") and (argument[len(argument) -2] == "Using") and (argument[len(argument) -1] == "Compound")):
                    MP1(argument).Compound()
                elif((argument[len(argument) -3] == "Drilling") and (argument[len(argument) -2] == "and") and (argument[len(argument) -1] == "boring")):
                    MP2(argument).Drilling()
                elif((argument[len(argument) -3] == "Turning") and (argument[len(argument) -2] == "between") and (argument[len(argument) -1] == "centers")):
                    MP2(argument).Turning()
                elif((argument[len(argument) -3] == "Start") and (argument[len(argument) -2] == "thread") and (argument[len(argument) -1] == "cut")):
                    MP2(argument).Multi()
                elif((argument[len(argument) -2] == "Eccentric") and (argument[len(argument) -1] == "turning")):
                    MP2(argument).Eccentric()
                elif((argument[len(argument) -4] == "Study") and (argument[len(argument) -3] == "of") and (argument[len(argument) -2] == "drilling") and (argument[len(argument) -1] == "machine")):
                    MP2(argument).Study()
                elif((argument[len(argument) -3] == "Drilling") and (argument[len(argument) -2] == "and") and (argument[len(argument) -1] == "tapping")):
                    MP2(argument).Drilling()
                elif((argument[len(argument) -2] == "V-SLOT") and (argument[len(argument) -1] == "GROOVING")):
                    MP2(argument).Shaping()
                elif((argument[len(argument) -2] == "Spline") and (argument[len(argument) -1] == "milling")):
                    MP2(argument).Spline()
                elif((argument[len(argument) -2] == "Keyway") and (argument[len(argument) -1] == "milling")):
                    MP2(argument).Keyway()
                elif((argument[len(argument) -4] == "Study") and (argument[len(argument) -3] == "of") and (argument[len(argument) -2] == "grinding") and (argument[len(argument) -1] == "machine")):
                    MP2(argument).grinding()
                elif((argument[len(argument) -2] == "Cylindrical") and (argument[len(argument) -1] == "grinding")):
                    MP2(argument).Cylindrical()
                elif((argument[len(argument) -3] == "Tuned") and (argument[len(argument) -2] == "And") and (argument[len(argument) -1] == "Wideband")):
                    CL1(argument).Tuned()
                elif((argument[len(argument) -2] == "Frequency") and (argument[len(argument) -1] == "Modulation")):
                    CL1(argument).Frequency()
                elif((argument[len(argument) -3] == "Amplitude") and (argument[len(argument) -2] == "and") and (argument[len(argument) -1] =="Demodulator")):
                    CL1(argument).Amplitude()
                elif((argument[len(argument) -3] == "Pre") and (argument[len(argument) -2] == "and") and (argument[len(argument) -1] == "De-emphasis")):
                    CL1(argument).emphasis()
                elif((argument[len(argument) -3] == "Sample") and (argument[len(argument) -2] == "Hold") and (argument[len(argument) -1] == "PAM")):
                    CL1(argument).Sample()
                elif((argument[len(argument) -3] == "Simple") and (argument[len(argument) -2] == "Automatic") and (argument[len(argument) -1] == "Gain")):
                    CL1(argument).Automatic()
                elif((argument[len(argument) -3] == "Delayed") and (argument[len(argument) -2] == "Automatic") and (argument[len(argument) -1] == "Gain")):
                    CL1(argument).Delayed()
                elif((argument[len(argument) -4] == "Pulse") and (argument[len(argument) -3] == "width") and (argument[len(argument) -2] == "and") and (argument[len(argument) -1] == "Position")):
                    CL1(argument).Pulse()
                elif((argument[len(argument) -3] == "Mixer") and (argument[len(argument) -2] == "and") and (argument[len(argument) -1] == "Ring")):
                    CL1(argument).Mixer()
                elif((argument[len(argument) -3] == "K-type") and (argument[len(argument) -2] == "Low") and (argument[len(argument) -1] == "Pass")):
                    NT(argument).K_type()
                elif((argument[len(argument) -3] == "k-type") and (argument[len(argument) -2] == "Band") and (argument[len(argument) -1] == "Pass")):
                    NT(argument).Band()
                elif((argument[len(argument) -3] == "Design") and (argument[len(argument) -2] == "Of") and (argument[len(argument) -1] == "M-Derived")):
                    NT(argument).Design()
                elif((argument[len(argument) -3] == "Switched") and (argument[len(argument) -2] == "Twin") and (argument[len(argument) -1] == "T-Network")):
                    NT(argument).Switched()
                elif((argument[len(argument) -3] == "LC") and (argument[len(argument) -2] == "Resonant") and (argument[len(argument) -1] == "Circuit")):
                    NT(argument).LC()
                elif((argument[len(argument) -3] == "Open") and (argument[len(argument) -2] == "Circuit") and (argument[len(argument) -1] == "Independence")):
                    NT(argument).Open()
                elif((argument[len(argument) -3] == "Characteristic") and (argument[len(argument) -2] == "Of") and (argument[len(argument) -1] == "Equalizer")):
                    NT(argument).Equalizer()
                elif((argument[len(argument) -3] == "Characteristics") and (argument[len(argument) -2] == "Of") and (argument[len(argument) -1] == "Attenuator")):
                    NT(argument).Attenuator()
                elif((argument[len(argument) -4] == "Junction") and (argument[len(argument) -3] == "Field") and (argument[len(argument) -2] == "Effect") and (argument[len(argument) -1] == "Transistor")):
                    EDC(argument).Junction()
                elif((argument[len(argument) -2] == "Semiconductor") and (argument[len(argument) -1] == "diode")):
                    EDC(argument).Semiconductor()
                elif((argument[len(argument) -4] == "BJT") and (argument[len(argument) -3] == "in") and (argument[len(argument) -2] == "CB") and (argument[len(argument) -1] == "Configuration")):
                    EDC(argument).BJT()
                elif((argument[len(argument) -2] == "Bridge") and (argument[len(argument) -1] == "Rectifier")):
                    EDC(argument).Bridge()
                elif((argument[len(argument) -4] == "BJT") and (argument[len(argument) -3] == "in") and (argument[len(argument) -2] == "CE") and (argument[len(argument) -1] == "configuration")):
                    EDC(argument).CE()
                elif((argument[len(argument) -4] == "Clipper") and (argument[len(argument) -3] == "Circuit") and (argument[len(argument) -2] == "Using") and (argument[len(argument) -1] == "Diode")):
                    EDC(argument).Clipper()
                elif((argument[len(argument) -2] == "Biasing") and (argument[len(argument) -1] == "Circuits")):
                    EDC(argument).Biasing()
                elif((argument[len(argument) -3] == "Characteristics") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "UJT")):
                    EDC(argument).UJT()
                elif((argument[len(argument) -3] == "Characteristics") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "MOSFET")):
                    EDC(argument).MOSFET()
                elif((argument[len(argument) -1] == "SCR") ):
                    EDC(argument).SCR()
                elif((argument[len(argument) -2] == "Photo") and (argument[len(argument) -1] == "transistor")):
                    EDC(argument).Biasing()
                elif((argument[len(argument) -3] == "CHARACTERISTICS") and (argument[len(argument) -2] == "OF") and (argument[len(argument) -1] == "TRIAC")):
                    EDC(argument).TRIAC()
                elif((argument[len(argument) -3] == "Characteristics") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "LED")):
                    EDC(argument).LED()
                elif((argument[len(argument) -1] == "CEA")):
                    EC(argument).CEA()
                elif((argument[len(argument) -2] == "Emitter") and (argument[len(argument) -1] == "follower")):
                    EC(argument).Emitter()
                elif((argument[len(argument) -2] == "Cascade") and (argument[len(argument) -1] == "Amplifier")):
                    EC(argument).Cascade()
                elif((argument[len(argument) -2] == "Cascode") and (argument[len(argument) -1] == "Amplifier")):
                    EC(argument).Cascode()
                elif((argument[len(argument) -2] == "FET") and (argument[len(argument) -1] == "amplifier")):
                    EC(argument).FET()
                elif((argument[len(argument) -2] == "DARLINGTON") and (argument[len(argument) -1] == "AMPLIFIER")):
                    EC(argument).DARLINGTON()
                elif((argument[len(argument) -2] == "RC") and (argument[len(argument) -1] == "OSCILLATORS")):
                    EC(argument).RC()
                elif((argument[len(argument) -2] == "LC") and (argument[len(argument) -1] == "OSCILLATORS")):
                    EC(argument).LC()
                elif((argument[len(argument) -1] == "CLAMPERS")):
                    EC(argument).CLAMPERS()
                elif((argument[len(argument) -2] == "DIFFERENTIAL") and (argument[len(argument) -1] == "AMPLIFIER")):
                    EC(argument).DIFFERENTIAL()
                elif((argument[len(argument) -3] == "NEGATIVE") and (argument[len(argument) -2] == "FEEDBACK") and (argument[len(argument) -1] == "AMPLIFIER")):
                    EC(argument).NEGATIVE()
                elif((argument[len(argument) -2] == "ASTABLE") and (argument[len(argument) -1] == "MULTIVIBRATOR")):
                    EC(argument).ASTABLE()
                elif((argument[len(argument) -2] == "SCHMITT") and (argument[len(argument) -1] == "TRIGGER")):
                    EC(argument).SCHMITT()
                elif((argument[len(argument) -2] == "RC") and (argument[len(argument) -1] == "INTEGRATOR")):
                    EC(argument).INTEGRATOR()
                elif((argument[len(argument) -2] == "RC") and (argument[len(argument) -1] == "INTEGRATOR")):
                    EC(argument).INTEGRATOR()
                elif((argument[len(argument) -3] == "VOLTAGE") and (argument[len(argument) -2] == "SERIES") and (argument[len(argument) -1] == "FEEDBACK")):
                    EC2(argument).VOLTAGE()
                elif((argument[len(argument) -3] == "VOLTAGE") and (argument[len(argument) -2] == "SHUNT") and (argument[len(argument) -1] == "FEEDBACK")):
                    EC2(argument).SHUNT()
                elif((argument[len(argument) -3] == "RC") and (argument[len(argument) -2] == "PHASE") and (argument[len(argument) -1] == "SHIFT")):
                    EC2(argument).PHASE()
                elif((argument[len(argument) -3] == "HARTLEY") and (argument[len(argument) -2] == "&") and (argument[len(argument) -1] == "COLPITTS")):
                    EC2(argument).HARTLEY()
                elif((argument[len(argument) -3] == "ASTABLE") and (argument[len(argument) -2] == "&") and (argument[len(argument) -1] == "MONOSTABLE")):
                    EC2(argument).ASTABLE()
                elif((argument[len(argument) -2] == "BISTABLE") and (argument[len(argument) -1] == "MULTIVIBRATOR")):
                    EC2(argument).BISTABLE()
                elif((argument[len(argument) -2] == "CLASS") and (argument[len(argument) -1] == "A")):
                    EC2(argument).CLASS_A()
                elif((argument[len(argument) -2] == "CLASS") and (argument[len(argument) -1] == "B")):
                    EC2(argument).CLASS_B()
                elif((argument[len(argument) -3] == "ASTABLE") and (argument[len(argument) -2] == "AND") and (argument[len(argument) -1] == "MONOSTABLE")):
                    EC2(argument).ASTABLE()
                elif((argument[len(argument) -3] == "TIME") and (argument[len(argument) -2] == "BASE") and (argument[len(argument) -1] == "GENERATORS")):
                    EC2(argument).TIME()
                elif((argument[len(argument) -3] == "D.C") and (argument[len(argument) -2] == "SHUNT") and (argument[len(argument) -1] == "MOTOR")):
                    EM1(argument).DC_SHUNT_MOTOR()
                elif((argument[len(argument) -3] == "DC") and (argument[len(argument) -2] == "SERIES") and (argument[len(argument) -1] == "MOTOR")):
                    EM1(argument).DC_SERIES_MOTOR()
                elif((argument[len(argument) -3] == "DC") and (argument[len(argument) -2] == "COMPOUND") and (argument[len(argument) -1] == "MOTOR")):
                    EM1(argument).DC_COMPOUND_MOTOR()
                elif((argument[len(argument) -3] == "SELF") and (argument[len(argument) -2] == "EXCITED") and (argument[len(argument) -1] == "DC")):
                    EM1(argument).SELF()
                elif((argument[len(argument) -3] == "SEPARATELY") and (argument[len(argument) -2] == "EXCITED") and (argument[len(argument) -1] == "DC")):
                    EM1(argument).SEPARATELY()
                elif((argument[len(argument) -3] == "Load") and (argument[len(argument) -2] == "separately") and (argument[len(argument) -1] == "DC")):
                    EM1(argument).Load_Separately()
                elif((argument[len(argument) -3] == "Load") and (argument[len(argument) -2] == "self") and (argument[len(argument) -1] == "DC")):
                    EM1(argument).Load_Self()
                elif((argument[len(argument) -2] == "SWINBURNE’S") and (argument[len(argument) -1] == "TEST")):
                    EM1(argument).SWINBURNE()
                elif((argument[len(argument) -1] == "Hopkin")):
                    EM1(argument).Hopkin()
                elif((argument[len(argument) -2] == "Speed") and (argument[len(argument) -1] == "control")):
                    EM1(argument).Speed()
                elif((argument[len(argument) -2] == "OC_DC") and (argument[len(argument) -1] == "shunt")):
                    EM1(argument).OCDC()
                elif((argument[len(argument) -3] == "OC") and (argument[len(argument) -2] == "and") and (argument[len(argument) -1] == "SC")):
                    EM1(argument).OC()
                elif((argument[len(argument) -1] == "Single_Phase_Transformer")):
                    EM1(argument).trf()
                elif((argument[len(argument) -2] == "REDWOOD") and (argument[len(argument) -1] == "VISCOMETER")):
                    TE1(argument).REDWOOD()
                elif((argument[len(argument) -3] == "CLEVELAND") and (argument[len(argument) -2] == "OPEN") and (argument[len(argument) -1] == "CUP")):
                    TE1(argument).CLEVELAND()
                elif((argument[len(argument) -3] == "RECIPROCATING") and (argument[len(argument) -2] == "AIR") and (argument[len(argument) -1] == "COMPRESSOR")):
                    TE1(argument).COMPRESSOR()
                elif((argument[len(argument) -2] == "NATURAL") and (argument[len(argument) -1] == "CONVECTION")):
                    TE1(argument).NATURAL()
                elif((argument[len(argument) -3] == "Junkers") and (argument[len(argument) -2] == "gas") and (argument[len(argument) -1] == "calorimeter")):
                    TE1(argument).Junkers()
                elif((argument[len(argument) -2] == "Forced") and (argument[len(argument) -1] == "convection")):
                    TE1(argument).Forced()
                elif((argument[len(argument) -2] == "BOMB") and (argument[len(argument) -1] == "CALORIMETER")):
                    TE1(argument).BOMB()
                elif((argument[len(argument) -2] == "PIN") and (argument[len(argument) -1] == "FIN")):
                    TE1(argument).Pin_Fin()
                elif((argument[len(argument) -3] == "TIME") and (argument[len(argument) -2] == "DIVISION") and (argument[len(argument) -1] == "MULTIPLEXING")):
                    Com2(argument).TIME_DIVISION_MULTIPLEXING()
                elif((argument[len(argument) -5] == "M-ary") and (argument[len(argument) -4] == "ASK,") and (argument[len(argument) -3] == "FSK,") and (argument[len(argument) -2] == "and") and (argument[len(argument) -1] == "PSK")):                    
                    Com2(argument).Mary_ASK_FSK_and_PSK()     
                elif((argument[len(argument) -4] == "BASK,") and (argument[len(argument) -3] == "BFSK") and (argument[len(argument) -2] == "and") and (argument[len(argument) -1] == "BPSK")):
                    Com2(argument).BASK_BFSK_and_BPSK()
                elif((argument[len(argument) -2] == "RSA") and (argument[len(argument) -1] == "ALGORITHM")):
                    Com2(argument).RSA_ALGORITHM()
                elif((argument[len(argument) -3] == "PULSE") and (argument[len(argument) -2] == "CODE_") and (argument[len(argument) -1] == "MODULATION")):
                    Com2(argument).PULSE_CODE_MODULATION()
                elif((argument[len(argument) -1] == "LCT")):
                    Com2(argument).LCT()
                elif((argument[len(argument) -1] == "DM")):
                    Com2(argument).DM()
                elif((argument[len(argument) -2] == "FREQUENCY") and (argument[len(argument) -1] == "SYNTHESIZER")):
                    Com2(argument).FREQUENCY_SYNTHESIZER()
                elif((argument[len(argument) -1] == "ASK")):
                    Com2(argument).ASK()
                elif((argument[len(argument) -1] == "BPSK")):
                    Com2(argument).BPSK()
                elif((argument[len(argument) -1] == "FSK")):
                    Com2(argument).FSK()
                elif((argument[len(argument) -3] == "Gate") and (argument[len(argument) -2] == "Pulse") and (argument[len(argument) -1] == "Generation")):
                    PowerElec(argument).Gate_Pulse_Generation()
                elif((argument[len(argument) -3] == "CHARACTERISTICS") and (argument[len(argument) -2] == "OF") and (argument[len(argument) -1] == "SCR")):
                    PowerElec(argument).CHARACTERISTICS_OF_SCR()
                elif((argument[len(argument) -3] == "CHARACTERISTICS") and (argument[len(argument) -2] == "OF") and (argument[len(argument) -1] == "TRIAC")):
                    PowerElec(argument).CHARACTERISTICS_OF_TRIAC()
                elif((argument[len(argument) -3] == "MOSFET") and (argument[len(argument) -2] == "&") and (argument[len(argument) -1] == "IGBT")):                 
                    PowerElec(argument).MOSFET_IGBT()
                elif((argument[len(argument) -2] == "HALF") and (argument[len(argument) -1] == "CONTROLLED")):                  
                    PowerElec(argument).HALF_CONTROLLED()
                elif((argument[len(argument) -2] == "FULLY") and (argument[len(argument) -1] == "CONTROLLED")):                  
                    PowerElec(argument).FULLY_CONTROLLED()
                elif((argument[len(argument) -3] == "MOSFET") and (argument[len(argument) -2] == "BASED") and (argument[len(argument) -1] == "CHOPPERS")):
                    PowerElec(argument).MOSFET_BASED_CHOPPERS()
                elif((argument[len(argument) -4] == "SINGLE") and (argument[len(argument) -3] == "PHASE") and (argument[len(argument) -2] == "PWM") and (argument[len(argument) -1] == "INVERTER")):
                    PowerElec(argument).SINGLE_PHASE_PWM_INVERTER()
                elif((argument[len(argument) -4] == "THREE") and (argument[len(argument) -3] == "PHASE") and (argument[len(argument) -2] == "PWM") and (argument[len(argument) -1] == "INVERTER")):
                    PowerElec(argument).THREE_PHASE_PWM_INVERTER()
                elif((argument[len(argument) -3] == "AC") and (argument[len(argument) -2] == "VOLTAGE") and (argument[len(argument) -1] == "CONTROLLER")):
                    PowerElec(argument).AC_VOLTAGE_CONTROLLER()
                elif((argument[len(argument) -4] == "SWITCHED") and (argument[len(argument) -3] == "MODE") and (argument[len(argument) -2] == "POWER") and (argument[len(argument) -1] == "INVERTER")):
                    PowerElec(argument).SWITCHED_MODE_POWER_CONVERTER()
                elif((argument[len(argument) -2] == "Specific") and (argument[len(argument) -1] == "Gravity")):                  
                    FirstYGtech(argument).Specific_Gravity()
                elif((argument[len(argument) -2] == "Grain") and (argument[len(argument) -1] == "size")):                  
                    FirstYGtech(argument).Grain_size_analysis()
                elif((argument[len(argument) -2] == "Standard") and (argument[len(argument) -1] == "proctor")):                  
                    FirstYGtech(argument).Standard_proctor()
                elif((argument[len(argument) -3] == "Free") and (argument[len(argument) -2] == "swell") and (argument[len(argument) -1] == "Index")):
                    FirstYGtech(argument).Determination_of_free_swell_index()
                elif((argument[len(argument) -2] == "Shrinkage") and (argument[len(argument) -1] == "limit")):                  
                    FirstYGtech(argument).Determination_of_shrinkage_limit()
                elif((argument[len(argument) -3] == "Permeability") and (argument[len(argument) -2] == "or") and (argument[len(argument) -1] == "Hydraulic")):
                    FirstYGtech(argument).Permiability_of_hydraaulic_conductivity()
                elif((argument[len(argument) -3] == "Unconfined") and (argument[len(argument) -2] == "compression") and (argument[len(argument) -1] == "test")):
                    FirstYGtech(argument).UCT()
                elif((argument[len(argument) -3] == "DIRECT") and (argument[len(argument) -2] == "SHEAR") and (argument[len(argument) -1] == "TEST")):
                    FirstYGtech(argument).Direct_shear_test()
                elif((argument[len(argument) -3] == "Triaxial") and (argument[len(argument) -2] == "shear") and (argument[len(argument) -1] == "Test")):
                    FirstYGtech(argument).Triaxial_Shear_test()
                elif((argument[len(argument) -2] == "GUNN") and (argument[len(argument) -1] == "DIODE")):                  
                    com3(argument).GUNN_DIODE()
                elif((argument[len(argument) -2] == "REFLEX") and (argument[len(argument) -1] == "KLYSTRON")):                  
                    com3(argument).REFLEX_KLYSTRON()
                elif((argument[len(argument) -3] == "ISOLATOR") and (argument[len(argument) -2] == "&") and (argument[len(argument) -1] == "CIRCULATOR")):
                    com3(argument).ISOLATOR_CIRCULATOR()
                elif((argument[len(argument) -4] == "E") and (argument[len(argument) -3] == "and") and (argument[len(argument) -2] == "HI") and (argument[len(argument) -1] == "plane")):
                    com3(argument).EPLANE_AND_HIPLANE_TEE()                  
                elif((argument[len(argument) -2] == "MAGIC") and (argument[len(argument) -1] == "TEE")):                  
                    com3(argument).MAGIC_TEE()
                elif((argument[len(argument) -2] == "DIRECTIONAL") and (argument[len(argument) -1] == "COUPLER")):                  
                    com3(argument).DIRECTIONAL_COUPLER()
                elif((argument[len(argument) -2] == "HORN") and (argument[len(argument) -1] == "ANTENNA")):                  
                    com3(argument).HORN_ANTENNA()
                elif((argument[len(argument) -3] == "MEASUREMENT") and (argument[len(argument) -2] == "OF") and (argument[len(argument) -1] == "IMPEDANCE")):
                    com3(argument).MEASUREMENT_OF_IMPEDANCE() 
                elif((argument[len(argument) -2] == "Fiber") and (argument[len(argument) -1] == "measurement")):                  
                    com3(argument).FIBRE_OPTIC_MEASUREMENTS()
                elif((argument[len(argument) -3] == "Characteristics") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "LED")):
                    com3(argument).FIBRE_OPTIC_LED()
                elif((argument[len(argument) -1] == "APD")):
                    com3(argument).APD()  
                elif((argument[len(argument) -3] == "LPF") and (argument[len(argument) -2] == "-EL") and (argument[len(argument) -1] == "2")):
                    E2(argument).LPF()
                elif((argument[len(argument) -4] == "UJT") and (argument[len(argument) -3] == "relax") and (argument[len(argument) -2] == "osc-") and (argument[len(argument) -1] == "EL2")):
                    E2(argument).UJT()
                elif((argument[len(argument) -1] == "RC-EL2")):
                    E2(argument).RC()
                elif((argument[len(argument) -4] == "Single") and (argument[len(argument) -3] == "stage") and (argument[len(argument) -2] == "RC-")and (argument[len(argument) -1]=="EL2")):
                    E2(argument).single_RC()
                elif((argument[len(argument) -1] == "Astable-EL2")):
                    E2(argument).Astable()
                elif((argument[len(argument) -2] == "Monostable-") and (argument[len(argument) -1] == "-EL2")):
                    E2(argument).Monostable()
                elif((argument[len(argument) -1] == "SCHMITT-el2")):
                    E2(argument).SCHMITT()
                elif((argument[len(argument) -4] == "P-n") and (argument[len(argument) -3] == "Junction") and (argument[len(argument) -2] == "Diode")and (argument[len(argument)-1== "Characteristics"])):
                    EL1(argument).PN_Juction()
                elif((argument[len(argument) -4] == "CHARACTERISTICS") and (argument[len(argument) -3] == "OF") and (argument[len(argument) -2] == "ZENER") and (argument[len(argument) -1] == "DIODE")):
                    EL1(argument).zener()
                elif((argument[len(argument) -3] == "Half") and (argument[len(argument) -2] == "wave-") and (argument[len(argument) -1] == "EL1") ):
                    EL1(argument).Half()
                elif((argument[len(argument) -4] == "Full") and (argument[len(argument) -3] == "wave-") and (argument[len(argument) -2] == "EL") and (argument[len(argument) -1] == "1") ):
                    EL1(argument).Full()
                elif((argument[len(argument) -3] == "CB-") and (argument[len(argument) -2] == "EL") and (argument[len(argument) -1] == "1")):
                    EL1(argument).CB()
                elif((argument[len(argument) -2] == "JFET-") and (argument[len(argument) -1] == "EL1")):
                    EL1(argument).JFET()
                elif((argument[len(argument) -2] == "UJT-") and (argument[len(argument) -1] == "EL1")):
                    EL1(argument).UJT()
                elif((argument[len(argument) -1] == "Triac-EL1")):
                    EL1(argument).Triac()
                elif((argument[len(argument) -1] == "SCR-EL1")):
                    EL1(argument).SCR()
                elif((argument[len(argument) -4] == "Clipper") and (argument[len(argument) -3] == "&") and (argument[len(argument) -2] == "clamper-") and (argument[len(argument) -1] == "EL1")):
                    EL1(argument).Clipper()
                elif((argument[len(argument) -3] == "study") and (argument[len(argument) -2] == "of") and (argument[len(argument) -1] == "CRO")):
                    EL1(argument).CB()
                elif((argument[len(argument) -2] == "CE-") and (argument[len(argument) -1] == "EL1") ):
                    EL1(argument).CE()    
                elif((argument[len(argument) -3] == "Biasing") and (argument[len(argument) -2] == "circuit") and (argument[len(argument) -1] == "-EL1")):
                    EL1(argument).Bias()
                elif((argument[len(argument) -4] == "NO") and (argument[len(argument) -3] == "LOAD") and (argument[len(argument) -2] == "AND") and (argument[len(argument) -1] == "BLOCKED")):
                    EM2(argument).NO_LOAD_AND_BLOCKED()
                elif((argument[len(argument) -4] == "SLIP") and (argument[len(argument) -3] == "RING") and (argument[len(argument) -2] == "INDUCTION") and (argument[len(argument) -1] == "MOTOR")):                   
                    EM2(argument).SLIP_RING_INDUCTION_MOTOR()
                elif((argument[len(argument) -4] == "V") and (argument[len(argument) -3] == "AND") and (argument[len(argument) -2] == "INVERTED") and (argument[len(argument) -1] == "V")):
                    EM2(argument).V_AND_INVERTED_V()
                elif((argument[len(argument) -3] == "SINGLE") and (argument[len(argument) -2] == "PHASE") and (argument[len(argument) -1] == "INDUCTION")):
                    EM2(argument).SINGLE_PHASE_INDUCTION()
                elif((argument[len(argument) -4] == "Direct") and (argument[len(argument) -3] == "and") and (argument[len(argument) -2] == "Quadrature") and (argument[len(argument) -1] == "axis")):                   
                    EM2(argument).Direct_and_Quadrature_axis()
                elif((argument[len(argument) -3] == "THREE-PHASE") and (argument[len(argument) -2] == "SQUIRREL") and (argument[len(argument) -1] == "CAGE")):                   
                    EM2(argument).Three_phase()
                elif((argument[len(argument) -1] == "Single_Phase_Transformer")):
                    EE(argument).single_trf()
                elif((argument[len(argument) -1] == "WATTMETER")):
                    EE(argument).wattmeter()
                elif((argument[len(argument) -3] == "EMF")and (argument[len(argument) -2] == "and") and (argument[len(argument) -1] =="MMF" )):
                    EE(argument).emf()
                else:
                    Dummy(title).dummy()
            except ValueError:
                print(json.dumps({"error":"value added error"}))
            


if __name__ == "__main__":
    main(sys.argv[1:],sys.argv[2:])