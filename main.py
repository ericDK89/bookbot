def main():
    book = get_book("./books/frankenstein.txt")
    count = count_words(book)
    letters = count_letter(book)    
    letters_loop = loop(letters)
    text = f"""--- Begin report of books/frankenstein.txt ---

{count} words found in the document
           
            
{letters_loop}--- End report ---"""

    print(text)

def get_book(path):
    with open(path) as f:
        return f.read()


def count_words(book):
    a = book.split()
    return len(a)


def count_letter(book):
    d = {}

    for w in book:
        lw = w.lower()

        if "a" <= w <= "z" or "A" <= w <= "Z":
            if lw not in d:
                d[lw] = 1
            elif lw in d:
                d[lw] = d[lw] + 1

    return d


def loop(letters):
    a = ""

    for w in letters:
        a += f"The '{w}' character was found {letters[w]} times\n"

    return a

main()
