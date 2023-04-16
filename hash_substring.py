# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose 
    # which input type will follow
    teksts = input()
    if "I" in teksts:
        pattern=input().rstrip()
        text=input().rstrip()   
    elif "F" in teksts:
        file='./tests/06'
        try:
            with open (file, mode="r") as f:
                pattern=f.readline().strip()
                text=f.readline().strip()
        except Exception as e:
            print("Error:", str(e))
        
    else: 
        print ("Input error")
        return
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    d=256  #characters in input alphabet
    q=257  #number tu use for hashing

    pattern_hash=text_hash=0

    for j in range(len(pattern)):
        pattern_hash=(d*pattern_hash+ord(pattern[j])) %q
        text_hash=(d*text_hash+ord(text[j]))%q
    gadijumi=[]

    for j in range (len(text)-len(pattern)+1):
        if pattern_hash==text_hash and text[j : j+ len(pattern)]==pattern:
            gadijumi.append(j)
        if j<len(text)- len(pattern):
            text_hash=(d*(text_hash-ord(text[j])*pow(d, len(pattern)-1, q))+ord (text[j+len(pattern)]))%q
    return gadijumi

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

