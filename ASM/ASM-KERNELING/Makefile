make install:
	nasm -f bin kernel.asm -o kernel.bin
	nasm -f bin stage2ofGod.asm -o bootloader.bin

	dd if=/dev/zero of=disk.img bs=1024 count=1440
	dd if=bootloader.bin of=disk.img conv=notrunc

make test:
	qemu-system-x86_64 -drive format=raw,file=disk.img

make clean:
	rm -rf kernel.bin bootloader.bin disk.img ROSDOS.flp rosdos.bin