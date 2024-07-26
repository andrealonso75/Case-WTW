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
- 
