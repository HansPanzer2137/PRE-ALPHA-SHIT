#include "bib/kernel.h"

void kernel_entry()
{
    init_vga();
    print_s("Testing VGA.h");
    print_nl();
}