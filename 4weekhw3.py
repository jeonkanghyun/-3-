# -*- coding: utf-8 -*-
"""4weekhw3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eLnO5yYU6l8qF1wooxw2DA37duBHsPkk
"""

score = [] #비어있?는 리스트
a = 0
b = 0

for i in range(10) :
  score.append(int(input())) #score 리스트에다가 10개 점수 입력

while b <= 9 :#b는 리스트의 인덱스
  a = a + score[b] #점수 올리기

  if a == 100 :
    break #점수가 100이되면 그냥 탈출하고 출력
  elif a > 100 :
    #a가 100보다 크면 a값이랑 a-socre[b](그 전까지 더한거)중에서 100과 차이가 작은값 출력
    #두 차이가 같다면 더 큰 값 출력
    if a - 100 <= 100 - (a - score[b]) :
      break
    else :
      a = a - score[b]
    break
  b = b + 1
print(a)