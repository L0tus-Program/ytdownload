from pytube import YouTube
import pyautogui

def download (link):
    path = pyautogui.prompt("Digite o diretório que deseja salvar o vídeo:  ") # Inserir local de download 
    yt = YouTube(link)
    pyautogui.alert("Estou baixando seu vídeo ! Por favor , aguarde um instante . \nTítulo : %s" %(yt.title) ) #Mostra junto da mensagem de download o título do vídeo
    ys = yt.streams.get_highest_resolution() #Seleciona a melhor qualidade de vídeo disponível
    ys.download(path) # Path é a pasta para salver o vídeo , passada como parâmetro para a função download.
    pyautogui.alert("Download completo ! \nVídeo salvo em %s" %(path))



link = pyautogui.prompt("Digite o link que deseja baixar") # Inserir link do vídeo

print(link) #exibe em CONSOLE o retorno do prompt, alocado na variavel link

if link == None: # O "Cancel" do pyatoqui retorna um None
    pyautogui.alert("Programa encerrado")

else:
    download(link)










