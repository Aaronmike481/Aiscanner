import unicodedata
import re
from confusable_homoglyphs import confusables


CONFUSABLES = {
    # Cyrillic → Latin
    'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'х': 'x',
    'у': 'y', 'к': 'k', 'м': 'm', 'н': 'h', 'в': 'b', 'т': 't',
    'А': 'a', 'В': 'b', 'Е': 'e', 'К': 'k', 'М': 'm', 'Н': 'h',
    'О': 'o', 'Р': 'p', 'С': 'c', 'Т': 't', 'У': 'y', 'Х': 'x',
    
    # Greek → Latin
    'Α': 'a', 'Β': 'b', 'Ε': 'e', 'Ζ': 'z', 'Η': 'h', 'Ι': 'i',
    'Κ': 'k', 'Μ': 'm', 'Ν': 'n', 'Ο': 'o', 'Ρ': 'p', 'Τ': 't',
    'Υ': 'y', 'Χ': 'x',
}

def normalize(text: str) -> str:
    
    text = unicodedata.normalize('NFKC', text)
    
    
    text = re.sub(r'[\u200b-\u200f\u2028-\u202f\u2060-\u206f\ue000-\ue007f\ufeff]', '', text)
    
   
    text = ''.join(CONFUSABLES.get(c, c) for c in text)
    
   
    text = text.casefold()
    
   
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()


def confusable(text: str) -> str:
    result = []
    for char in text:
        is_conf = confusables.is_confusable(char, greedy=True)
        if is_conf:
            next_list = is_conf[0].get('homoglyphs', [])
            if next_list:
                result.append(next_list[0].get('c', char))
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)