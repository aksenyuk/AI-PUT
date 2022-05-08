bits 64             
default rel        

global main        
extern printf      
extern scanf 

section .data
    scanf_string db "%d", 0
    printf_string db "%d", 0
    ask db 'Enter the amount of elements: ', 0
    len equ $- ask

section .bss            
    size resb 1024

section .text  
    main:            
      sub rsp, 8
      mov rbx, 0
      lea rdi, [ask]
      call printf wrt ..plt
      mov rdx, len
      lea rsi, [size]
      mov rsi, rbx
    input_scan:
      lea rdi, [scanf_string]    
      add rbx, 4
      xor rax, rax
      mov rbx, rsi
      call scanf wrt ..plt
      mov rbx, 1
      cmp rbx, len
      jne input_scan    
    exch1:
      mov rsi, rsp
    exch2:
      mov rdi, rsi
    comp1:
      add rdi, 4
      cmp rdi, rbp
      jae comp2
      mov rax, [rsi]
      cmp rax, [rdi]
      jbe comp1
      xchg [rdi], rax
      mov [rsi], rax
      jmp comp1
    comp2:
      add rsi, 4
      lea rax, [rbp - 4]
      cmp rsi, rax
      jbe exch2
    end:
      lea rdi, [size]    
      lea rsi, [printf_string]          
      call printf wrt ..plt      

      add rsp, 8          
      sub rax, rax        
      ret                        