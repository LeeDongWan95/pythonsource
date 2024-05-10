# %%
# 들여쓰기 주의하기
if True:
    print("True")
# %%
a = 200
# a가 100 보다 크고 200 보다 작거나 같은지 확인
if a > 100 and a <= 200:
    print("a 는 100 보다 크고 200 보다 작거나 같다")

# %%
if 100 < a <= 200:
    print("a 는 100 보다 크고 200 보다 작거나 같다")

# %%
# 세 개의 숫자 중 가장 큰 수 출력
a, b, c = 12, 6, 18
max = a
if max < b:
    max = b
if max < c:
    max = c
print("a, b, c 중 가장큰 수는 {}".format(max))

# %%
if True:
    print("True")
else:
    print("False")
# %%
score, grade = 90, "A"
# score 가  90 이상이고 grade 가 A 이면 합격 아니면 불합격
if score >= 90 and grade == "A":
    print("합격")
else:
    print("불합격")

# %%
# 숫자를 입력 받은 후 짝/홀 출력
num = int(input("숫자입력"))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")
# %%
# 중첩 if
a = 75
if a > 50:
    if a < 100:
        print("50 보다 크고 100보다 작다")
    else:
        print("100 보다 크다")
else:
    print("50 보다 작다")


# %%
# 다중 if ==> switch(X)
# else if(X) ==> elif
num = 79
if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("F")
# %%
# age, height 입력받은 후
# age >= 20 이고 height >= 170 : A 지망 지원가능
# age >= 20 이고 height >= 160 : B 지망 지원가능
# age >= 20 이고 height < 160 : 지원불가
# age < 20 : 20세 이상 지원 가능
age = int(input("나이 입력"))
height = int(input("키 입력"))
# if age >= 20 and height >= 170:
#     print("A 지망 지원가능")
# elif age >= 20 and height >= 160:
#     print("B 지망 지원가능")
# elif age >= 20 and height < 160:
#     print("지원 불가")
# if age < 20:
#     print("20 세 이상 지원 가능")
if age >= 20:
    if height >= 170:
        print("A 지망 지원 가능")
    elif height >= 160:
        print("B 지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")


# %%
# 점수 입력 받은 후
# 81 ~ 100 : A학점
# 61 ~ 80 : B학점
# 41 ~ 60 : C학점
# 21 ~ 40 : D학점
# 0 ~ 20 : E학점
grade = int(input("점수 입력"))
# if 81 <= grade <= 100:
#     print("A 학점")
# elif 61 <= grade <= 80:
#     print("B 학점")
# elif 41 <= grade <= 60:
#     print("C 학점")
# elif 21 <= grade <= 40:
#     print("D 학점")
# elif 0 <= grade <= 20:
#     print("E 학점")
if grade > 80:
    print("A학점")
elif grade > 60:
    print("B학점")
elif grade > 40:
    print("C학점")
elif grade > 20:
    print("D학점")
else:
    print("E학점")
# %%
# 두 개의 숫자 입력받기, 연산자(+,-,*,/,//,**,%) 입력받기
# 연산 후 결과 출력 ( 5 + 3 = 8)
num1 = int(input("숫자1"))
num2 = int(input("숫자2"))
operator = input("연산자입력")
# if operator == "+":
#     print(f"{num1} {operator} {num2} =", num1 + num2)
# elif operator == "-":
#     print(f"{num1} {operator} {num2} =", num1 - num2)
# elif operator == "*":
#     print(f"{num1} {operator} {num2} =", num1 * num2)
# elif operator == "/":
#     print(f"{num1} {operator} {num2} =", num1 / num2)
# elif operator == "//":
#     print(f"{num1} {operator} {num2} =", num1 // num2)
# elif operator == "**":
#     print(f"{num1} {operator} {num2} =", num1 ** num2)
# elif operator == "%":
#     print(f"{num1} {operator} {num2} =", num1 % num2)
result = None
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    print(f"{num1} {operator} {num2} =", num1 * num2)
elif operator == "/":
    print(f"{num1} {operator} {num2} =", num1 / num2)
elif operator == "//":
    print(f"{num1} {operator} {num2} =", num1 // num2)
elif operator == "**":
    print(f"{num1} {operator} {num2} =", num1**num2)
elif operator == "%":
    print(f"{num1} {operator} {num2} =", num1 % num2)

# %%
