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
import sys


class Client (object):
    def __init__(self, telegramID=None, botID=None):
        self.telegramID = telegramID
        self.botID = botID

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
        # lxml
        bs = bs4.BeautifulSoup(htmlPage, "lxml")
        goal = bs.find("div", "dotd-title").find("h2").text
        return goal.replace("\t", "")

    def send_telegram(self, message):
        """
        Enviar un missatge via telegram a una id utilitzant un bot
        """
        bot = telebot.TeleBot(self.botID)
        bot.send_message(self.telegramID, message)

    def main(self):
        htmlWebPag = self.getWeb(
            'https://www.packtpub.com/packt/offers/free-learning/')
        message = "Today the avaible book is:" + self.getData(htmlWebPag)
        if self.telegramID and self.botID is not None:
            self.send_telegram(message)
        else:
            print message


if __name__ == "__main__":
    if len(sys.argv) == 3:
        client = Client(int(sys.argv[1]), sys.argv[2])
    elif len(sys.argv) == 1:
        client = Client()
    else:
        print "Ús: client.py or client.py < TelegramID > <BotID >"
        sys.exit(-1)
    client.main()
