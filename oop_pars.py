from pars_classe import parser_

user_file = input('Enter the name of the recording file: ')
file_dir = (f'{user_file}.txt')

parser = parser_('https://www.e-katalog.ru', file_dir)
parser.run()
