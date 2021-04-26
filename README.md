# Trabalho de CG, IA, Comp Evo, Redes
## _Participantes: Arquimedes, Wykthor, Audrey, Bruno_
Combinações: 
- Wykthor/Bruno (Redes) 
- Wykthor/Bruno/Audrey/Arquimedes (Comp Evo)
- Wykthor/Arquimedes(CG)
- Wykthor/? (IA)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
Inteligência Artificial: Usar uma rede neural profunda hiperparametrizada por um algoritmo genético para fazer a previsão de recompensa possível, dada uma ação, seguindo o algoritmo de Q-learning.

Protocolo de rede:

Cliente e servidor trocam informações, da seguinte forma:

Cliente gera um jogo(mapa, jogador, posição inicial do monstro), inicia um jogo, e o jogador faz um movimento, depois disso, o cliente conecta ao servidor e envia essas informações, com uma conexão estabelecida(provavelmente stateful), a cada movimento do jogador, o cliente envia este para o servidor, que com sua representação interna do jogo, decide um movimento para o monstro, e retorna este para o jogador. Repita até o monstro capturar o jogador, o jogador vencer, ou desistir.

Ao final da partida, o servidor vai ter calculado a recompensa para a IA que guiou o monstro, e treina-la de acordo com isso.

Especificação:

Primeira conexão: Estabelecer identidade do cliente(ID gerado pelo servidor), começar uma conexão TCP, gerar uma representação no servidor do tabuleiro(mxn posições). Talvez explorar a persistência de dados.

Conexões subsequentes: Enviar ID do usuário, junto de um identificador de requisição(Perdeu, ganhou, desistiu, próximo movimento, salvar jogo(talvez)) e informação pertinente(No caso de próximo movimento, seria a tupla (x,y) onde explicitaria o movimento do jogador para o servidor, atualizando assim o tabuleiro)

No caso de fim do jogo, a conexão é finalizada e o cliente deverá conectar-se de novo para iniciar outro jogo.

Conexão final: Requisitar o fim da conexão.

Ex. de Formato:

cliente:

INIC

nome: wykthor

mapa: [[0,0,j,0],[0,0,0,0],[0,0,0,0],[0,m,0,0]]


servidor:

INIC

id: 02


fim de ex.
