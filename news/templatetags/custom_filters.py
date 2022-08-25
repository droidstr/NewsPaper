from django import template

register = template.Library()


@register.filter()
def censor(text):
    """
   text: текст, к которому нужно применить фильтр
   Цензурирует все слова, первый символ в которых в верхнем
   регистре, а все остальные - в нижнем
   """
    if not isinstance(text, str):
        raise TypeError('filter censor applied to non-string value')
    text = text.split() # если не текст, райзается AttributeError
    result = ''
    for word in text:
        result += ' ' + word[0] + '*' * (len(word) - 1) if word.capitalize() == word and word[0].isalpha() else ' ' + word
    return result
    print('filter censor applied to non-string value')
    return text.strip()
