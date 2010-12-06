moduleNames= ['base64']
modules = map(__import__, moduleNames)
modules

def NumberFromChar(InputString):
  OutputString=ord(InputString)
  return OutputString

def CharFromNumber(InputString):
  OutputString=chr(InputString)
  return OutputString

def WordLength(InputString):
  OutputString=len(InputString)
  return OutputString

def IntegerNumber(InputString,Base):
  OutputString=int(InputString,Base)
  return OutputString

def Decrypt(message,code):
  message2 = "";ie = 0
  encmessage = modules[0].b64decode(message)
  list=[char for char in encmessage if char!='\n']
  clist=[char for char in code if char!='\n']
  for j in range(0,WordLength(list),16):
    for m in range(0,8):
      if ie+IntegerNumber(clist[m],16)<=WordLength(list):
        message2=message2+CharFromNumber(NumberFromChar(list[ie+IntegerNumber(clist[m],16)])-IntegerNumber(clist[m+8],16))
    ie=ie+16
  return message2.rstrip(' ')

def Decoder(message,index):
  if index==1:
    code="ba98763223b38343"
  elif index==2:
    code="d37e194800000000"
  elif index==3:
    code="38a7629b43303002"
  elif index==4:
    code="38d762ce433833b2"
  message2=Decrypt(message,code)
  return message2
