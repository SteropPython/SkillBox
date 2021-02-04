#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть зашифрованное сообщение

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

# ключ к расшифровке:
#   первое слово - 4-я буква
#   второе слово - буквы с 10 по 13, включительно
#   третье слово - буквы с 6 по 15, включительно, через одну
#   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
#   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
#
# Требуется задать конкретные индексы, например secret_message[3][12:23:4]
# Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат

# TODO вывести расшифрованное сообщение

firstString = ''.join([i for i in secret_message[0] if not i.isdigit()])
secondString = ''.join([i for i in secret_message[1] if not i.isdigit()])
thirdString = ''.join([i for i in secret_message[2] if not i.isdigit()])
fourthString = ''.join([i for i in secret_message[3] if not i.isdigit()])
fifthString = ''.join([i for i in secret_message[4] if not i.isdigit()])

print(firstString[3],
      secondString[9:13],
      thirdString[5:15:2],
      fourthString[-len(fourthString) + 12:-len(fourthString) + 6: -1],
      fifthString[-len(fifthString) + 20:-len(fifthString) + 15: -1])
