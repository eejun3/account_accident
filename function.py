from pprint import pprint
import time
from connection.db_connection import execute_query


def split_params(param):
    return param.split(',') if ',' in param else [param]


def process_queries(connection, customer_ids_old, customer_ids_new, user_ids_old, user_ids_new):
    if connection is None:
        return

    for i in range(len(customer_ids_old)):
        # 첫 번째 단계: customer 테이블 조회
        customer_query = "SELECT id,state FROM customer WHERE id IN (%s, %s)"
        customer_params = (customer_ids_old[i], customer_ids_new[i])
        customer_result = execute_query(connection, customer_query, customer_params)

        # Sleep to simulate delay
        time.sleep(1)  # 1초 지연

        # 두 번째 단계: user 테이블 조회
        user_query = "SELECT id,state FROM user WHERE id IN (%s, %s)"
        user_params = (user_ids_old[i], user_ids_new[i])
        user_result = execute_query(connection, user_query, user_params)

        pprint(customer_result)
        pprint(user_result)

        # 결과 검증
        if len(customer_result) == 2 and len(user_result) == 2:
            print(f"Pair {i + 1}: Passed")
        else:
            print(f"Pair {i + 1}: Failed at index {i}")

        # 다음 쿼리 전에 일정 시간 대기
        time.sleep(1)

    return "All queries executed successfully"
