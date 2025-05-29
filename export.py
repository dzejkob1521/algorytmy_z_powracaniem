import math

def export_to_tikz(graph, filename="graph_output.tex"):
    radius = 1.5
    positions = []
    tikz_lines = []

    for i in range(graph.nodes):
        angle = 2 * math.pi * i / graph.nodes
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        positions.append((x, y))
        tikz_lines.append(f"\\node (N{i}) at ({x:.2f},{y:.2f}) {{{i+1}}};")

    printed_edges = set()
    for u in range(graph.nodes):
        for v in graph.a_list[u]:
            if u < v and (u, v) not in printed_edges:
                tikz_lines.append(f"\\draw (N{u}) -- (N{v});")
                printed_edges.add((u, v))

    full_tex = [
        "\\documentclass{article}",
        "\\usepackage{tikz}",
        "\\begin{document}",
        "\\begin{center}",
        "\\begin{tikzpicture}[scale=3, every node/.style={circle, draw, fill=blue!20}]",
        *tikz_lines,
        "\\end{tikzpicture}",
        "\\end{center}",
        "\\end{document}"
    ]

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(full_tex))
        print(f"Dokument LaTeX zapisany do pliku: {filename}")
    except IOError as e:
        print(f"Błąd zapisu do pliku: {e}")
