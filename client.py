#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple python application for download the title of free books that we can
download by the webpage: https://www.packtpub.com/packt/offers/free-learning/

@author: marcelpv96@marcelpv96.com
'''
import urllib2


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
        L'unic que ens interesara sera el html amb l'etiqueta  dotd-title
        """
        pass

    def main(self):
        htmlBeforeParse = self.getWeb('https://www.packtpub.com/packt/offers/free-learning/')
        data = self.getData(htmlBeforeParse)
        return data

if __name__ == "__main__":
    client = Client()
    print client.main()
