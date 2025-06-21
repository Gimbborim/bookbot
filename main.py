import sys
from stats import conteopalabras
from stats import conteocar
from stats import ordenar


def get_book_text(filepath):

    with open(filepath) as f:
        contenido = f.read()
        conteo = conteopalabras(contenido)
        diccionario = conteocar(contenido)
    return conteo, diccionario


def ordenamiento(diccionario):
    orden = ordenar(diccionario)
    return orden


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    a = sys.argv[1]
    a1, b1 = get_book_text(a)
    c1 = ordenamiento(b1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {a}...")
    print("----------- Word Count ----------")
    print(f"Found {a1} total words")
    print("--------- Character Count -------")

    for i in c1:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


main()
