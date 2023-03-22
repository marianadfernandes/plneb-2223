Esta pasta contém os ficheiros necessários para a resolução do exercício como o ficheiro json do dicionário, txt e html do livro. 

Além disso, contém o ficheiro python com a resolução do exercício comentada. Os principais passos seguidos foram:
- Leitura do ficheiro json com o dicionário médico (dicionario_medico.json);
- Criação de um dicionário para guardar os termos e respetivas descrições retirados do ficheiro json;
- Leitura do ficheiro txt (LIVRO-Doenças-do-Aparelho-Digestivo.txt);
- Procura no ficheiro txt dos termos que se encontram no livro e no dicionário;
	- Para isso, foi necessário tornar os termos do dicionário e os termos encontrados a iniciar em minúsculas e retirar acentuação para ser possível identificar todas as variantes de escrita de cada palavra no texto.
- Leitura do ficheiro html (LIVRO-Doenças-do-Aparelho-Digestivos.html);
- Substituição dos termos encontrados pelo termo + respetiva descrição através da tag <a>
- Escrita do texto do ficheiro html + anotações num novo ficheiro html (livro_anotado.html)