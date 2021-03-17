from pytube import YouTube
import pyautogui
link = pyautogui.prompt("Digite o link que deseja baixar") # Inserir link do vídeo
path = pyautogui.prompt("Digite o diretório que deseja salvar o vídeo:  ") # Inserir local de download 
yt = YouTube(link)
pyautogui.alert("Estou baixando seu vídeo ! Por favor , aguarde um instante . \nTítulo : %s" %(yt.title) ) #Mostra junto da mensagem de download o título do vídeo
ys = yt.streams.get_highest_resolution() #Seleciona a melhor qualidade de vídeo disponível
ys.download(path) # Path é a pasta para salver o vídeo , passada como parâmetro para a função download.
pyautogui.alert("Download completo ! \nVídeo salvo em %s" %(path))




