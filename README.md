# Projeto Final de Computação 1

## Tema: Jogo de Batalha Naval

### Mecânicas:
- Sistema de cadastro/loing;
- Modo Jogador contra Jogador (localmente na mesma máquina);
- Modo Jogador contra Máquina;

## Instruções para jogar:

- ### MENU
  No menu principal, faça login com seus dados ou crie um cadastro se não o tiver feito. Depois de ter feito login, selecione a opção de ***Novo Jogo*** para começar um novo jogo ou selecione a opção ***Carregar Jogo*** para voltar ao ultimo save jogado. **Criando ou salvando um novo jogo, o save antigo será sobrescrito com o novo.**
    
                         
- ### PRIMEIRA ETAPA
  A primeira etapa do jogo consiste em posicionar os seus barcos no tabuleiro. Primeiramente, basta escolher o tipo do barco e sua orientação, que irá ser um input do tipo **[NÚMERO][ORIENTAÇÃO]**, onde número se refere ao tipo do barco, e a orientação se refere a como seu barco se orientará no espaço, *"H"* para horizontal e *"v"* para vertical. Em seguida, é necessário identificar o centro do barco destacado e escolher sua posição no tabuleiro atravez de um input
  do tipo **[LETRA][NÚMERO]** ou **[NÚMERO][LETRA]**.

- ### SEGUNDA ETAPA
  A segunda etapa será onde os jogadores tentarão adivinhar onde o barco do adiversário está posicionado. Todos os espaços do tabuleiro serão encobertos e somente revelados ao realizar-se um ataque a aquela casa específica. Para salvar o jogo, basta selecionar a opção de salvamento. Ela está disponível a cada começo de turno. Após o termino do jogo, o vencedor é anunciado e os tabuleiros de cada jogador são revelados. No tabuleiro revelado ao final do jogo, as casas marcadas com **X** são aquelas onde o pedaço do barco foi destruído.


