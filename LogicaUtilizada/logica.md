# **Construção**
- A construção se deu em 100% python. Achei que dessa forma acabei tendo mais facilidade para definir bem as tabelas.
- A primeira coisa que foi feita foi uma análise descritiva da tabela e suas informações. Com essa leitura, pude descartar a coluna de data de nascimento e idade do Customer (Customer Birthday e Customer Age). Não tinha nexo essas colunas, sendo que se uma compra foi feita apenas dias depois a idade se alterava assim como a data de nascimento.
- O segundo passo foi a criação em VSCode. Aqui é feita a leitura da tabela em xlsx em uma pasta que chama **original**. Após a leitura é feito um check para puxar informações novas que serão salvas em uma nova base dentro de uma pasta chamada **processado**. Esse check se da pela coluna **Order Id** onde ele verifica se há orderId já na base. Se não tiver ele adiciona e se houver ele ignora. Dessa forma é possível ter a base sempre atualizada.
- Após isso, entra a parte de dividir o DataFrame em partes. Assim, consigo separar todas as tabelas para depois mandar ela para o banco de dados.
1. dim_customer
2. dim_manager
3. dim_product
4. dim_store
5. fact_orders
- As tabelas prontas foram salvas em csv dentro da pasta processado/store_split.
- Agora vem a parte de fazer a integração com o banco de dados. Para esse case usei o PostgreSQL. A integração é feita no mesmo notebook em Python e manda cada uma das tabelas atualizadas para o banco.
<img src="/imagens/baseDados.jpg">

### Vendo as tabelas no Power BI
<img src="/imagens/powerBIBanco.jpg">

- Com as tabelas prontas e com todas as ligações feitas, é a hora de visualizar os dados de forma gráfica.



# Resumo

- Andre, por que você não fez via SQL como era pedido, devem estar perguntando. Acabei indo mais no caminho de Python que SQL em si. Para essa tarefa, talvez deva ter sido um caminho mais fácil a ser seguido. Penso que a entrega final talvez seja mais interessante que os meios. A entrega final levei em consideração era ter os dados dentro do banco e replicado no Power BI. Levar isso em consideração em qualquer projeto é muito importante.
# Entrada - Enviar os dados para o banco de dados
# Workflow - Levar os dados para o banco de dados
# Saída - Painel informativo e dinâmico dos dados que estão disponíveis.
  
## As etapas no geral foram:
  1. Análise descritiva da tabela e suas informações (não estava no escopo) 
  2. Leitura da tabela original que pode ser atualizada
  3. Criação da tabela mãe com direito a dados novos inclusos a cada atualização, que é chamada de tabela_mestre
  4. Criação das tabelas de dimensão e fato a partir da tabela_mestre
  5. Criação do banco de dados
  6. Visualização dos dados


