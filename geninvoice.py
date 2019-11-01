# Test di estrazione e parsing di un file XML estrazione Numero e data fattura
import xml.etree.ElementTree as ET
import os

# apre il file scaricato dal sito fatturapa.gov.it come modello
model = ET.parse('IT01234567890_FPA01.xml')

#Estrae il progressivo invio (pi)dal file modello
pivatr = model.find('FatturaElettronicaHeader/DatiTrasmissione/IdTrasmittente/IdCodice').text
pi = model.find('FatturaElettronicaHeader/DatiTrasmissione/ProgressivoInvio').text
print(pivatr, pi)

# classe usata per la generazione del progressivo invio


