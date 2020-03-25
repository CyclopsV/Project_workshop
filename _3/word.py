import re


def throw_trash(string: str) -> str:
    reg: re.Pattern = re.compile('[^a-zA-Za-яА-ЯёЁ ]')
    string: str = reg.sub('', string).replace('  ', ' ')
    return string.lower()


def count_word(string: str) -> dict:
    s_list: list = string.split(' ')
    count: dict = {}
    for i in s_list:
        count.update({i: s_list.count(i)})
    count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    return count


def coding_words(count_w: dict, stat: str = 'all') -> dict:
    w: list = list(count_w.keys())
    words: dict = {}
    for i in range(len(count_w)):
        if stat == 'all':
            words.update({w[i]: i})
        else:
            if count_w[w[i]] > 1:
                words.update({w[i]: i+1})
            else:
                break
    return words


def coding_string(string: str, coding_dict: dict) -> str:
    s_list: list = string.split(' ')
    for i in range(len(s_list)):
        s_list[i] = str(coding_dict.get(s_list[i], 0))
    return ' '.join(s_list)


s: str = input('Введите строку: ')
if not s:
    s = 'Hello!@ приве фы hello ва#фыв!а% а! world #&фф &!*!#$#%@*+_ world!'

s = throw_trash(s)
count = count_word(s)
all_words = coding_words(count)
print(all_words)
words = coding_words(count, stat='no_all')
all_cod_str = coding_string(s, all_words)
cod_str = coding_string(s, words)

print(f'До кодировки:\n{s}\n\nПри кодировке всех слов:\n{all_cod_str}\n\nПри кодировке слов (len(word)>1):\n{cod_str}')
