import pandas as pd
import matplotlib.pyplot as plt
import time
import pyautogui
import pyunpack
import os
import getpass

pyautogui.PAUSE = 2

pyautogui.hotkey('win','r')
pyautogui.write('chrome')
pyautogui.hotkey('enter')
pyautogui.hotkey('ctrl','t')
pyautogui.write('https://drive.google.com/drive/u/0/folders/12DYZtCNYXwU7aXDhPsMJ-j_5yNp-ygua')
pyautogui.hotkey('enter')
time.sleep(10)
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('enter')
time.sleep(5)
pyautogui.press('up')
pyautogui.hotkey('enter')
time.sleep(25)
pyautogui.hotkey('alt','f4')
usuario = (getpass.getuser())
diretorio = (r'C:\Users\\'+usuario+'\Downloads\Meu_PESO')
os.mkdir(diretorio)


source1 = r"C:/Users/"+usuario+"/Downloads"
termo_procura = 'drive-download-'

for raiz, diretorios, arquivos in os.walk(source1):
   for arquivo in arquivos:
      if termo_procura in arquivo:
         caminho_completo = os.path.join(raiz, arquivo)
         nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
         tamanho = os.path.getsize(caminho_completo)
         download = 'C:/Users/'+usuario+'/Downloads\\'+nome_arquivo+'.zip'
         Nova_Pasta = 'C:/Users/'+usuario+'/Downloads/Meu_PESO\peso.zip'

os.rename(download,Nova_Pasta)

pyunpack.Archive(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\peso.zip').extractall(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO')


peso_junho_21 = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Junho 21.xlsx')
peso_maio_21 = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Maio 21.xlsx')
peso_abril_21 = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Abril 21.xlsx')
peso_marco_211 = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Março21.xlsx')
peso_marco_21 = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Marco  21.xlsx')
peso_fevereiro_21 = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Fevereiro21.xlsx')
peso_janeiro_21 = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Janeiro21.xlsx')
peso_dezembro = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Dezembro.xlsx')
peso_novembro = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Novembro.xlsx')
peso_outubro = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Outubro.xlsx')
peso_setembro = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Setembro.xlsx')
peso_agosto = pd.read_excel(r'C:\Users\\'+usuario+'\Downloads\Meu_PESO\Peso Agosto.xlsx')

peso_concat=pd.concat([peso_agosto,peso_setembro,peso_outubro,peso_novembro,peso_dezembro,peso_janeiro_21,peso_fevereiro_21,peso_marco_21,peso_marco_211,peso_abril_21,peso_maio_21,peso_junho_21], axis=0, ignore_index=True)

gra = peso_concat['peso']
plt.plot(gra)
plt.show()




