from ldap3 import Server, Connection, SIMPLE, SYNC, ASYNC, SUBTREE, ALL

# домен - example.com
# DNS имя сервера Active Directory
AD_SERVER = 'corp.ertelecom.loc'
# Пользователь (логин) в Active Directory - нужно указать логин в AD
# в формате 'CORP\aduser' или 'aduser@ertelecom.loc'
domen = str('@corp.ertelecom.loc')
login = input('Введите логин: ')
AD_USER = (login+domen)
print(AD_USER)
AD_PASSWORD = input('Введите пароль: ')
AD_SEARCH_TREE = 'dc=corp,dc=ertelecom,dc=loc'

server = Server(AD_SERVER)
conn = Connection(server,user=AD_USER,password=AD_PASSWORD)
conn.bind()
print(conn)


# в ответ должно быть - True

# Поиск в Active Directory
# примеры ldap фильтров можно посмотреть здесь -
# https://social.technet.microsoft.com/wiki/contents/articles/8077.active-directory-ldap-ru-ru.aspx
# Я в нижеследующем фильтре:
# - исключаю всеx отключенных пользователей (!(UserAccountControl:1.2.840.113556.1.4.803:=2))
# - добавляю только тех пользователей у которых заполнено имя и фамилия
# - и вывожу атрибуты - attributes
# Все возможные атрибуты Active Directory можно посмотреть здесь -
# https://msdn.microsoft.com/en-us/library/ms675090%28v=vs.85%29.aspx
#a = input("Введи логин для поиска: ")
conn.search('dc=corp,dc=ertelecom,dc=loc,ou=uk,ou=users', '(objectclass=person)', attributes=['sn','givenName'])

# после этого запроса в ответ должно быть - True

# можно посмотреть на результат
print(conn.entries)
# или вывести только Common-Name - cn
#for entry in conn.entries:
 #   print(entry.cn)

# Найти пользователя с логином admin (sAMAccountName=admin) и показать информацию по нему
#slogin = input("введите логин для поиска: ")

#conn.search(AD_SEARCH_TREE,'(sAMAccountName=805306368)', SUBTREE,
 #  attributes =['cn','sAMAccountName','gn']
  #  )
#conn.entries