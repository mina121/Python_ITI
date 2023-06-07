import subprocess
import win32com.client

# set the path to the Proteus executable
proteus_path = r"C:\Program Files (x86)\Labcenter Electronics\Proteus 8 Professional\BIN\PDS.EXE"

# set the path to the schematic file containing the AVR ATMega32
schematic_path = r"C:\Users\User\Documents\JOHN\g.pdsprj"

# set the path to the hex file to load into the AVR component
hex_file_path = r"F:\linux\New folder\output.hex"


# build the hex file using Make
make_command = "make"
subprocess.run(make_command, shell=True)

# create a new instance of Proteus Schematic Application
app = win32com.client.Dispatch("Proteus.Application")

# open the schematic file containing the AVR ATMega32
schematic = app.SchematicSheet
schematic.Load(schematic_path)

# get the AVR ATMega32 component on the schematic
avr_component = schematic.FindComponent("ATMega32")

# load the hex file into the AVR component
avr_component.LoadHex(hex_file_path)

# simulate the schematic for 10 seconds
app.SimulationRun(10000)

# close the schematic application
app.Quit()
