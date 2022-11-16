import telebot

bot = telebot.TeleBot("5669638102:AAFrbMg3zaQS0mJdAVRa1A8nMPuw5d0omeM")

#Botão de voltar
@bot.message_handler(commands=["Voltar"])
def Voltar(mensagem):
    responder(mensagem)

#Comando Horarios
@bot.message_handler(commands=["Horario"])
def Horario(mensagem):
    f_h = open("Horarios.txt", 'r')
    bot.reply_to(mensagem, f"{f_h.read()}\n/Voltar  🔙Tela inicial")
    f_h.close()

@bot.message_handler(commands=["Contato"])
def Contato(mensagem):
    f_c = open("Contatos.txt", "r")
    bot.send_message(mensagem.from_user.id, f"{f_c.read()}\n\n/Voltar  🔙Tela inicial")
    f_c.close()

@bot.message_handler(commands=["Videos"])
def Contato(mensagem):
    f_v = open("Videos.txt", "r")
    bot.send_message(mensagem.from_user.id, f"{f_v.read()}\n\n/Voltar  🔙Tela inicial")
    f_v.close()


#Comando Bot
#Caso a msg "/bot" seja enviada no grupo geral, a respota do bot será no privado
@bot.message_handler(commands=["Bot", "bot"])
def Bot(mensagem):
    if mensagem.chat.type == 'group':
        bot.send_message(mensagem.from_user.id,
                         "Olá😊!! Aqui é o bot do Programauto: AutoBOT 🤖!!\nEstou aqui para te ajudar em diversos tópicos relacionados ao nosso projeto.😁")
        # bot.reply_to(mensagem, "Olá!! Aqui é o bot do Programauto!!\nEstou aqui para te ajudar em diversos tópicos relacionados ao nosso projeto.")
        resposta = """
        Quais informações você deseja:
          /Horario das Aulas 📅🕗
          /Contato dos Instrutores ☎️
          /Videos das Aulas Gravadas 📼
          
        Clique nas opções acima para ser Redirecionado 👍
        """
        bot.send_message(mensagem.from_user.id, resposta)
        print(mensagem.chat)


@bot.message_handler(func=lambda mensagem: True) #Decorator para a primeira mensagem
def responder(mensagem):
    if mensagem.chat.type == 'private':
        bot.reply_to(mensagem, "Olá😊!! Aqui é o bot do Programauto: AutoBOT 🤖!!\nEstou aqui para te ajudar em diversos tópicos relacionados ao nosso projeto.😁")
        resposta = """
        Quais informações você deseja:
          /Horario das Aulas 📅🕗
          /Contato dos Instrutores ☎
          /Videos das Aulas Gravadas 📼
        
        Clique nas opções acima para ser Redirecionado 👍"""
        bot.send_message(mensagem.from_user.id, resposta)

bot.polling()