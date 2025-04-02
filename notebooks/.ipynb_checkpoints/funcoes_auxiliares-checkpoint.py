import textwrap
import string

def decode_review(text, index):
    """Função para juntar textos de acordo de cada índice na Base de Dados.

    Parameters
    ----------
    text : List[int]
        Lista com os números inteiros quw representam as palavras codificadas.
    index : Dict[str]
        Dicionário que contém o índice de cada palavra usada.

    Returns
    -------
    text
        Retorna um texto com a avaliação de cada usuário sobre um respectivo filme.
    """
    
    reverse_index = {value: key for key, value in index.items()}
    return " ".join([reverse_index.get(value, "<UNK>") for value in text])



def print_review(text, width=50):
    """Função para comprimir o texto de acordo com o número de caracteres limite.

    Parameters
    ----------
    text : str
        Texto a ser formatado.
    width : numeric, opcional
        O número máximo de caracteres que será utilizado por linha.
    """
    
    wrapper = textwrap.TextWrapper(width=width)
    print(wrapper.fill(text))


def encode_review(text, index):
    """Função para modificar o texto escrito para um texto sem pontuação, além de converter cada palavra em um índice de acordo com o dicionário.

    Parameters
    ----------
    text : str
        Texto a ser formatado.
    index : Dict[str]
        Dicionário que contém o índice de cada palavra usada.

    Returns
    -------
    text
        Retorna um texto com a avaliação de cada usuário sobre um respectivo filme.
    """
    text = text.translate(str.maketrans("", "",string.punctuation)).lower()
    return [index.get(word, 2) for word in text.split(" ")]