.text
main:
	#inicializa��o
	addi $t0, $zero, 10 #n�mero de itera��es
	addi $t1, $zero, 0 #contador
	addi $t2, $zero, 3 #valor
	addi $t3, $zero, 3 #valor a ser incrementado
	
loop: 
	beq $t1, $t0, fim # encerra caso o contador seja igual ao n�mero de itera��es
	add $t2, $t2, $t3 #incrementa
	addi $t1, $t1, 1 #incrementa o contador
	
	j loop

fim:
	#fim
	