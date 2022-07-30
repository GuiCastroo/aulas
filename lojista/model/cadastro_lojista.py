import uuid

lista_lojista = []


def cadastro(name, email, cpf):
    #todo enriquecer informações no lojista,e validações se pode ou não operar conosco.
    novo_lojista = {
        "id": str(uuid.uuid4()),
        "name": name,
        "email": email,
        "cpf": cpf
    }
    lista_lojista.append(novo_lojista)
    return novo_lojista


def get_lojista(email):
    if not lista_lojista:
        result = 'nao existe lojista ainda, por favor cadastra seu usuário'
        return result
    result = None
    for cadastro_unico in lista_lojista:
        #TODO AJUSTAR ESSA LINHA DE CÓDIGO USANDO list comprehension
        print(f'testando o seguinte user: {cadastro_unico}')
        if cadastro_unico["email"] == email:
            print(cadastro_unico)
            result = cadastro_unico
        else:
            result = 'Não existe lojista com este id'
    return result


def update_lojista():
    # TODO
    pass
