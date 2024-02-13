import os
import re
os.system('cls')

def generator_numbers(text: str)->str:
    regul=r'\d+.\d+'
    return re.findall(regul,text)

def sum_profit(text: str,func: callable):
    list=func(text)  
    return sum(map(lambda digital: float(digital),list))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.0 доларів."

total_income = sum_profit(text, generator_numbers) 
print(f"Загальний дохід: {total_income}")







# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# print(text,end="\n\n")


# regul='\d+.\d+'
# print(re.findall(regul,text), end='\n\n')


# text1 = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# print(text1.split(),end='\n\n')


# text2 = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# for charworlds in text2.split():
#     if charworlds.isdigit():
#         print(charworlds)
# print("Не працює бо 1000.01 не рахує що це число charworlds.isdigit() != 1000.01  ")
