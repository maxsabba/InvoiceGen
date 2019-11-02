import xml.etree.ElementTree as ET
import os
from numpy import base_repr
import random
import sys

iteraction = int(sys.argv[1])


# apre il file scaricato dal sito fatturapa.gov.it come modello
invoice = ET.parse('IT01234567890_FPA01.xml')
fn ='IT01234567890_FPA01.xml'

#crea un oggetto per il tag ProgressivoInvio
#pivatr = invoice.find('FatturaElettronicaHeader/DatiTrasmissione/IdTrasmittente/IdCodice').text
pi = invoice.find('FatturaElettronicaHeader/DatiTrasmissione/ProgressivoInvio')
#print(pivatr)

for i in range(iteraction):
    #  generazione del progressivo invio partendo da un numero casuale
    def calcpi():
        new = random.randrange(1, 60466175)
        #print('il valore è:', new)
        new = base_repr(new, 36)       
        #aggiunge i zeri a sx fino ad un massimo di 5 caratteri
        new = new.rjust(5, '0')
        return new

    newpi = calcpi()
    pi.text = str(newpi)
    #pi.set('updated', 'yes')
    newfile = fn.replace('IT01234567890_FPA01.xml', 'IT01234567890_' + str(newpi) + '.xml')
    invoice.write('./fakexml/'+ newfile, encoding="utf-8", xml_declaration=True)

    
    
