keywords = ["asm","else","new","this","auto","enum","operator","throw","bool","explicit","private","true","break","export","protected","try","case","extern","public","typedef","catch","false","register","typeid","char","float","reinterpret_cast","typename","class","for","return","union","const","friend","short","unsigned","const_cast","goto","signed",	"using","continue","if","sizeof","virtual","default","inline","static","void","delete",	"int","static_cast","volatile","do","long","struct","wchar_t","double","mutable","switch","while",'dynamic_cast',"namespace","template"]
operator = ["+", "-", "*", "/", "%", "="]
punc_marks = ["<", ">", "#", "}", "{", "(", ")", ":", ";", ","]
key_count = [0]*len(keywords)
op_count = [0]*len(operator)
pun_count = [0]*len(punc_marks)              

with open('1.cpp', 'r') as f:
    sample = f.read()
    
words = []
lines = sample.split("\n")
for i in lines:
    for j in range(0, len(i)):
        if i[j] == "/" and i[j+1] == "/":
            lines.remove(i)
            
for word in lines:
    words.append(word.split(" "))
    if word.split("(") not in words:
        words.append(word.split("("))
    else:
        if word.split(")") not in words:
            words.append(word.split(")"))
        else:
            if word.split(")") not in words:
                words.append(word.split(")"))
            else:
                if word.split("#") not in words:
                    words.append(word.split(";"))
                else:
                    if word.split("#") not in words:
                        words.append(word.split("#"))
                    else:
                        if word.split("<") not in words:
                            words.append(word.split("<"))
                        else:
                            if word.split(">") not in words:
                                words.append(word.split(">"))
                            else:
                                if word.split(":") not in words: 
                                    words.append(word.split(":"))
                                    
for line in sample:
    for ch in line:
        for i in range(0, len(operator)):
            if ch == operator[i]:
                op_count[i] += 1
        for i in range(0, len(punc_marks)):
            if ch == punc_marks[i]:
                pun_count[i] += 1
            
    
q = []
for i in words:
    for j in i:
        q.append(j)
    
for i in range(0, len(q)):
    if q[i] in keywords:
        ind = keywords.index(q[i])
        key_count[ind] += 1
    if q[i] in operator:
        ind = operator.index(q[i])
        op_count[ind] += 1
    if q[i] in punc_marks:
        ind = punc_marks.index(q[i])
        pun_count[ind] += 1
        
print("Keywords :")
for i in range(0, len(keywords)):
    if key_count[i] > 0:
        print(keywords[i], ": ", key_count[i])
print("\nOperators :")
for i in range(0, len(operator)):
    if op_count[i] > 0:
        print(operator[i], ": ", op_count[i])
print("\nPunctuation Marks :")
for i in range(0, len(punc_marks)):
    if pun_count[i] > 0:
        print(punc_marks[i], ": ", pun_count[i])