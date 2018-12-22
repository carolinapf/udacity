# udacity
nível_fácil ="A Barata diz que tem __1__ saias de filó\n" "É __2__ da barata, ela tem é __3__ só\n" "Ah ra ra, ho ro ró, ela __4__ é uma só!"

nível_fácil_respostas = ["sete", "mentira", "uma", "tem"]

nível_médio = "A Barata diz que tem um __1__ de __2__\n" "É __3__ da barata, o pé dela é __4__\n" "Ah ra ra, ho ró ró, o pé dela é peludo!"

nível_médio_respostas = ["sapato", "veludo", "mentira", "peludo"]

nível_difícil = "A Barata diz que tem um __1__ de __2__\n" "É mentira da barata, ela tem é __3__ dura\n" "Ah ra ra , ho ró ró, ela tem é casca __4__"

nível_difícil_respostas = ["anel", "formatura", "casca", "dura"]

perguntas = ["__1__", "__2__","__3__","__4__"]

def get_nível():
    print ("Olá! Por favor, selecione um nível. Você tem 4 tentativas por pergunta.")
    nível = input("Digite fácil, médio ou difícil\n").lower()
    if nível=="fácil":
        parágrafo(nível_fácil, perguntas, nível_fácil_respostas)
    elif nível=="médio":
        parágrafo(nível_médio, perguntas, nível_médio_respostas)
    elif nível=="difícil":
        parágrafo(nível_difícil, perguntas, nível_difícil_respostas)
    else:
        print ("Escolha apenas fácil, médio ou difícil")
    print (get_nível)

def parágrafo(quiz, espaços, respostas):
	print (quiz)
	for número_espaço in range(0, len(espaços)):
		resposta_input = input("Qual é " + espaços[número_espaço] +"?")
		tentativas = 1
		max_tentativas = 4
		while resposta_input.lower()!= respostas[número_espaço]:
			tentativas += 1
			resposta_input = input("Você errou =( Vamos tentar novamente. Qual é a palavra" + espaços[número_espaço] + "?")
			if tentativas == max_tentativas:
				print ("Você errou novamente. Vamos tentar mais uma vez!")
				get_nível()
		else:
			quiz = quiz.replace(espaços[número_espaço], respostas[número_espaço])
			print("Correto! " + quiz)
	if len(espaços) == len(respostas):
		print ("Parabéns! Quer tentar outro nível?")
		get_nível()

get_nível()
