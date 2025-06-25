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