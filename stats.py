def count_words(text):
  return len(text.split())

def count_chars(text):
  report = {}
  for char in text:
    lower_char = char.lower()
    if not lower_char in report:
      report[lower_char] = 0
    report[lower_char] += 1
  
  return report

def sort_on_count(dict):
  return dict["count"]

def generate_sorted_report(chars_count):
  ordered_report = []
  for key in chars_count:
    char = {}
    char["char"] = key
    char["count"] = chars_count[key]
    ordered_report.append(char)

  ordered_report.sort(reverse=True, key=sort_on_count)
  return ordered_report