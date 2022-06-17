# Функция сравнения строк из лекции
def compare(S1, S2):
    ngrams = [S1[i:i + 3] for i in range(len(S1))]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)

    return count / max(len(S1), len(S2))

if __name__ == '__main__':
    s = 'компьютер' # Строка с которой сравниваем
    l = ['компьютер', 'компьютеры', 'компьютерный', 'комп', 'компьютеризация'] # Список строк для сравнения
    for t in l: # Для каждой строки t в списке l
        print(s, t, compare(s, t)) # Вывод строк и результата сравнения
