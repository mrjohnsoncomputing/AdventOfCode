import hashlib, threading

def findHash(i, zeros):
    key = "iwrupvqb"
    while True:
        newkey = key + str(i)
        hsh = hashlib.md5(newkey.encode()) 
        hx = hsh.hexdigest()
        #print(hx[0:5])
        if hx[0:zeros] == "0"*zeros:
            print(hx, i)
            return i
        i+=1

#thread = threading.Thread(target=findHash, args=(key, 1) )
#thread.daemon = True
#thread.start()
answer = findHash(0, 6)
print(answer)
