import subprocess
import os

def compile_c_files():
    # List all files with the ".c" extension in the current directory
    c_files = [f for f in os.listdir(".") if f.endswith(".c")]
    print(c_files)

    # Compile each C file
    for c_file in c_files:
        object_file = os.path.splitext(c_file)[0] + ".o"
        avr_gcc_path = r'E:\Embedded\AVR\AVR\02-Tools\03-IMT SDK\03- IMT SDK\IMT_SDK_Win_64\WinAVR\bin\avr-gcc.exe'
        result = subprocess.run([avr_gcc_path, '-mmcu=atmega32', '-Os', '-c', c_file, '-o', object_file])

        if result.returncode != 0:
            print(f"Error compiling {c_file}")
            return

    print("Compilation completed .")

def link_object_files():
    # List all files with the ".o" extension in the current directory
    object_files = [f for f in os.listdir(".") if f.endswith(".o")]

    # Link the object files
    avr_gcc_path = r'E:\Embedded\AVR\AVR\02-Tools\03-IMT SDK\03- IMT SDK\IMT_SDK_Win_64\WinAVR\bin\avr-gcc.exe' 
    result = subprocess.run([avr_gcc_path, '-mmcu=atmega32', '-Os'] + object_files + ['-o', 'output.elf'])
    if result.returncode != 0:
        print("Error linking object files")
        return

    print("Linking completed .")

def generate_hex_file():
    # Generate the hex file
    avr_objcopy_path=r'E:\Embedded\AVR\AVR\02-Tools\03-IMT SDK\03- IMT SDK\IMT_SDK_Win_64\WinAVR\bin\avr-objcopy.exe'
    result = subprocess.run([avr_objcopy_path, '-O', 'ihex', '-R', '.eeprom', 'output.elf', 'output.hex'])
    if result.returncode != 0:
        print("Error generating hex file")
        return

    print("Hex file generation completed .")

# Compile the C files
compile_c_files()

# Link the object files
link_object_files()

# Generate the hex file
generate_hex_file()