#return selected pins from file
def getPins_parameter():
 filepath = ('/home/pi/gpio/gpio_pins.lst')
 with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       if cnt == int(getPins()):
        sl = line.strip()
        setPins(str(cnt))
        #print("Line {}: {}".format(cnt, sl))
        return sl
       else:
        line = fp.readline()
        cnt += 1

#write pin to file
def setPins(pinState):
 fobj_out = open("/home/pi/gpio/gpio_pins.per","w")
 fobj_out.write(pinState)
 fobj_out.close()

#read and return pin from file
def getPins():
 fobj = open("/home/pi/gpio/gpio_pins.per")
 for line in fobj:
   return line.rstrip()
 fobj.close()

#setPins("000011110000")
#getPins_parameter(4)
