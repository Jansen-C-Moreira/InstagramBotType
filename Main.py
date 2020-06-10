from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from tkinter import *





class InstagramBot():
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("int1.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enable", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Users\User\Desktop\Gecko\geckodriver.exe"
        )

    def login(self,):
        driver = self.driver
        driver.get("http://www.instagram.com")
        time.sleep(3)
        loginusuario = driver.find_element_by_xpath("//input[@name='username']")
        loginusuario.clear()
        loginusuario.send_keys(self.username)
        time.sleep(3)
        passwd = driver.find_element_by_xpath( "//input[@name='password']")
        passwd.clear()
        passwd.send_keys(self.password)
        time.sleep(3)
        passwd.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_nas_fotos()

    def TypeLikeHuman(self, lugar):
        print("Começando a escrever-->")
        with open('cidades.csv', 'r') as texto:
            linhas = texto.readlines()
        lista = []
        for linha in linhas:
            lista.append(linha)
        cidadealeatotia = random.choice(lista)
        for letra in cidadealeatotia:
            lugar.send_keys(letra)
            time.sleep(random.randint(1, 5) / 30)
        print("Escrito.")
    def comente_nas_fotos(self):
        driver = self.driver
        time.sleep(7)
        driver.get(self.url)
        time.sleep(5)
        u = 0
        while True:
            print("Até agora foram feitos", u, "comentários")
            for i in range(0, 3):
                try:
                    driver.find_element_by_class_name('Ypffh').click()
                    commentario = driver.find_element_by_class_name("Ypffh")
                    time.sleep(random.randint(2, 5))
                    self.TypeLikeHuman(commentario)
                    time.sleep(random.randint(3, 5))
                    driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                    time.sleep(random.randint(3, 5))
                    u += 2
                except Exception as e:
                    print(e)
                    print("Erro ao escrever!")
                    time.sleep(300)
            time.sleep(600)
            print("Passaram 10 minutos")
            time.sleep(600)
            print("Passaram 20 minutos")
            time.sleep(600)
            print("Passaram 30 minutos\nRecomeçando")
def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()
class Window1():
    def __init__(self, master):
        self.master = master
        self.master.title("BotInstagtram")
        self.master.geometry("700x500")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.user = StringVar()
        self.passwd = StringVar()
        self.url = StringVar()
        self.LabelTitle = Label(self.frame, text="BOT INSTAGRAM", font=("verdana", 30), bd=20)
        self.LabelTitle.grid(row=0, columnspan=2, pady=20)
        #-----------------------------------------------------------
        #Frames
        self.Loginframe1 = Frame(self.frame, width=500, height=150, bd=20, relief='ridge')
        self.Loginframe1.grid(row=1, column=0, sticky=W)
        self.Loginframe2 = Frame(self.frame, width=500, height=50, bd=20, relief='ridge')
        self.Loginframe2.grid(row=2, column=0, sticky=W)

        #-----------------------------------------------------------
        #Frame1
        self.LabelUser = Label(self.Loginframe1, text="Name", font=('arial', 15, "bold"))
        self.LabelUser.grid()
        self.LabeltxtUser = Entry(self.Loginframe1, text="Nome", font=('arial', 15, "bold"), textvariable=self.user)
        self.LabeltxtUser.grid(row=0, column=1)
        self.LabelPasswd = Label(self.Loginframe1, text="Pass", font=('arial', 15, "bold"))
        self.LabelPasswd.grid(row=1, column=0)
        self.LabeltxtPasswd = Entry(self.Loginframe1, text="Senha", font=('arial', 15, "bold"), show="*", textvariable=self.passwd)
        self.LabeltxtPasswd.grid(row=1, column=1)
        self.Botar = Label(self.Loginframe1, text="URL", font=('arial', 12, 'bold'))
        self.Botar.grid(row=2, column=0)
        self.LabeltxtURL = Entry(self.Loginframe1, text="URL", font=('arial', 15, "bold"), textvariable=self.url)
        self.LabeltxtURL.grid(row=2, column=1)

        #-----------------------------------------------------------
        #Frame2

        self.TestarConta = Button(self.Loginframe2, text="Run", width=10, font=('arial', 12, 'bold'), command=self.Login)
        self.TestarConta.grid()
        #-----------------------------------------------------------
        #Frame3



    def Login(self):
        name = (self.user.get())
        passwd = (self.passwd.get())
        url = (self.url.get())
        self.lucasbot = InstagramBot(name, passwd, url)
        self.lucasbot.login()



if __name__ == '__main__':
    main()

