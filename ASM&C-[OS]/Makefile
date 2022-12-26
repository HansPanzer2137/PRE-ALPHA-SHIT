make install:
	mkdir -p packKern/ISO
	mkdir -p packKern/kernelBIN 
	as --32 boot.s -o packKern/boot.o
	

	gcc -m32 -c bib/utils.c -o packKern/utils.o -std=gnu99 -ffreestanding -O1 -Wall -Wextra  
	gcc -m32 -c bib/SHELL/shell.c -o packKern/shell.c -std=gnu99 -ffreestanding -O1 -Wall -Wextra -lm
	gcc -m32 -c bib/char.c -o packKern/char.o -std=gnu99 -ffreestanding -O1 -Wall -Wextra 
	gcc -m32 -c kernel.c -o packKern/kernel.o -std=gnu99 -ffreestanding -O1 -Wall -Wextra 
	ld -m elf_i386 -T linker.ld packKern/utils.o packKern/char.o packKern/boot.o packKern/kernel.o -o packKern/kernelBIN/TempleOS32.bin 
	grub-file --is-x86-multiboot packKern/kernelBIN/TempleOS32.bin 
	mkdir -p isodir/boot/grub
	cp packKern/kernelBIN/ROS-OS.bin isodir/boot/TempleOS32.bin
	cp grub.cfg isodir/boot/grub/grub.cfg
	grub-mkrescue -o packKern/ISO/TempleOS32.iso isodir


make test-kernel:
	qemu-system-i386 -kernel TempleOS32.bin

make run:
	qemu-system-i386 -cdrom packKern/ISO/TempleOS32.iso

make clean:
	sudo rm -rf boot.o kernel.o MyOS.bin myos.bin myos.iso MyOS.iso isodir a.out foo.o packKern/*