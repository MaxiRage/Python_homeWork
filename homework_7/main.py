from calc import Calc_block as calc
from logger import result_logger as write_log
import transform as transform
import console as console

j = transform.data_formatting(console.input_data())
calc_result = calc(j)
console.view_data(calc_result, 'Ответ')
write_log(j, calc_result)
