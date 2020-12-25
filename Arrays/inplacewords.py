def reverse_words(msg):

    def reverseword(start, end):
        while (start != end and start < end):
            temp=msg[start]
            msg[start]= msg[end]
            msg[end]=temp
            start+=1
            end-=1
        print (msg)


    reverseword(0,len(msg)-1)


    start=0
    end=0
    for i in range (0, len(msg)):
        if msg[i] ==  ' ':
            end = i-1
            reverseword(start, end)
            start=end+2
        elif i == (len(msg)-1):
            reverseword(start, len(msg)-1)
   
        




reverse_words ([ 'l', 'a', 'n', 'd', 'e', 'd', ' ', 'h', 'a', 's', ' ',
  'e', 'a', 'g', 'l', 'e', ' ', 't', 'h', 'e' ])