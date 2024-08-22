


def valida(func):

    def valida_login():
        rest = func()
        print(rest[0], rest[1])
        return True
        
    return valida_login


@valida
def login():
    email = 'teste@gagaga'
    password = 'form.password.data'
        
    return email, password


print(login())