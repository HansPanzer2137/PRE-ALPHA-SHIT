# using PeachPy: https://github.com/Maratyszcza/PeachPy
# to install libary: pip install --upgrade git+https://github.com/Maratyszcza/PeachPy

# [!] Warining
# Currently PeachPy is not installing good on Windows, I recomend use native Linux / WSL2


#simple usage of x64 asm registers without C file usage

from peachpy import *
from peachpy.x86_64 import *

#max cross-platform compatibility argument
x = Argument(ptr(const_float_), name="x")
# auto-detect
y = Argument(ptr(const_float_))



# Everything inside the `with` statement is function body
with Function("DotProduct", (x, y), float_,
  # Enable instructions up to SSE4.2
  # PeachPy will report error if you accidentally use a newer instruction
  target=uarch.default + isa.sse4_2):

  # Request two 64-bit general-purpose registers. No need to specify exact names.
  reg_x, reg_y = GeneralPurposeRegister64(), GeneralPurposeRegister64()

  # This is a cross-platform way to load arguments. PeachPy will map it to something proper later.
  LOAD.ARGUMENT(reg_x, x)
  LOAD.ARGUMENT(reg_y, y)

  # Also request a virtual 128-bit SIMD register...
  xmm_x = XMMRegister()
  # ...and fill it with data
  MOVAPS(xmm_x, [reg_x])
  # It is fine to mix virtual and physical (xmm0-xmm15) registers in the same code
  MOVAPS(xmm2, [reg_y])

  # Execute dot product instruction, put result into xmm_x
  DPPS(xmm_x, xmm2, 0xF1)

  # This is a cross-platform way to return results. PeachPy will take care of ABI specifics.
  RETURN(xmm_x)


#SAMPLE OF EXECUTE

# Use MS-COFF format with Microsoft ABI for Windows
#python -m peachpy.x86_64 -mabi=ms -mimage-format=ms-coff -o example.obj example.py
# Use Mach-O format with SysV ABI for OS X
#python -m peachpy.x86_64 -mabi=sysv -mimage-format=mach-o -o example.o example.py
# Use ELF format with SysV ABI for Linux x86-64
#python -m peachpy.x86_64 -mabi=sysv -mimage-format=elf -o example.o example.py
# Use ELF format with x32 ABI for Linux x32 (x86-64 with 32-bit pointer)
#python -m peachpy.x86_64 -mabi=x32 -mimage-format=elf -o example.o example.py
# Use ELF format with Native Client x86-64 ABI for Chromium x86-64
#python -m peachpy.x86_64 -mabi=nacl -mimage-format=elf -o example.o example.py


#for more info visit
# https://github.com/Maratyszcza/PeachPy

