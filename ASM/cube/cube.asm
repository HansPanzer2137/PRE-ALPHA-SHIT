;compile it using masm in visual studio code

section .data

section .bss

section .text

global _start

_start:
    ; set up the graphics mode
    mov ax, 0x4f02 ; set graphics mode function
    xor bx, bx ; use mode 0 (320x200 with 256 colors)
    int 0x10 ; call the interrupt

    ; set up the palette
    mov dx, 0x3c8 ; set palette function
    mov al, 0 ; start at color 0
    out dx, al
    inc dx ; move to the data register
    mov cx, 256*3 ; set up a loop to write all 256 colors
    rep outsb ; write the colors to the palette

    ; set up the vertices for the cube
    mov ax, 0x0400 ; set starting point for vertices
    mov word [es:ax], 0 ; x coordinate
    mov word [es:ax+2], 0 ; y coordinate
    mov word [es:ax+4], 0 ; z coordinate
    add ax, 6 ; move to the next vertex
    mov word [es:ax], 0 ; x coordinate
    mov word [es:ax+2], 0 ; y coordinate
    mov word [es:ax+4], 50 ; z coordinate
    add ax, 6 ; move to the next vertex
    mov word [es:ax], 50 ; x coordinate
    mov word [es:ax+2], 0 ; y coordinate
    mov word [es:ax+4], 50 ; z coordinate
    add ax, 6 ; move to the next vertex
    mov word [es:ax], 50 ; x coordinate
    mov word [es:ax+2], 0 ; y coordinate
    mov word [es:ax+4], 0 ; z coordinate
    add ax, 6 ; move to the next vertex
    mov word [es:ax], 0 ; x coordinate
    mov word [es:ax+2], 50 ; y coordinate
    mov word [es:ax+4], 0 ; z coordinate
    add ax, 6 ; move to the next vertex
    mov word [es:ax], 0 ; x coordinate
    mov word [es:ax+2], 50 ; y coordinate
    mov word [es:ax+4], 50 ; z coordinate
    add ax, 6 ; move to the next vertex
    mov word [es:ax], 50 ; x coordinate
    mov word [es:ax+2], 50 ; y coordinate
    mov word [es:ax+4], 50 ; z coordinate
    add ax, 6 ; move to the next vertex
    mov word [es:ax], 50 ; x coordinate
    mov word [es:ax+2], 50 ; y coordinate
    mov word [es:ax+4], 0 ; z coordinate

    ; set up the faces for the cube
    mov ax, 0x0412 ; set starting point for faces
    mov word [es:ax], 4 ; number of vertices in this face
    mov word [es:ax+2], 0 ; index of the first vertex
    mov word [es:ax+4], 1 ; index of the second vertex
    mov word [es:ax+6], 2 ; index of the third vertex
    mov word [es:ax+8], 3 ; index of the fourth vertex
    add ax, 10 ; move to the next face