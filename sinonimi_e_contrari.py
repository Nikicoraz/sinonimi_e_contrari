from bs4 import BeautifulSoup as __bs
from urllib import request as __request
from enum import Enum as __Enum

__BASE_SITO = "https://sapere.virgilio.it/parole/sinonimi-e-contrari/"

class Request(__Enum):
    SINONIMI = "Sinonimi"
    CONTRARI = "Contrari"

def __richiedi_parole(http : __request.urlopen, richiesta : Request):
    """
    Ricerca le parole della pagina delle sinonimi e contrari.

    Parameters
    ----------
    http : request.urlopen
        Url della pagina contenente le parole.
    richiesta : REQUEST
        Tipo di richiesta.
    
    Returns
    -------
    A list of str of the synonyms or the antonyms of the word.
    Returns an empty list if the word is not found.
    
    """
    bs = __bs(http, "html.parser")
    p = bs.find("p", {"class": "sct-macrotipo"}, text=richiesta.value)
    if(p == None):
        return []
    p_parole = p.find_next("p")
    a_parole = p_parole.find_all("a")
    return [x.get_text() for x in a_parole]



def richiedi(parola : str, richiesta : Request):
    """
    Richiede la pagina delle sinonimi e contrari di una parola.
    
    Parameters
    ----------
    parola : str
        Parola da cercare.
    richiesta : REQUEST
        Tipo di richiesta.

    Returns
    -------
    A list of str of the synonyms or the antonyms of the word.
    Returns an empty list if the word is not found.

    """
    http = __request.urlopen(__BASE_SITO + parola.lower())
    if richiesta == Request.SINONIMI or richiesta == Request.CONTRARI:
        return __richiedi_parole(http, richiesta)
    else:
        raise ValueError("Richiesta non valida.")