#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple python application for obatain the title of free books that we can
download by the webpage: https://www.packtpub.com/packt/offers/free-learning/

@author: marcelpv96@marcelpv96.com
'''
import bs4
import urllib2
import telebot

class Client (object):
    def getWeb(self, webPage):
        """
        Obrir web -> urllib2 podem obrir una web i descarregar tot el html que
        la forma.
        """
        f = urllib2.urlopen(webPage)
        html = f.read()
        f.close()
        return html

    def getData(self, htmlPage):
        """
        L'unic que ens interessa es el que trobem dins la classe amb l'etiqueta
        dotd-title, podem parsejar el html amb BeautifulSoup.
        """
        bs = bs4.BeautifulSoup(htmlPage, "lxml")
        items = bs.find("div", "dotd-title")
        item = bs.find("h2")
        for line in item:
            if item != "<h2>" or item != "<\h2>":
                goal = line
        return goal.replace("\t", "")

    def send_telegram(self, message):
        """
        Enviar un missatge via telegram utilitzant un bot.
        """
        bot_id = "338150385:AAEzsfua9rUEp6l3zExAsdiC8kyE0OcouK4"
        bot = telebot.TeleBot(bot_id)
        bot.send_message(333932412,message)

    def main(self):
        htmlWebPag = self.getWeb('https://www.packtpub.com/packt/offers/free-learning/')
        message = "Today the avaible book is:"+self.getData(htmlWebPag)
        self.send_telegram(message)


if __name__ == "__main__":
    client = Client()
    avaibleBook = client.main()
