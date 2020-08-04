from config import settings


def main():
    print('Testando o Dynaconf:')
    print(f'+username: {settings.username}')
    print(f'+database: {settings.database.name}')
    print(f'+password:{settings.password}')



if __name__ == "__main__":
    main()