#ifndef CURSOR_H
#define CURSOR_H

#include "../types.h"
#include "../keyboard.h"
#include "../char.h"
#include "../text.h"
#include "../utils.h"
#include "../kernel.h"

void enable_cursor(uint8_t cursor_start, uint8_t cursor_end){
    
    outb(0x3D4, 0x0A);
    outb(0x3D5, (inb(0x3D5) & 0xC0) | cursor_start);

    outb(0x3D4, 0x0B);
    outb(0x3D5, (inb(0x3D5) & 0xE0) | cursor_end);
}

void disable_cursor(){

    outb(0x3D4, 0x0A);
    outb(0x3D5, 0x20);
}


#endif