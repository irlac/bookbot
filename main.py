def word_count(text):
    words = text.split()
    
    return len(words)

def char_count(text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    lc_text = text.lower()
    chars = {}
    
    for char in lc_text:
        if char in alpha:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
    
    chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    return chars

def aggregate(text):
    wc = word_count(text)
    cc = char_count(text)
    report = f"--- Begin report of books/frankenstein.txt ---\n{wc} words found in the document\n\n"
    
    for key in cc:
        report += f"The '{key}' character was found {cc[key]} times\n"
        
    report += "--- End report ---"
    return report

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        print(aggregate(file_contents))

main()