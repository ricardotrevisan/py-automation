import subprocess
import os, platform
import talker
from dotenv import load_dotenv

load_dotenv()
IP_DEVICE = os.environ.get('IP_DEVICE')

if platform.system().lower()=="windows":
    proc = subprocess.Popen(["ping", "-t", IP_DEVICE], stdout=subprocess.PIPE)
else:
    proc = subprocess.Popen(["ping", IP_DEVICE], stdout=subprocess.PIPE)

print(proc.stdout.readline())
flag = False

while True:
  line = proc.stdout.readline()
  if not line:
    break

  linha = line.decode('utf-8')
  #print("len: ", len(linha.split()))
  #print("split: ", linha.split())
  #print("conteudo:", linha.split()[2])

  connected_ip = line.decode('utf-8').split()[2]
  if connected_ip.__contains__(IP_DEVICE) and not flag:
      talker.speech("Dispositivo Conectado")
      #print("Connected")
      flag = True
  elif not connected_ip.__contains__(IP_DEVICE):
      print("nao conectado")
      flag = False
