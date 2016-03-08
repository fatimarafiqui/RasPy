# Basic Database Connection
import MySQLdb

db = MySQLdb.connect("localhost", "Student","","mona")
curs = db.cursor()

che = 1
flag = 0
while (che==1): 
  f = raw_input ('Family member name\n')
  print f
  curs.execute("INSERT INTO mona(name)VALUES(%s)",(f))
 db.commit()
  flag = flag+1
  che = input ("More Family Members (1/0)\n")
  if (che==1):
     print "Enter More members\n"
  if (che==0):
     break
print flag 
print "members of family\n "
