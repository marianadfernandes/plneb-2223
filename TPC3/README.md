Conteúdos da pasta:

- Ficheiro python com a implementação do código para separação do contéudo do ficheiro dicionario_medico.txt em termo e descrição, para além da construção do código para gerar um ficheiro html;
- Ficheiro html com tabela de descrição e termo, além de uma barra para auxiliar a pesquisa de termos pela sua inicial.

Raciocínio por detrás do código:

1º Começou-se por tentar marcar todos os termos com #T=
- Para isso, foi necessário primeiro tratar de uma exceção encontrada nas descrições, que iniciava com letra minúscula, em vez de maiúscula;

2º Eliminaram-se os espaços encontrados entre termo e descrição ou entre as linhas das descrições quando ocorria quebra de página;

3º Como já não seriam necessários, retiraram-se os \f e os marcadores usados para os termos (#T=);
- O processo implementado seguinte é semelhante ao feito em aula. Inclui-se na expressão regex \n? para serem captados os casos em que existia um \n entre o termo e a descrição;

- De notar que foram necessários tratar 3 casos especiais à mão pois não foi possível resolver com expressões regulares pois estavam a ser indevidamente marcados como termos, não estavam a ser suprimidas as linhas que se encontravam a meio da descrição ou a descrição não se encontrava pela ordem presente no pdf;
	- Esses casos foram, por ordem, no termo dacnomania, Fahrenheit e sulco.