from tasks import cpu_bound_function
from datetime import datetime


def main():
    print(cpu_bound_function)
    async_result_1 = cpu_bound_function.delay(4, 1)
    async_result_2 = cpu_bound_function.delay(2, 21)



    result_1 = async_result_1.get()
    result_2 = async_result_2.get()


    print(result_1)
    print(result_2)




start = datetime.now()
main()
print(datetime.now() - start)
