#include "bib/kernel.h"
#include "bib/utils.h"
#include "bib/char.h"
#include "bib/types.h"
#include "bib/text.h"

void kernel_entry()
{
    init_vga(BRIGHT_GREEN, BLACK);
    print_string("Testing VGA.h");
    print_new_line();
}