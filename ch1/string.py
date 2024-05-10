# %%
# 문자 처리
# 문자, 문자열 구분 안함 - 쌍따옴표, 홀따옴표 허용, 3개
# 'Life is too short, You need Python'
# "Life is too short, You need Python"
# '''Life is too short, You need Python'''
# """Life is too short, You need Python"""

multiline = """
    Life is too short
    You need Python
"""
multiline

# %%
# + : 문자열 결합
str1 = "Python" + " is fun"
str1

# %%
# * : 문자열 반복
"Python" * 2
# %%
print("=" * 50)
print("My Program")
print("=" * 50)

# %%
# 문자열 인덱싱과 슬라이싱
# Python is fun
print(str1[3])
print(str1[5])
print(str1[-1])  # 오른쪽에서 인덱싱
# %%
# 슬라이싱 [시작위치:끝 위치] => 끝 위치 포함 안함
str1 = "Life is too short"
print(str1[0:])
print(str1[0:4])
print(str1[4:])
print(str1[4:8])
print(str1[:17])
print(str1[0:-4])

# %%
# len() : 길이
len(str1)
# %%
str2 = "20240510Sunny"
# 년월일 출력 : 20240510
# 날씨 출력 : Sunny
print(str2[0:8])
print(str2[8:])
# %%
# 년월일 출력 : 2024-05-10
print(str2[0:4] + "-" + str2[4:6] + "-" + str2[6:8])
# %%
jumin = "901205-3234567"
# 주민등록번호에서 1 or 3 남자, 2 or 4 여자
no = int(jumin[7])

if no == 1 or no == 3:
    print("남자")
else:
    print("여자")


if no % 2 == 1:
    print("남자")
else:
    print("여자")
