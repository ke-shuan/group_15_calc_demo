import math
import re  # 用於處理百分比符號

# 定義可用函數
def custom_function(x):
    return x ** 2 + 2 * x + 1

allowed_functions = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'log': math.log,
    'pi': math.pi,
    'e': math.e,
    'custom_function': custom_function
}

# 預處理函數：將百分比轉換為具體的數值
def preprocess_expression(expression):
    # 將 "數字%" 替換為 "(數字/100)"
    expression = re.sub(r'(\d+)%', r'(\1 / 100)', expression)
    return expression

# 輸入數學算式
math_expression = input("請輸入數學算式（例如：100 * 10%）: ")

# 預處理輸入
math_expression = preprocess_expression(math_expression)

# 安全地計算數學式
try:
    # 使用 eval 並限制在 allowed_functions
    result = eval(math_expression, {"__builtins__": None}, allowed_functions)
    print(f"計算結果是: {result}")
except Exception as e:
    print(f"發生錯誤: {e}")
