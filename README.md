# Jogo de Adivinhação de Países

## Introdução
Este é um jogo simples que consulta a API do IBGE para exibir informações de algum país aleatório, o qual o jogador deve tentar descobrir o nome. A inspiração para fazer isso veio a partir do site https://artigo.app/ e da vontade de praticar sobre consumo de APIs.

## Como Jogar
1. Execute o arquivo Python `main.py`.
2. O jogo irá sortear um país a partir da requisição da API e fornecer a **localização** do país, uma **descrição sobre seu histórico** e uma dica (**primeira letra** do nome do país e qual **moeda** é utilizada lá).
3. O jogador insere sua resposta.
4. Se a resposta estiver correta, o jogador recebe uma mensagem de parabéns. Caso contrário, a resposta correta é revelada.
5. Após cada rodada, o jogador tem a opção de jogar novamente ou sair do jogo.
6. Um histórico das respostas corretas é mantido e exibido no final do jogo.

## Possíveis Melhorias Futuras
- Armazenar o histórico de jogo em um arquivo txt.
- Integrar a aplicação com o framework Flask para exibir em um site.
