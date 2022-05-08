bits 64            
default rel         

global main         
extern printf       
extern scanf        

section .data           
    scanf_string db "%s", 0
    printf_string db "%s", 0xa, 0

section .bss            
    input resb 1024
    output resb 1024

section .text           
    main:               
        sub rsp, 8          

        lea rdi, [scanf_string]      
        lea rsi, [input]            
        call scanf wrt ..plt         

        ; REPZ approach
        mov rcx, 1024           
        lea rsi, [input]         
        lea rdi, [output]       
        cld                     
        repz movsb              

        ; simple approach
    ;     lea rbx, [input]            
    ;     lea rcx, [output]          
    ; copy_char:              
    ;     mov al, [rbx]               
    ;     mov [rcx], al               

    ;     inc rbx                 
    ;     inc rcx                

    ;     cmp al, 0               
    ;     jne copy_char          

        lea rdi, [printf_string]     
        lea rsi, [output]           
        call printf wrt ..plt       

        add rsp, 8          
        xor rax, rax        
        ret                 
