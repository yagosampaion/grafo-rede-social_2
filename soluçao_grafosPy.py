from collections import deque

# Rede ficticia de conexoes entre cidades brasileiras.
grafo = {
    "Brasília": ["Goiânia", "Belo Horizonte"],
    "Goiânia": ["Brasília", "São Paulo", "Cuiabá"],
    "Belo Horizonte": ["Brasília", "Cuiabá", "Rio de Janeiro"],
    "Cuiabá": ["Goiânia", "Belo Horizonte", "São Paulo", "Curitiba"],
    "São Paulo": ["Goiânia", "Cuiabá", "Curitiba"],
    "Rio de Janeiro": ["Belo Horizonte", "Curitiba", "Porto Alegre"],
    "Curitiba": ["Cuiabá", "São Paulo", "Rio de Janeiro", "Porto Alegre"],
    "Porto Alegre": ["Rio de Janeiro", "Curitiba"],
}


def bfs(rede, origem, destino):
    fila = deque([(origem, [origem])])
    visitados = {origem}
    while fila:
        atual, caminho = fila.popleft()
        if atual == destino:
            return caminho
        for vizinho in rede.get(atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))
    return None


def dfs(rede, origem, destino):
    pilha = [(origem, [origem])]
    visitados = set()
    while pilha:
        atual, caminho = pilha.pop()
        if atual in visitados:
            continue
        visitados.add(atual)
        if atual == destino:
            return caminho
        for vizinho in reversed(rede.get(atual, [])):
            if vizinho not in visitados:
                pilha.append((vizinho, caminho + [vizinho]))
    return None


def bloquear_conexao(rede, cidade_a, cidade_b):
    copia = {cidade: vizinhos.copy() for cidade, vizinhos in rede.items()}
    if cidade_b in copia.get(cidade_a, []):
        copia[cidade_a].remove(cidade_b)
    if cidade_a in copia.get(cidade_b, []):
        copia[cidade_b].remove(cidade_a)
    return copia


def mostrar_resultados(rede, origem, destino):
    for nome, algoritmo in [("BFS", bfs), ("DFS", dfs)]:
        caminho = algoritmo(rede, origem, destino)
        if caminho is None:
            print(f"{nome}: não existe caminho entre as cidades.")
        else:
            print(f"{nome}: {' -> '.join(caminho)}")
            print(f"Quantidade de arestas: {len(caminho) - 1}")


def main():
    print("REDE SIMULADA DE CONEXÕES ENTRE CIDADES")
    print("Cidades disponíveis:", ", ".join(grafo))
    origem = input("Cidade de origem: ").strip()
    destino = input("Cidade de destino: ").strip()
    if origem not in grafo or destino not in grafo:
        print("Cidade inválida. Digite um nome exatamente como aparece na lista.")
        return

    print("\nCENÁRIO 1 - REDE COMPLETA")
    mostrar_resultados(grafo, origem, destino)

    cidade_a, cidade_b = "Goiânia", "São Paulo"
    rede_bloqueada = bloquear_conexao(grafo, cidade_a, cidade_b)
    print(f"\nCENÁRIO 2 - BLOQUEIO ENTRE {cidade_a} E {cidade_b}")
    mostrar_resultados(rede_bloqueada, origem, destino)


if __name__ == "__main__":
    main()