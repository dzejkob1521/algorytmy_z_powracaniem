import sys
import argparse
from algorithms import find_eulerian_cycle, find_hamiltonian_cycle
from export import export_to_tikz
from generators import create_hamiltonian_graph, create_non_hamiltonian_graph

def read_line(prompt=""):
    if sys.stdin.isatty():
        return input(prompt)
    else:
        sys.stdout.write(prompt)
        sys.stdout.flush()
        line = sys.stdin.readline()
        if line:
            print(line.strip())
        return line

def execute_command(comm, graph):
    comm=comm.lower()
    if comm == 'print':
        graph.print_graph()
    elif comm == 'euler':
        find_eulerian_cycle(graph)
    elif comm == 'hamilton':
        find_hamiltonian_cycle(graph)
    elif comm == 'export':
        export_to_tikz(graph)
    elif comm == 'help':
        print("Dostępne komendy:")
        print(" - print: Wyświetla graf")
        print(" - euler: Szuka cyklu Eulera")
        print(" - hamilton: Szuka cyklu Hamiltona")
        print(" - export: Eksportuje graf do pliku TikZ")
        print(" - help: Pomoc")
        print(" - exit: Zakończ program")
    elif comm == 'exit':
        return False
    else:
        print("Nieznana komenda. Użyj 'help' aby zobaczyć dostępne komendy.")
    return True

def handle_command_loop(graph):
    while True:
        try:
            print("action>", end=' ', flush=True)
            comm = read_line().strip().lower()
            if not comm:
                break
            if not execute_command(comm, graph):
                break
        except KeyboardInterrupt:
            print("\nPrzerwano przez użytkownika (Ctrl+C).")
            sys.exit(1)
        except EOFError:
            print("\nKoniec wprowadzania danych (Ctrl+D)")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Generator grafów Hamilton/Nie-Hamilton")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--hamilton', action='store_true', help="Generuje graf Hamiltona")
    group.add_argument('--non-hamilton', action='store_true', help="Generuje graf nie-Hamiltonowski")
    args = parser.parse_args()

    try:
        nodes = int(input("nodes> ").strip())
        if args.hamilton:
            saturation = int(input("saturation (30 or 70)> ").strip())
            if saturation not in (30, 70):
                print("Dla Hamiltona nasycenie musi być 30 lub 70.")
                return
            graph = create_hamiltonian_graph(nodes, saturation)
        elif args.non_hamilton:
            graph = create_non_hamiltonian_graph(nodes)

        handle_command_loop(graph)

    except ValueError:
        print("Błąd: podano nieprawidłowe dane liczbowe.")
    except KeyboardInterrupt:
        print("\nPrzerwano przez użytkownika (Ctrl+C).")
    except EOFError:
        print("\nZakończono wprowadzanie danych (Ctrl+D).")