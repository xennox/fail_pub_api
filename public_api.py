from goodreads import client
import goodreads_api_client as gr
import colorama # Чтобы было прикольней и весело
from goodreads import client
import googletrans
import goodreads_api_client as gr

from db_con import *
from colorama import Fore
colorama.init()

client = gr.Client(developer_key='Y6KLU6ejpge4GENfZw1Z8w')

def Get_Info(data):
    list_translate=select(f"select name from books where id={data['id']}")
    for name_book in list_translate:
        return {**data, **{'Ru_name':name_book[0]}}

print(Fore.BLUE)
book_input = int(input("Введи айди: "))
book = client.Book.show(book_input)
keys_wanted = ['id', 'title', 'isbn']
reduced_book = {k:v for k, v in book.items() if k in keys_wanted}
reduced_rus_book = (Get_Info(reduced_book))


print(Fore.RED + reduced_book['title'] + Fore.GREEN + '\n' + 'Локализация: ' + reduced_rus_book['Ru_name'])
