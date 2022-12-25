#ifndef SHELL_H
#define SHELL_H

#include "../utils.h"
#include "../keyboard.h"
#include "../kernel.h"
#include "../char.h"
#include "../text.h"
#include "DISK.h"




void checkCOMMAND()
{
  if(cipa[0]=='A'){

    print_new_line();
    print_string("THIS IS FUCKING WORK BROOOO!");
  
  }else{
    
    if(cipa[0]=='H' && cipa[1]=='E' && cipa[2]=='L' && cipa[3]=='P'){
      
      print_new_line();
      print_string("YOU ARE FUCKING NIGGA FROM CIA");
    
    }else{
      
      if(cipa[0]=='S' && cipa[1]=='T' && cipa[2]=='A' && cipa[3]=='C' && cipa[4]=='H' && cipa[5]=='U'){
          
          print_new_line();
          init_vga(BRIGHT_GREEN, BLACK);
          for(int slex = 0; slex<=10;slex++){
            print_new_line();
            print_string("STACHU IS FUCKING CIA NIGGA AGENT");  //thats a true
          };

      }else{

          if(cipa[0]=='R' && cipa[1]=='O' && cipa[2]=='S' && cipa[3]=='-' && cipa[4]=='R' && cipa[5]=='O' && cipa[6]=='O' && cipa[7]=='T'){
                
                print_new_line();
                print_string("OK BRO BUT YOU MUST LOGIN TO BE STALIN");
                for(int i = 30; i>=0; i--){
                  cipa[i] = '0';
                };
                n = 0;
                SHELLlogin();
              
          }else{
              
                print_new_line();
                print_string("BAD COMMAND! YOU WANT TO GO TO GULAG?");
              }
          }
        }
      }
  }
             //working [TODO] : MAKE shellCommands.h with this function





void SHELLlogin(){
  init_vga(BRIGHT_GREEN, BLACK);
  print_string("STALINIUM SHELL LOGIN");
  print_new_line();
  print_string("User:");
  for(int e = 30; e>=0; e--){
                  cipa[e] = '0';
  };
  test_input();
  if(cipa[0]=='S' && cipa[1]=='T' && cipa[2]=='A' && cipa[3]=='L' && cipa[4]=='I' && cipa[5]=='N'){
    print_new_line();
    print_string("Password:");
    for(int f = 30; f>=0; f--){
                  cipa[f] = '0';
    };
    test_input();
    if(cipa[0]=='T' && cipa[1]=='O' && cipa[2]=='O' && cipa[3]=='R'){
      print_new_line();
      print_string("YOU ARE NOW STALIN");
      
    }

  }
}




extern void DONUT();



#endif