from pbkdf2 import crypt

if __name__ == '__main__':
  pwhash = crypt("secret")
  alleged_pw = raw_input("Enter password: ")
  if pwhash == crypt(alleged_pw, pwhash):
      print "Password good"
  else:
      print "Invalid password"