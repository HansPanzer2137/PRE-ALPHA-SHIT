%include "stage2info.inc"
ORG STAGE2_RUN_OFS

BITS 16


start:
    ; Removed the segment and stack code
    call cls
    MOV AH, 06h    ; Scroll up function
    XOR AL, AL     ; Clear entire screen
    XOR CX, CX     ; Upper left corner CH=row, CL=column
    MOV DX, 184FH  ; lower right corner DH=row, DL=column
    MOV BH, 0Ah    ; Green on black (cmd color -h)
    INT 10H
   ; mov si, start_text ; Put string position into SI
    ;call print_string   ; Call our string-printing routine
push bx ;push registers
push cx
push dx
mov ah,0h
int 16h

jmp login_SHELL_TEST


;--------------------------------------------------------------------
;     TEST LOGIN SHELL for version 0.301 of ROS-DOS      
;
;---------------------------------------------------------------------

login_SHELL_TEST:


   call standardSHELL
   mov si, loadingBAR_TEST00
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST01
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST02
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST03
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST04
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST05
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST06
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST07
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST08
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST09
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST10
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST11
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST12
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST13
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST14
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST15
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST16
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST17
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST18
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST19
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST20
   call print_string
   call TIMER

   call cls

   call standardSHELL
   mov si, loadingBAR_TEST21
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST22
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST23
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST24
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST25
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST26
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST27
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST28
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST29
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST30
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST31
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST32
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST33
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST34
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST35
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST36
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST37
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST38
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST39
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST40
   call print_string
   call TIMER

   call cls

call standardSHELL
   mov si, loadingBAR_TEST41
   call print_string
   call TIMER

call standardSHELL
   mov si, loadingBAR_TEST_DONE
   call print_string
   call TIMER

   call cls


   call done
standardSHELL:
   mov si, loginTEST_SHELL
   call print_string

   mov si, loginTEST_SHELL1
   call print_string

   mov si, loginTEST_SHELL2
   call print_string

   mov si, loginTEST_SHELL3
   call print_string

   mov si, loginTEST_SHELL4
   call print_string

   mov si, loginTEST_SHELL5
   call print_string

   mov si, spaceTEST
   call print_string
   
   ret

done:
   jmp login_shell

;--------------------------------------------------------
;     NORMAL SHELL (used in version 0.201 - 0.299 )
;
;--------------------------------------------------------

login_shell:
   mov si, loginTEST_SHELL
   call print_string

   mov si, login_hint
   call print_string

   jmp logUSER
logUSER:
   mov si, login
   call print_string

   mov di, buffer
   call get_string

   mov si, buffer
   cmp byte [si], 0
   je main_program

   mov di, buffer
   mov di, shell_login2
   call strcmp
   jc .logPASS
   jnc .badWORDS

.logPASS:

   mov si, password
   call print_string

   mov di, buffer
   call get_string

   mov si, buffer
   cmp byte [si], 0
   je main_program

   mov si, buffer
   mov di, shell_login1
   call strcmp

   jc .login_GOOD
   jnc .badWORDS

.badWORDS:
   mov si, badPass
   call print_string
   jmp logUSER

.login_GOOD:
   mov si, prompt1
   call print_string
   call cls
   mov si, prompt2
   call print_string
   call cls
   mov si, prompt3
   call print_string
   call cls
   ;MOV BH, 0Ah    ; Green on black (cmd color -h)
   ;INT 10H         ;NOT WORKING
   mov si, systemWORK
   call print_string
   jmp main_program

main_program:
   mov si, prompt
   call print_string

    mov di, buffer
    call get_string

    mov si, buffer
    cmp byte [si], 0
    je main_program

    mov si, buffer
    mov di, cmd_shutdown
    call strcmp
    jc .shutdown

    mov si, buffer
    mov di, cmd_cls
    call strcmp
    jc .cls

    mov si, buffer
    mov di, cmd_dateTEST
    call strcmp
    jc .date

    mov si, buffer
    mov di, cmd_timerTEST
    call strcmp
    jc .timerTEST

    mov si, buffer
    mov di, cmd_timeTEST
    call strcmp
    jc .time

    mov si, buffer
    mov di, cmd_about
    call strcmp
    jc .about

    mov si, buffer
    mov di, cmd_credits
    call strcmp
    jc .credits

    mov si, buffer
    mov di, cmd_diskSHIT
    call strcmp
    jc .diskSHIT

    mov si, buffer
    mov di, cmd_reboot
    call strcmp
    jc .reboot


    mov si, buffer
    mov di, cmd_help
    call strcmp
    jc .helpcomm

    mov si, badcommand
    call print_string
	jmp main_program            ; Jump here - infinite loop!

.reboot:
   mov ax, 0
   int 19h

.timerTEST:
    call cls

    mov si, loadingBAR_TEST00
    call print_string
    call TIMER

    call cls

    mov si, loadingBAR_TEST01
    call print_string
    call TIMER

    call cls

    mov si, loadingBAR_TEST02
    call print_string
    call TIMER

    call cls

    mov si, loadingBAR_TEST03
    call print_string
    call TIMER

    call cls    

    mov si, loadingBAR_TEST_DONE    
    call print_string    
    call TIMER  

    call cls    
    jmp main_program
.cls:
  pusha
  mov ah, 0x00
  mov al, 0x03  ; text mode 80x25 16 colours
  int 0x10
  popa

  MOV BH, 0Ah    ; Green on black (cmd color -h)
  INT 10H

   mov si, systemWORK
   call print_string

  jmp main_program

.helpcomm:
    mov si, text_string
    call print_string

    jmp main_program

.about:
    mov si, about_string
    call print_string

    jmp main_program
.shutdown:
mov ax, 0x1000
mov ax, ss
mov sp, 0xf000
mov ax, 0x5307
mov bx, 0x0001
mov cx, 0x0003
int 0x15

.credits
  mov si, cr_str
  call print_string
  
  jmp main_program
;--------------------------------------------------
;     SHELL DISK PORT CHECK
;
;---------------------------------------------------


.diskSHIT:
   call getsec
   mov si, DONESHIT
   call print_string
   jmp main_program

   

;---------------------------------------------------------
;        TIME FROM BIOS COMMAND
;
;--------------------------------------------------------
;--------------------------------------------------------
.date:
   call get_date
   mov si, date
   call print_string
   jmp main_program


.time:
   call get_time
   mov si, time
   call print_string
   jmp main_program

;------------------------------------------------------------
;        
;  DISK PORT
;------------------------------------------------------------




getsec: 
   push	bp			;save old frame pointer
	mov	bp,sp			;get new frame pointer
	mov	ax,4[bp]		;put drive number into AL
	xor	ah,ah
	mov	cx,6[bp]		;number of sectors to fetch
	mov	dx,8[bp]		;logical record number of 1st sector
	mov     bx,10[bp]		;pointer to transfer address
	int	25h			;BIOS call
	jc	error			;error has occurred if carry flag = 1
	mov	al,00H			;NULL to indicate sucessful completion
	jmp	done1
error:	cmp	al,00H			;detect unspecified error code 00H
	jne	done1			;...change to 0FFh if found to 
	mov	al,0FFH			;...differentiate it from success code
done1:	xor	ah,ah			;return AL only
	popf				;remove flags int 0x25 left on stack
	pop	bp			;restore original frame pointer
	ret				;all done


DISK_READ_ERROR_MSG db 'DISK DESTROYED!!!! IVAN WTF !!!!',13,10,0
DONESHIT db 'DONE TOVARISH!!',13,10,0



;--------------------------------------------------------------
;     GET DATE
;
;----------------------------------------------------------------

get_date:
    mov     ah, 04h             ; get date from bios.
    int     1ah

    mov     bx, date     ; do day.
    mov     al, dl
    call    put_bcd2

    inc     bx                  ; do month.
    mov     al, dh
    call    put_bcd2

    inc     bx                  ; do year.
    mov     al, ch
    call    put_bcd2
    mov     al, cl
    call    put_bcd2

    ret


;-----------------------------------------------------------
;  GET TIME
;
;----------------------------------------------------------

get_time:
    mov     ah, 02h             ; get time from bios.
    int     1ah

    mov     bx, time     ; do hour.
    mov     al, ch
    call    put_bcd2

    inc     bx                  ; do minute.
    mov     al, cl
    call    put_bcd2

    inc     bx                  ; do second.
    mov     al, dh
    call    put_bcd2

    ret
;-------------------------------------------------------------
;   TIMER
;
;------------------------------------------------------------
TIMER:
   MOV     CX, 0FH
   MOV     DX, 4240H
   MOV     AH, 86H
   INT     15H
   ret
;------------------------------------------------------------
; Places two-digit BCD value (in al) as two characters to [bx].
;   bx is advanced by two, ax is destroyed.
put_bcd2:
    push    ax                  ; temporary save for low nybble.
    shr     ax, 4               ; get high nybble as digit.
    and     ax, 0fh
    add     ax, '0'
    mov     [bx], al            ; store that to string.
    inc     bx
    pop     ax                  ; recover low nybble.

    and     ax, 0fh             ; make it digit and store.
    add     ax, '0'
    mov     [bx], al

    inc     bx                  ; leave bx pointing at next char.

    ret


;------------------------------------------------------------------------
;INT 1Ah,  02h (2)        Read Real-Time Clock Time                       many
;
;    Reads the time from the computer's real-time clock.
; 
;       On entry:      AH         02h
; 
;       Returns:       CF         Set if clock not operating; else cleared
;                      CH         Hours (BCD)
;                      CL         Minutes (BCD)
;                      DH         Seconds (BCD)
;                      DL         1 if daylight saving time option; else 0
 

;BCD (Binary coded Decimal) -> Decimal
;TODO: FUCKING BCD<->DECIMAL ENCODER/DECODER

;--------------------------------------------------------
;  BCD TO DECIMAL ENCODER
;
;-------------------------------------------------------

bcd_to_int:
pusha
mov bl, al	; Store entire number for now
and ax, 0Fh	; Zero-out high bits
mov cx, ax	; CH/CL = lower BCD number, zero extended
shr bl, 4	; Move higher BCD number into lower bits, zero fill msb
mov al, 10
mul bl	; AX = 10 * BL
add ax, cx	; Add lower BCD to 10*higher
mov [.tmp], ax
popa
mov ax, [.tmp]	; And return it in AX!
ret
.tmp	dw 0


;--------------------------------------------------------------------
;
;
;--------------------------------------------------------------------






;----------------------------------------------------------------------


;---------------------------------------------------------------------------------------------------------
;
;     ROS-DOS SYSTEM VARIBLE
;     
;
;     EVERY VARIBLE WHICH HAS GOT "TEST" IN NAME IS IN DEVELOPMENT
;     (AND MAYBE IN NEXT UPDATE CAN BE USEFULL (CHANGELOG INFORM YOU))
;
;
;---------------------------------------------------------------------------------------------------------
	


   ;------------------------------------------------
   ;  TIME VARIBLES
   ;  IN DEVELOP
   ;-------------------------------------------


   date db      "00/00/0000", 013,10,0
   time db      "00:00:00", 13,10,0



   ;----------------------------------------------


   cmd_help db 'help', 0
   prompt db 'DOS:/>', 0
   prompt1 db 'Starting ROS-DOS.', 0
   prompt2 db 'Starting ROS-DOS..', 0
   prompt3 db 'Starting ROS-DOS...', 0
   systemWORK db 'ROS-DOS version 0.202',13,10,0
   cmd_shutdown db 'shutdown',0
   cmd_reboot db 'reboot',0
   cmd_cls db 'cls',0
   cmd_about db 'about',0
   cmd_timeTEST db 'time', 0
   cmd_diskSHIT db 'checkdisk',0
   cmd_dateTEST db 'date', 0
   cmd_timerTEST db 'timer',0
   cmd_credits db 'rosdos-credits',0
   badcommand db 'Bad command! Use help command if you dont want to go to Gulag!',13,10,0


   login db 'User: ', 0
   password db 'Password: ',0

   badPass db 'Bad pass Tovarish! You are near Gulag',13,10,0

   shell_login2 db 'root', 0
   shell_login1 db 'toor', 0


   buffer times 64 db 0
    login_hint db 'HINT from Stalin!',13,10,'Default user is root and password is toor',13,10,'In future you can add your own user and set password or not',13,10,' ',13,10,0

    shell_start db '-------------------------------',13,10,'|     ROS-DOS version 0.2     |',13,10,'|  ROS-SOFT CORPORATION 2021  |',13,10,'-------------------------------',13,10,' ',13,10,0

    loadingBAR_TEST00 db '                  [>                                         ]                  ',13,10,0
    loadingBAR_TEST01 db '                  [->                                        ]                  ',13,10,0
    loadingBAR_TEST02 db '                  [-->                                       ]                  ',13,10,0
    loadingBAR_TEST03 db '                  [--->                                      ]                  ',13,10,0
    loadingBAR_TEST04 db '                  [---->                                     ]                  ',13,10,0
    loadingBAR_TEST05 db '                  [----->                                    ]                  ',13,10,0
    loadingBAR_TEST06 db '                  [------>                                   ]                  ',13,10,0
    loadingBAR_TEST07 db '                  [------->                                  ]                  ',13,10,0
    loadingBAR_TEST08 db '                  [-------->                                 ]                  ',13,10,0
    loadingBAR_TEST09 db '                  [--------->                                ]                  ',13,10,0
    loadingBAR_TEST10 db '                  [---------->                               ]                  ',13,10,0
    loadingBAR_TEST11 db '                  [----------->                              ]                  ',13,10,0
    loadingBAR_TEST12 db '                  [------------>                             ]                  ',13,10,0
    loadingBAR_TEST13 db '                  [------------->                            ]                  ',13,10,0
    loadingBAR_TEST14 db '                  [-------------->                           ]                  ',13,10,0
    loadingBAR_TEST15 db '                  [--------------->                          ]                  ',13,10,0
    loadingBAR_TEST16 db '                  [---------------->                         ]                  ',13,10,0
    loadingBAR_TEST17 db '                  [----------------->                        ]                  ',13,10,0
    loadingBAR_TEST18 db '                  [------------------>                       ]                  ',13,10,0
    loadingBAR_TEST19 db '                  [------------------->                      ]                  ',13,10,0
    loadingBAR_TEST20 db '                  [-------------------->                     ]                  ',13,10,0
    loadingBAR_TEST21 db '                  [--------------------->                    ]                  ',13,10,0
    loadingBAR_TEST22 db '                  [---------------------->                   ]                  ',13,10,0
    loadingBAR_TEST23 db '                  [----------------------->                  ]                  ',13,10,0
    loadingBAR_TEST24 db '                  [------------------------>                 ]                  ',13,10,0
    loadingBAR_TEST25 db '                  [------------------------->                ]                  ',13,10,0
    loadingBAR_TEST26 db '                  [-------------------------->               ]                  ',13,10,0
    loadingBAR_TEST27 db '                  [--------------------------->              ]                  ',13,10,0
    loadingBAR_TEST28 db '                  [---------------------------->             ]                  ',13,10,0
    loadingBAR_TEST29 db '                  [----------------------------->            ]                  ',13,10,0
    loadingBAR_TEST30 db '                  [------------------------------>           ]                  ',13,10,0
    loadingBAR_TEST31 db '                  [------------------------------->          ]                  ',13,10,0
    loadingBAR_TEST32 db '                  [-------------------------------->         ]                  ',13,10,0
    loadingBAR_TEST33 db '                  [--------------------------------->        ]                  ',13,10,0
    loadingBAR_TEST34 db '                  [---------------------------------->       ]                  ',13,10,0
    loadingBAR_TEST35 db '                  [----------------------------------->      ]                  ',13,10,0
    loadingBAR_TEST36 db '                  [------------------------------------>     ]                  ',13,10,0
    loadingBAR_TEST37 db '                  [------------------------------------->    ]                  ',13,10,0
    loadingBAR_TEST38 db '                  [-------------------------------------->   ]                  ',13,10,0
    loadingBAR_TEST39 db '                  [--------------------------------------->  ]                  ',13,10,0
    loadingBAR_TEST40 db '                  [----------------------------------------> ]                  ',13,10,0
    loadingBAR_TEST41 db '                  [----------------------------------------->]                  ',13,10,0
    loadingBAR_TEST_DONE db '                  [------------------------------------------]                  ',13,10,0

    spaceTEST db ' ',13,10,0

    loginTEST_SHELL db ' ',13,10,' ',13,10,' ',13,10,' ',13,10,0
    loginTEST_SHELL1 db '                  _------------------------------------------_                  ',13,10,0
    loginTEST_SHELL2 db '                  |                                          |                  ',13,10,0
    loginTEST_SHELL3 db '                  |          ROS-DOS version 0.301           |                  ',13,10,0
    loginTEST_SHELL4 db '                  |                                          |                  ',13,10,0
    loginTEST_SHELL5 db '                  --------------------------------------------                  ',13,10,0

    start_text db 'Starting ROS-DOS...',13,10,0
    text_string db '|HELP MENU| |ROS-DOS v0.1|',13,10,'reboot - reboot bro',13,10,'shutdown - shutdown bro ',13,10,'cls - clear screen',13,10,'about - About ROS-DOS',13,10,'rosdos-credits - about system makers',13,10,' ',13,10,0

    about_string db '|About|',13,10,'ROS-DOS is assembly writed system maked for fun and learn assembly',13,10,0

    message_str db '|Message|',10,13,'Priviet Tovarish!',13,10,'Press button',0

    cr_str db '|Credits|',13,10,'Copyright © 2021 ROS-SOFT Company',13,10,'Main Programer: HansPanzer2137',13,10,'Design: Milosz Haraburda & Pawel Migocki', 13,10,'Special thanks for: Stachu (Mieteq), Patryk Kwasniak and Alex (Mrozon) Sudzik',13,10,' ',13,10,0

    standard db 'DOS:/>',0






credits:
mov si, cr_str  ; Put string position into SI
call print_string   ; Call our string-printing routine
push bx ;push registers
push cx
push dx
mov ah,0h
int 16h
je start



message:
call cls
mov si, message_str ; Put string position into SI
call print_string   ; Call our string-printing routine
push bx ;push registers
push cx
push dx
mov ah,0h
int 16h
je start

cls:
  pusha
  mov ah, 0x00
  mov al, 0x03  ; text mode 80x25 16 colours
  int 0x10
  popa
  ret

about:
call cls
mov si, about_string    ; Put string position into SI
call print_string   ; Call our string-printing routine
push bx ;push registers
push cx
push dx
mov ah,0h
int 16h
je start

print_string:           ; Routine: output string in SI to screen
    mov ah, 0Eh     ; int 10h 'print char' function

.repeat:
    lodsb           ; Get character from string
    cmp al, 0
    je .done        ; If char is zero, end of string
    int 10h         ; Otherwise, print it
    jmp .repeat
.done:
    ret
    

get_string:
   xor cl, cl
.loop:
   mov ah, 0
   int 0x16
   
   cmp al, 0x08
   je .backspace
   
   cmp al, 0x0D
   je .done
   
   cmp cl, 0x3F
   je .loop
   
   mov ah, 0x0E
   int 0x10
   
   stosb
   inc cl
   jmp .loop
.backspace:
   cmp cl, 0
   je .loop
   
   dec di
   mov byte [di], 0
   dec cl
   
   mov ah, 0x0E
   mov al, 0x08
   int 10h
   
   mov al, ' ' 
   int 10h
   
   mov al, 0x08
   int 10h
   
   jmp .loop
   
.done:
   mov al, 0
   stosb
   
   mov ah, 0x0E
   mov al, 0x0D
   int 0x10
   mov al, 0x0A
   int 0x10
   
   ret
strcmp:
.loop:
   mov al, [si]
   mov bl, [di]
   cmp al, bl
   jne .notequal
   
   cmp al, 0
   je .done
   
   inc di
   inc si
   jmp .loop
.notequal:
   clc
   ret
.done:
   stc      
   ret