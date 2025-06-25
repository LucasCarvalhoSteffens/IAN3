# Ontologias e Redes Semânticas: Aplicações em Inteligência Artificial

## Introdução
Ontologias e redes semânticas são ferramentas fundamentais em Inteligência Artificial (IA) para representação e organização de conhecimento de forma estruturada e legível por máquinas. Uma ontologia é uma representação formal de conhecimento, composta por conceitos de um domínio e suas relações. Redes semânticas, por sua vez, são grafos que representam conhecimento por meio de nós (conceitos) e arestas (relações). Essas ferramentas permitem que sistemas realizem raciocínio, inferência e compartilhamento de conhecimento, sendo essenciais em aplicações que exigem interoperabilidade e processamento inteligente de dados.

Este relatório explora os fundamentos teóricos de ontologias e redes semânticas, técnicas e ferramentas associadas, exemplos de aplicações reais e propõe uma implementação prática no contexto da Engenharia de Software.

## Fundamentos Teóricos
### Ontologias
Uma ontologia define um vocabulário para um domínio específico, incluindo:
- **Classes**: Representam conceitos ou entidades (ex.: "Pessoa", "Veículo").
- **Propriedades**: Definem relações (ex.: "temParte", "éUm") ou atributos (ex.: "nome", "idade").
- **Indivíduos**: Instâncias de classes (ex.: "João" como instância de "Pessoa").
- **Axiomas**: Regras ou restrições que governam as relações (ex.: "Toda Pessoa tem um nome").

Ontologias são frequentemente expressas usando padrões como OWL (Web Ontology Language) e RDF (Resource Description Framework), que fornecem semântica formal para representação de conhecimento.

### Redes Semânticas
Redes semânticas são grafos direcionados ou não direcionados onde:
- **Nós** representam conceitos ou entidades.
- **Arestas** representam relações, como "é-um" (herança) ou "parte-de" (composição).

Redes semânticas são predecessoras das ontologias modernas e, embora menos formais, são amplamente usadas em processamento de linguagem natural, grafos de conhecimento e sistemas de raciocínio.

### Princípios Chave
- **Interoperabilidade**: Ontologias permitem que sistemas compartilhem e reutilizem conhecimento entre plataformas.
- **Raciocínio**: Mecanismos de inferência usam ontologias para derivar novos conhecimentos (ex.: se "João é uma Pessoa" e "Toda Pessoa é Mortal", então "João é Mortal").
- **Escalabilidade**: Redes semânticas e ontologias podem modelar domínios complexos com grandes conjuntos de dados.

## Técnicas, Ferramentas e Frameworks
### Técnicas
- **Desenvolvimento de Ontologias**: Metodologias como Methontology ou Neon guiam a criação de ontologias, envolvendo etapas como especificação, conceituação, formalização e implementação.
- **Raciocínio**: Técnicas como Lógica Descritiva (Description Logic) e consultas SPARQL permitem inferência e extração de dados em ontologias.
- **Tecnologias da Web Semântica**: Padrões como RDF, OWL e SPARQL facilitam a criação de bases de conhecimento legíveis por máquinas.
- **Algoritmos de Grafos**: Redes semânticas utilizam algoritmos de travessia de grafos (ex.: busca em largura) para tarefas como descoberta de caminhos ou relações.

### Ferramentas e Frameworks
- **Protégé**: Editor de ontologias de código aberto para criação e visualização de ontologias OWL.
- **Apache Jena**: Framework Java para aplicações de web semântica, suportando RDF e SPARQL.
- **OWL API**: Biblioteca para manipulação programática de ontologias OWL.
- **SPARQL**: Linguagem de consulta para bancos de dados RDF, usada para extrair informações de grafos de conhecimento.
- **GraphDB**: Triplestore para armazenamento e consulta de dados RDF.
- **RDFLib**: Biblioteca Python para trabalhar com RDF e ontologias.

## Aplicações Reais e Estudos de Caso
### Estudo de Caso 1: DBpedia
DBpedia é uma base de conhecimento em larga escala que extrai dados estruturados da Wikipédia e os representa como uma ontologia RDF. Ela permite:
- **Interoperabilidade**: Aplicações podem consultar a DBpedia para obter informações estruturadas sobre entidades (ex.: pessoas, lugares).
- **Aplicações**: Usada em sistemas de resposta a perguntas, motores de recomendação e busca semântica.

### Estudo de Caso 2: Saúde (SNOMED CT)
SNOMED Clinical Terms (SNOMED CT) é uma ontologia usada em saúde para padronizar informações clínicas. Ela suporta:
- **Interoperabilidade**: Permite compartilhamento de dados entre sistemas de saúde.
- **Aplicações**: Suporte a decisões clínicas, integração de registros de pacientes e pesquisa médica.

### Estudo de Caso 3: Google Knowledge Graph
O Knowledge Graph do Google utiliza redes semânticas para melhorar os resultados de busca, entendendo relações entre entidades (ex.: conectar "Leonardo da Vinci" à "Mona Lisa"). Ele possibilita:
- **Aplicações**: Melhoria na precisão de buscas, desambiguação de entidades e recomendações contextuais.

## Proposta de Aplicação: Sistema de Recomendação de Filmes Baseado em Ontologia
### Visão Geral
Propomos um sistema simples de recomendação de filmes baseado em ontologia, implementado em Python usando RDFLib e SPARQL. O sistema modela filmes, gêneros e preferências de usuários como uma ontologia e recomenda filmes com base em consultas do usuário.

### Detalhes da Implementação
- **Design da Ontologia**: Criar uma ontologia RDF com classes (`Filme`, `Gênero`, `Usuário`), propriedades (`temGênero`, `gostaDeGênero`) e indivíduos (filmes e usuários específicos).
- **Ferramentas**: Usar RDFLib para criação da ontologia e SPARQL para consultas.
- **Funcionalidade**: Usuários inserem seus gêneros preferidos, e o sistema consulta a ontologia para recomendar filmes.
- **Plataforma**: Implementado no Google Colab para acessibilidade e reprodutibilidade.

### Código
Abaixo está o código Python para o sistema de recomendação de filmes.

```python
from rdflib import Graph, RDF, RDFS, OWL, Namespace, Literal

# Inicializar o grafo RDF
g = Graph()
EX = Namespace("http://example.org/")
g.bind("ex", EX)

# Definir classes da ontologia
g.add((EX.Filme, RDF.type, OWL.Class))
g.add((EX.Genero, RDF.type, OWL.Class))
g.add((EX.Usuario, RDF.type, OWL.Class))

# Definir propriedades
g.add((EX.temGenero, RDF.type, OWL.ObjectProperty))
g.add((EX.gostaDeGenero, RDF.type, OWL.ObjectProperty))
g.add((EX.nome, RDF.type, OWL.DatatypeProperty))
g.add((EX.ano, RDF.type, OWL.DatatypeProperty))

# Adicionar dados de exemplo (filmes, gêneros e usuários)
# Filmes
g.add((EX.Inception, RDF.type, EX.Filme))
g.add((EX.Inception, EX.temGenero, EX.FiccaoCientifica))
g.add((EX.Inception, EX.temGenero, EX.Acao))
g.add((EX.Inception, EX.nome, Literal("Inception")))
g.add((EX.Inception, EX.ano, Literal(2010)))

g.add((EX.TheMatrix, RDF.type, EX.Filme))
g.add((EX.TheMatrix, EX.temGenero, EX.FiccaoCientifica))
g.add((EX.TheMatrix, EX.temGenero, EX.Acao))
g.add((EX.TheMatrix, EX.nome, Literal("The Matrix")))
g.add((EX.TheMatrix, EX.ano, Literal(1999)))

g.add((EX.LordOfTheRings, RDF.type, EX.Filme))
g.add((EX.LordOfTheRings, EX.temGenero, EX.Fantasia))
g.add((EX.LordOfTheRings, EX.nome, Literal("The Lord of the Rings: The Fellowship of the Ring")))
g.add((EX.LordOfTheRings, EX.ano, Literal(2001)))

g.add((EX.PulpFiction, RDF.type, EX.Filme))
g.add((EX.PulpFiction, EX.temGenero, EX.Crime))
g.add((EX.PulpFiction, EX.temGenero, EX.Acao))
g.add((EX.PulpFiction, EX.nome, Literal("Pulp Fiction")))
g.add((EX.PulpFiction, EX.ano, Literal(1994)))

# Gêneros
g.add((EX.FiccaoCientifica, RDF.type, EX.Genero))
g.add((EX.Acao, RDF.type, EX.Genero))
g.add((EX.Fantasia, RDF.type, EX.Genero))
g.add((EX.Crime, RDF.type, EX.Genero))

# Usuários
g.add((EX.Alice, RDF.type, EX.Usuario))
g.add((EX.Alice, EX.gostaDeGenero, EX.FiccaoCientifica))
g.add((EX.Alice, EX.gostaDeGenero, EX.Acao))

g.add((EX.Bob, RDF.type, EX.Usuario))
g.add((EX.Bob, EX.gostaDeGenero, EX.Fantasia))

g.add((EX.Carol, RDF.type, EX.Usuario))
g.add((EX.Carol, EX.gostaDeGenero, EX.Crime))
g.add((EX.Carol, EX.gostaDeGenero, EX.Acao))

# Consulta 1: Recomendar filmes para um usuário com base em seus gêneros preferidos
def consulta_recomendacao_usuario(usuario):
    query = f"""
        PREFIX ex: <http://example.org/>
        SELECT ?filme ?nome ?ano
        WHERE {{
            ?usuario ex:gostaDeGenero ?genero .
            ?filme ex:temGenero ?genero .
            ?filme ex:nome ?nome .
            ?filme ex:ano ?ano .
            FILTER(?usuario = ex:{usuario})
        }}
        ORDER BY ?ano
    """
    results = g.query(query)
    print(f"\nRecomendações para {usuario}:")
    for row in results:
        print(f"Filme: {row.nome}, Ano: {row.ano}")

# Consulta 2: Listar filmes de um gênero específico
def consulta_filmes_por_genero(genero):
    query = f"""
        PREFIX ex: <http://example.org/>
        SELECT ?filme ?nome ?ano
        WHERE {{
            ?filme ex:temGenero ex:{genero} .
            ?filme ex:nome ?nome .
            ?filme ex:ano ?ano .
        }}
        ORDER BY ?ano
    """
    results = g.query(query)
    print(f"\nFilmes do gênero {genero}:")
    for row in results:
        print(f"Filme: {row.nome}, Ano: {row.ano}")

# Consulta 3: Encontrar usuários que gostam de um gênero específico
def consulta_usuarios_por_genero(genero):
    query = f"""
        PREFIX ex: <http://example.org/>
        SELECT ?usuario
        WHERE {{
            ?usuario ex:gostaDeGenero ex:{genero} .
        }}
    """
    results = g.query(query)
    print(f"\nUsuários que gostam do gênero {genero}:")
    for row in results:
        usuario = str(row.usuario).split('#')[-1]
        print(f"Usuário: {usuario}")

# Consulta 4: Listar filmes lançados após um determinado ano
def consulta_filmes_por_ano(ano_minimo):
    query = f"""
        PREFIX ex: <http://example.org/>
        SELECT ?filme ?nome ?ano
        WHERE {{
            ?filme ex:nome ?nome .
            ?filme ex:ano ?ano .
            FILTER(?ano >= {ano_minimo})
        }}
        ORDER BY ?ano
    """
    results = g.query(query)
    print(f"\nFilmes lançados após {ano_minimo}:")
    for row in results:
        print(f"Filme: {row.nome}, Ano: {row.ano}")

# Executar as consultas
print("=== Sistema de Recomendação de Filmes ===")
consulta_recomendacao_usuario("Alice")
consulta_recomendacao_usuario("Bob")
consulta_recomendacao_usuario("Carol")
consulta_filmes_por_genero("FiccaoCientifica")
consulta_usuarios_por_genero("Acao")
consulta_filmes_por_ano(2000)
```

## Conclusão
Ontologias e redes semânticas são ferramentas poderosas para representação e raciocínio de conhecimento em IA. Elas permitem interoperabilidade, suportam raciocínio complexo e alimentam aplicações em diversos domínios, como saúde, motores de busca e sistemas de recomendação. Nosso sistema de recomendação de filmes demonstra como ontologias podem ser aplicadas de forma prática usando ferramentas acessíveis como RDFLib e SPARQL. Trabalhos futuros poderiam expandir a ontologia com propriedades adicionais (ex.: atores, avaliações) para melhorar a precisão das recomendações.

## Referências
- Gruber, T. R. (1993). A Translation Approach to Portable Ontology Specifications. *Knowledge Acquisition*.
- W3C. (2012). OWL 2 Web Ontology Language Document Overview.
- Lehmann, J., et al. (2015). DBpedia – A Large-scale, Multilingual Knowledge Base Extracted from Wikipedia. *Semantic Web Journal*.
- Documentação do RDFLib: https://rdflib.readthedocs.io/
- Protégé: https://protege.stanford.edu/
