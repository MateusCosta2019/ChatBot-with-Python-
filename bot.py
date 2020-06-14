#chat bot para ensino e pratica de ingles

# bibliotecas do chat
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#bibliotecas de esculta
import speech_recognition as sr

#biblioteca de fala
import pyttsx3

#criando um novo bot
bot = ChatBot('Norman')

#setando algumas informações para treinar o bot
conversation = (['Hello', 'Hi, What is your name?', 'Nice to meet you', 'How are you?', 'Fine', 'Where you from?', 'I am from Brasil', 
	'What are you doing?', 'Nothing special.', 'What is your level of English?', 'How long do you study English?', 'How old are you?',])

#
engine = pyttsx3.init() #selecionar o sintetizador


#treinando o bot com o banco de dados e com as conversas setadas 
trainer = ListTrainer(bot)
trainer.train(conversation)

#reconhecedor de audio
recognizer = sr.Recognizer() 

print()

#habilitando o modo de captura de audio 
with sr.Microphone() as source:

	 print("Say something for conversation of me!.")

	 recognizer.adjust_for_ambient_noise(source) # se adptar ao ruido externo do ambiente
	
	 #criando looping de conversa
	 while True:

	 	audio = recognizer.listen(source) # escultado entrada de audio

	 	speech = recognizer.recognize_google(audio, language="en-US") #guardando a captura de audio
	 	
	 	print("You say: ", speech)#imprimindo entrada do usuario

	 	response = bot.get_response(speech) #procesando resposta do bot
	 	
	 	print('Teacher: ', response) #imprimindo resposta do bot

	 	engine.say(response) #lendo a variavel que sera reproduzida
	 	engine.runAndWait() #reproduzindo resposta do bot
