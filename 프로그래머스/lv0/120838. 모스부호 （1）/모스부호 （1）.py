def solution(letter):
    answer = ''
    
    morse_dict = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    
    morse = []
    alphabet = []
    
    splt = letter.split(' ')
    
    for idx, mor in enumerate(morse_dict):
        alp = morse_dict[mor]
        morse.append(mor)
        alphabet.append(alp)
    
    print(morse)
    print(alphabet)
    
    for i in splt:
        if i in morse:
            idx = morse.index(i)
            print(idx)
            answer += alphabet[idx]
            
    
    
    return answer