import tkinter as tk
from tkinter import ttk, scrolledtext
from connection.db_connection import create_db_connection
from function import *

# UI 초기화
root = tk.Tk()
root.title("DB Query Generator")

# 실행 창 설명 추가
description = "이 폼을 사용하여 필요한 파라미터를 입력하고 DB 쿼리를 생성하세요."
description_label = ttk.Label(root, text=description, wraplength=400)
description_label.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

# 파라미터 라벨과 입력 필드 (param1과 param3을 한 줄에 배치)
ttk.Label(root, text="old customers :").grid(column=0, row=1, padx=10, pady=10)
param1_entry = ttk.Entry(root)
param1_entry.grid(column=1, row=1, padx=10, pady=10)

ttk.Label(root, text="new customers :").grid(column=2, row=1, padx=10, pady=10)
param3_entry = ttk.Entry(root)
param3_entry.grid(column=3, row=1, padx=10, pady=10)

# 파라미터 라벨과 입력 필드 (param2와 param4를 한 줄에 배치)
ttk.Label(root, text="old users :").grid(column=0, row=2, padx=10, pady=10)
param2_entry = ttk.Entry(root)
param2_entry.grid(column=1, row=2, padx=10, pady=10)

ttk.Label(root, text="new users :").grid(column=2, row=2, padx=10, pady=10)
param4_entry = ttk.Entry(root)
param4_entry.grid(column=3, row=2, padx=10, pady=10)

# 결과를 표시할 Text 위젯 추가 (스크롤 가능)
result_text = scrolledtext.ScrolledText(root, width=40, height=10)
result_text.grid(column=0, row=4, columnspan=4, pady=10)

# 제출 버튼
submit_button = ttk.Button(root, text="Generate Query", command=lambda: generate_query())
submit_button.grid(column=0, row=3, columnspan=4, padx=10, pady=10)

# DB 접속 정보
host = "host"
port = 3306
user = "user"
password = "password!"
database = "database"  # 사용할 데이터베이스 이름을 입력하세요.


# 데이터베이스 에 연결
connection = create_db_connection(host, port, user, password, database)


# 제출 버튼에 이벤트 핸들러 연결 (이전 코드에서 구현한 generate_query 함수를 여기에 연결하세요)
def generate_query():
    # param1 = param1_entry.get()
    # param2 = param2_entry.get()
    # param3 = param3_entry.get()
    # param4 = param4_entry.get()
    param1 = "56539,117375"
    param2 = "38906,103219"
    param3 = "1813202,1881271"
    param4 = "1812917,1881034"

    customer_ids_old = split_params(param1)
    user_ids_old = split_params(param2)
    customer_ids_new = split_params(param3)
    user_ids_new = split_params(param4)

    if not (len(customer_ids_old) == len(user_ids_old) == len(customer_ids_new) == len(user_ids_new)):
        result_text.insert(tk.END, "ids must be in pairs. Please enter same length parameter.")
        return
    else:
        result = process_queries(connection, customer_ids_old, customer_ids_new, user_ids_old, user_ids_new)
    # 이후 단계 에서 DB 조회 및 쿼리문 생성 로직 추가 예정
    # result = execute_query(connection, "SELECT * FROM instructor WHERE id = " + param1)
    # Text 위젯의 현재 내용을 클리어
    result_text.delete('1.0', tk.END)

    # Text 위젯에 결과 텍스트를 삽입
    result_text.insert(tk.END, result)


submit_button.config(command=generate_query)

root.mainloop()
