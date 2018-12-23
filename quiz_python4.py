#coding utf-8

#função def: define funções onde terá uma sequencia de comandos, e quando precisar dessas sequência novamente basta chama-la.
#if é uma estrutura de condição que permite avaliar uma expressão e executar uma determinada ação.
#elif avalia as expressões intermediárias antes de usar o else.
#else é utilizado para quando a condição definida por if não é satisfeita.
#while é uma estrutura de repetição onde definni-se uma expressão e um mesmo bloco será executado enquanto a expressão definida for verdadeira.

easy_level ="A Barata diz que tem __1__ saias de filó\n" "É __2__ da barata, ela tem é __3__ só\n" "Ah ra ra, ho ro ró, ela __4__ é uma só!"

easy_level_answers = ["sete", "mentira", "uma", "tem"]

medium_level ="A Barata diz que tem um __1__ de __2__\n" "É __3__ da barata, o pé dela é __4__\n" "Ah ra ra, ho ró ró, o pé dela é peludo!"

medium_level_answers = ["sapato", "veludo", "mentira", "peludo"]

hard_level ="A Barata diz que tem um __1__ de __2__\n" "É mentira da barata, ela tem é __3__ dura\n" "Ah ra ra , ho ró ró, ela tem é casca __4__"

hard_level_answers = ["anel", "formatura", "casca", "dura"]

questions = ["__1__", "__2__","__3__","__4__"]



#a função get_level mostra a pergunta referente ao nível que o usuário digitou.
#a função process_paragraph é responsável pelos parágrafos a serem completados.

def get_level():
    print ("Olá! Por favor, selecione um nível. Você tem 4 tentativas por pergunta.")
    level_name = input("Digite easy, medium ou hard\n").lower()
    if level_name=="easy":
        process_paragraph(easy_level, questions, easy_level_answers)
    elif level_name=="medium":
        process_paragraph(medium_level, questions, medium_level_answers)
    elif level_name=="hard":
        process_paragraph(hard_level, questions, hard_level_answers)
    else:
        print ("Escolha apenas easy, medium ou hard")
    print (get_level)

def process_paragraph(quiz, blanks, answers):
	print (quiz)
	for count_blanks in range(0, len(blanks)):
		answer_input = input("Qual é " + blanks[count_blanks] +"?")
		attempts = 1
		max_attempts = 4
		while answer_input.lower()!= answers[count_blanks]:
			attempts += 1
			answer_input = input("Você errou =( Vamos tentar novamente. Qual é a palavra" + blanks[count_blanks] + "?")
			if attempts == max_attempts:
				print ("Você errou novamente. Vamos tentar mais uma vez!")
				get_level()
		else:
			quiz = quiz.replace(blanks[count_blanks], answers[count_blanks])
			print("Correto! " + quiz)
	if len(blanks) == len(answers):
		print ("Parabéns! Quer tentar outro nível?")
		get_level()

get_level()