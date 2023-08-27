from queue import PriorityQueue

class Node:
   def __init__(self,freq,ch):
      self.left = None
      self.right = None
      self.freq = freq
      self.ch = ch




   def __gt__(self, other):
      return (self.freq> other.freq ) 
def getNode(ch,freq,left,right):
   node=Node(freq,ch)
   node.left = left
   node.right = right
   return node


def encode(root,string,huffmanCode):
  
   if (root==None):
      return  
   if (not root.left and not root.right) :
      huffmanCode[root.ch] = string
   
   encode(root.left, string + "0", huffmanCode)
   encode(root.right, string + "1", huffmanCode)

   
   
def decode(root,rr,index,text,r,c):
   if root==None or index>len(text)-1:
      return 
   if (root.left==None and  root.right==None):
      r=r+root.ch
      index=index+1
      #print("text= ",text[index:])
      if (text[index:]==""):
         output = open("decoded.txt","w+")
         output.write("".join(r))
         print("Decoded file generated as decoded.txt")
      return decode(rr,rr,0,text[index:],r,0)

   
   if (index==0 and c==0):
      c=c+1
   elif(index==0 and c==1):
      index=index+1
   else:
      index=index+1

     
   
   if (text[index] =='0'):
      decode(root.left,rr, index, text,r,c)
   else:
      decode(root.right,rr, index, text,r,c)
	


def buildHuffmanTreeEncode(text):
   dictionary = {}
   for i in text:
      if i in dictionary:
         dictionary[i]=dictionary[i]+1
      else:
         dictionary[i]=1
   pq= PriorityQueue()
   for i in dictionary:
      pq.put(getNode(i,dictionary[i],None,None))
   
   while (pq.qsize()!=1):
      left=pq.get()
      right=pq.get()
      sum=left.freq+right.freq
      pq.put(getNode('' , sum, left, right))
   root = pq.get()
   
   huffmanCode={}
   encode(root, "", huffmanCode)
   string=""
   for c in text:
      string=string+str(huffmanCode[c])
   output = open("encoded.txt","w+")
   output.write("".join(string))
   print("Encoded file generated as encoded.txt")

def buildHuffmanTreeDecode(text,chars,freqq):
   pq=PriorityQueue()
   for i in range(0,len(chars)):
      pq.put(getNode(chars[i],freqq[i],None,None))
   while (pq.qsize()!=1):
      left=pq.get()
      right=pq.get()
      sum=left.freq+right.freq
      pq.put(getNode('' , sum, left, right))
   root = pq.get()
   rr=root
   
   
   index=int(0)
   r=""
   c=0
   decode(root,rr,index,text,r,c)

   
   
   

   

with open("encode.txt", 'r') as f:
    stringToEncode = f.read()



buildHuffmanTreeEncode(stringToEncode)



chars = []
freq = []

file= open("decode.txt", 'r')
data = file.read()
lines=data.splitlines()



stringToDecode=lines[0]
newList = lines[1].split(">")
for word in newList:
   if word == '':
      break
   
   newword = word[1:].split(":")
   chars.append(newword[0])
   freq.append(int(newword[1]))


   
#print("jbhjkwebnjkewnfjkenfdjkwenfejkfnekj",stringToDecode)
buildHuffmanTreeDecode(stringToDecode,chars,freq)


