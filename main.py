from stats import count_chars, count_words, generate_sorted_report
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  
def print_report(report):
    print("--------- Character Count -------")
    for item in report:
      if item["char"].isalpha():
        print(f"{item["char"]}: {item["count"]}")

def main():
  try:
    filepath = sys.argv[1]
  except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  print("============ BOOKBOT ============")
  book = get_book_text(filepath)
  num_words = count_words(book)
  num_chars = count_chars(book)
  sorted_report = generate_sorted_report(num_chars)

  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print_report(sorted_report)
    
  print("============= END ===============")

main()