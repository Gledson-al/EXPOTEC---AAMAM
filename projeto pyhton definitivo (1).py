import mysql.connector
from mysql.connector import Error
from datetime import datetime

from conexao import conectar, fechar_conexao

# =========================
# USUÁRIOS
# =========================

def adicionar_usuario(conexao):

    print("\n=== USUÁRIOS CADASTRADOS ===")
    listar_usuarios(conexao)

    nome_usuario = input("\nDigite o nome do usuário: ").strip()

    if not nome_usuario:
        print("Nome inválido.")
        return

    while True:    
        dt_nasc_usuario = input("Digite a data de nascimento do usuário (YYYY-MM-DD): ")
        try:
            datetime.strptime(dt_nasc_usuario, "%Y-%m-%d")
            break
        except:
            print("Data inválida, por favor inserir uma data válida")

    email_usuario = input("Digite o email do usuário: ").strip()

    if not email_usuario:
        print("Email inválido.")
        return
   
    data_cadastro_usuario = datetime.now().date()
    if not data_cadastro_usuario:
        print("Data inválida")
        return
     
    usuario_ativo = input("Ativo? [S/N]: ").strip().upper()
    usuario_ativo = 1 if usuario_ativo == 'S' else 0
    
    genero_usuario = input("Digite o genero do usuário Masculino ou Feminino: ").strip().capitalize()

    if genero_usuario not in ['Feminino', 'Masculino']:
        print("Genero inválido")
        return
    
    cursor = conexao.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO usuarios
            (nome_usuario, dt_nasc_usuario, email_usuario, data_cadastro_usuario, usuario_ativo, genero_usuario)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (nome_usuario, dt_nasc_usuario, email_usuario, datetime.now().date(), usuario_ativo, genero_usuario))

        conexao.commit()
        print("Usuário cadastrado!")

    except mysql.connector.Error:
        print("Não foi possível cadastrar o usuário.")


def listar_usuarios(conexao):
    cursor = conexao.cursor(dictionary = True)

    cursor.execute("""
    SELECT id_usuario, nome_usuario, dt_nasc_usuario, email_usuario, data_cadastro_usuario, usuario_ativo, genero_usuario
        FROM usuarios
        ORDER BY id_usuario
            """)
    
    usuarios = cursor.fetchall()

    if not usuarios:
        print("Nenhum usuário cadastrado no momento.")
        return
    
    for usuario in usuarios:
       print(
    f"[{usuario['id_usuario']}] "
    f"[{usuario['nome_usuario']}] "
    f"[{usuario['dt_nasc_usuario']}] "
    f"[{usuario['email_usuario']}] "
    f"[{usuario['data_cadastro_usuario']}] "
    f"[Ativo: {usuario['usuario_ativo']}] "
    f"[{usuario['genero_usuario']}]"
)
       

    



def atualizar_usuario(conexao):

    print("\n=== USUÁRIOS CADASTRADOS ===")
    listar_usuarios(conexao)

    id_usuario = input("\nDigite o ID do usuário: ").strip()

    if not id_usuario.isdigit():
        print("ID inválido.")
        return

    novo_nome = input("Novo nome: ").strip()

    if not novo_nome:
        print("Nome inválido.")
        return

    nova_dt_nasc = input("Nova data nascimento (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(nova_dt_nasc, "%Y-%m-%d")
    except:
        print("Data inválida.")
        return

    novo_email = input("Novo email: ").strip()

    if not novo_email:
        print("Email inválido.")
        return
    usuario_ativo = input("O usuário continua ativo? [S/N]").strip().upper()
    usuario_ativo = 1 if usuario_ativo == 'S' else 0
        
    genero_usuario = input("Digite o seu novo genero: [Masculino / Feminino]").strip().capitalize()    
    cursor = conexao.cursor()

    try:

        cursor.execute(
            """
            UPDATE usuarios
            SET nome_usuario = %s,dt_nasc_usuario = %s, email_usuario = %s, usuario_ativo = %s, genero_usuario = %s
            WHERE id_usuario = %s
            """,
            (novo_nome, nova_dt_nasc, novo_email, usuario_ativo, genero_usuario, id_usuario)
        )

        conexao.commit()

        if cursor.rowcount == 0:
            print("Usuário não encontrado.")
        else:
            print("Usuário atualizado com sucesso!")

    except mysql.connector.Error:
        print("Não foi possível atualizar o usuário.")


    


# =========================
# CONTATOS DE EMERGÊNCIA
# =========================

def adicionar_contatoemergencia(conexao):

    print("\n=== CONTATOS DE EMERGÊNCIA ===")
    listar_contatoemergencia(conexao)

    nome = input("\nDigite o nome do contato de emergencia: ").strip()

    if not nome:
        print("Nome inválido.")
        return

    telefone = input("Digite o telefone do contato: ").strip()

    if not telefone:
        print("Telefone inválido.")
        return

    parentesco = input("Digite o parentesco: ").strip()

    if not parentesco:
        print("Parentesco inválido.")
        return
    
    fk_ce_usuario = input("Digite o ID do usuário: ").strip()

    if not fk_ce_usuario.isdigit():
        print("ID do usuário inválido")
        return

    cursor = conexao.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO contato_emergencia (nome_contato, telefone_contato, parentesco, fk_ce_usuario)
            VALUES (%s, %s, %s, %s)
            """,
            (nome, telefone, parentesco, fk_ce_usuario)
        )

        conexao.commit()

        print("Contato de emergência cadastrado com sucesso!")

    except mysql.connector.Error:
        print("Não foi possível cadastrar o contato.") 


   


def listar_contatoemergencia(conexao):

    cursor = conexao.cursor(dictionary=True)

    cursor.execute( """
        SELECT
            ce.id_contato,
            ce.nome_contato,
            ce.telefone_contato,
            ce.parentesco,
            u.nome_usuario,
            u.id_usuario
        FROM contato_emergencia ce
        LEFT JOIN usuarios u 
            ON ce.fk_ce_usuario = u.id_usuario
        ORDER BY ce.id_contato
    """)

    contatos = cursor.fetchall()
    

    if not contatos:
            print("Nenhum contato de emergência cadastrado no momento.")
            return
    for contato in contatos:
        print(f"[{contato['id_contato']}] "
            f"[{contato['nome_contato']}] "
            f"[{contato['telefone_contato']}] - "
            f"Parentesco: [{contato['parentesco']}] "
            f"Usuário: [{contato['nome_usuario']}] "
            f"(ID: {contato['id_usuario']})"
        )

    

   


def atualizar_contatoemergencia(conexao):

    print("\n=== CONTATOS DE EMERGÊNCIA ===")
    listar_contatoemergencia(conexao)

    id_contato = input("\nDigite o ID do contato: ").strip()

    if not id_contato.isdigit():
        print("ID inválido.")
        return

    novo_nome = input("Novo nome do contato: ").strip()

    if not novo_nome:
        print("Nome inválido.")
        return

    novo_telefone = input("Novo telefone: ").strip()

    if not novo_telefone:
        print("Telefone inválido.")
        return

    novo_parentesco = input("Novo parentesco: ").strip()

    if not novo_parentesco:
        print("Parentesco inválido.")
        return

    cursor = conexao.cursor()

    try:

        cursor.execute(
            """
            UPDATE contato_emergencia
            SET 
                nome_contato = %s,
                telefone_contato = %s,
                parentesco = %s
            WHERE id_contato = %s
            """,
            (novo_nome, novo_telefone, novo_parentesco, id_contato)
        )

        conexao.commit()

        if cursor.rowcount == 0:
            print("Contato não encontrado.")
        else:
            print("Contato atualizado com sucesso!")

    except mysql.connector.Error:
        print("Não foi possível atualizar o contato.")   




def excluir_contatoemergencia(conexao, id_contato):

    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM contato_emergencia WHERE id_contato = %s", (id_contato,))
    
    conexao.commit()
    print(f"Contato de emergência com ID {id_contato} excluído com sucesso.")


    



# =========================
# REMÉDIOS
# =========================


def adicionar_remedio(conexao):

    print("\n=== Rémedios Cadastrados ===")
    listar_remedio(conexao)

    nome_remedio = input("\nDigite o nome do remédio que deseja adicionar: ").strip().capitalize()

    if not nome_remedio:
        print("Nome do remédio inválido.")
        return

    descricao = input("Descrição do remédio: ").strip()
    if not descricao:
        print("descrição inválida")
        return
 
    dosagem = input("Digite a dosagem: ").strip()
    if not dosagem:
        print("Dosagem inválida.")
        return

    horario = input("Digite o horário para tomar o remédio (HH:MM:SS): ").strip()
    if not horario:
        print("Horário inválido.")
        return
    
    tipo_remedio = input("Digite o tipo do remédio: ").strip()

    if not tipo_remedio:
        print("Tipo inválido.")
        return


    cursor = conexao.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO remedios (nome_remedio, descricao_remedio, dosagem_remedio, horario_remedio, tipo_remedio)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (nome_remedio, descricao, dosagem, horario, tipo_remedio)
        )

        conexao.commit()
        print("Remédio cadastrado com sucesso!")

    except mysql.connector.Error:
        print("Não foi possível cadastrar o remédio: ")



def listar_remedio(conexao):

    cursor = conexao.cursor(dictionary = True)

    cursor.execute("""SELECT id_remedio, nome_remedio, descricao_remedio, dosagem_remedio, horario_remedio, tipo_remedio FROM remedios ORDER BY id_remedio""")

    remedios = cursor.fetchall()


    if not remedios:
        print("Nenhum remédio cadastrado no momento.")
        return
    for remedio in remedios:
        print(
            f"[{remedio['id_remedio']}] "
            f"[{remedio['nome_remedio']}] "
            f"[{remedio['descricao_remedio']}] "
            f"[{remedio['dosagem_remedio']}] "
            f"[{remedio['horario_remedio']}]"
            f"[{remedio['tipo_remedio']}]"
        )

    



def atualizar_remedio(conexao):

    print("\n=== REMÉDIOS CADASTRADOS ===")
    listar_remedio(conexao)

    id_remedio = input("\nDigite o ID do remédio: ").strip()

    if not id_remedio.isdigit():
        print("ID inválido.")
        return

    novo_nome = input("Novo nome do remédio: ").strip()

    if not novo_nome:
        print("Nome inválido.")
        return

    nova_dosagem = input("Nova dosagem: ").strip()

    if not nova_dosagem:
        print("Dosagem inválida.")
        return

    novo_horario = input("Novo horário (HH:MM:SS): ").strip()

    if not novo_horario:
        print("Horário inválido.")
        return
    
    novo_tipo = input("Novo tipo do remédio: ").strip()

    if not novo_tipo:
        print("Tipo inválido.")
        return

    cursor = conexao.cursor()

    try:

        cursor.execute(
            """
            UPDATE remedios
            SET nome_remedio = %s,
                dosagem_remedio = %s,
                horario_remedio = %s,
                tipo_remedio = %s
            WHERE id_remedio = %s
            """,
            (novo_nome, nova_dosagem, novo_horario,novo_tipo, id_remedio)
        )

        conexao.commit()

        if cursor.rowcount == 0:
            print("Remédio não encontrado.")
        else:
            print("Remédio atualizado com sucesso!")

    except mysql.connector.Error:
        print("Não foi possível atualizar o remédio.")




def excluir_remedio(conexao, id_remedio):

    cursor = conexao.cursor()
    
    try:
        cursor.execute("""SELECT COUNT(*) FROM tratamentos WHERE fk_tratamento_remedios = %s""", (id_remedio,))


        if cursor.fetchone()[0] > 0:
            print("Não é possível excluir o remédio, pois ele está sendo usado em um tratamento")
            return
        
        cursor.execute("""
            DELETE FROM remedios WHERE id_remedio = %s""", (id_remedio,))
        
        conexao.commit()
        print("Remédio excluído com sucesso")
    except mysql.connector.Error:
        print("Erro ao tentar excluir")

    finally:
        cursor.close()    
 

# =========================
# TRATAMENTOS
# =========================

def adicionar_tratamento(conexao):

    print("\n=== TRATAMENTOS CADASTRADOS ===")
    listar_tratamentos(conexao)

    nome_tratamento = input("\nDigite o nome do tratamento: ").strip()

    if not nome_tratamento:
        print("Nome do tratamento inválido.")
        return

    descricao = input("Digite a descrição do tratamento: ").strip()

    if not descricao:
        print("Descrição inválida.")
        return
    
    tipo = input("Digite o tipo do tratamento: ").strip()

    if not tipo:
        print("Tipo inválido.")
        return

    duracao = input("Digite a duração do tratamento: ").strip()

    if not duracao:
        print("Duração inválida.")
        return

    fk_remedio = input("Digite o ID do remédio: ").strip()

    if not fk_remedio.isdigit():
        print("ID do remédio inválido.")
        return

    data_cadastro = datetime.now().date()

    cursor = conexao.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO tratamentos (nome_tratamento, descricao_tratamento, tipo_tratamento, duracao_tratamento, data_cadastro_tratamento, fk_tratamento_remedios)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (nome_tratamento, descricao, tipo, duracao, data_cadastro, fk_remedio)
        )

        conexao.commit()

        print("Tratamento cadastrado com sucesso!")

    except mysql.connector.Error:
        print("Não foi possível cadastrar o tratamento.")





def listar_tratamentos(conexao):

    cursor = conexao.cursor(dictionary = True)
    cursor.execute("""
    SELECT
        tratamentos.id_tratamento, tratamentos.nome_tratamento, tratamentos.tipo_tratamento, tratamentos.descricao_tratamento, tratamentos.duracao_tratamento, remedios.nome_remedio
    FROM tratamentos 
    LEFT JOIN remedios 
        ON tratamentos.fk_tratamento_remedios = remedios.id_remedio
    ORDER BY tratamentos.id_tratamento
""")
    
    tratamentos = cursor.fetchall()


    if not tratamentos:
        print("Nenhum tratamento cadastrado no momento.")
        return
    
    for tratamento in tratamentos:
        print(
            f"[{tratamento['id_tratamento']}] "
            f"[{tratamento['nome_tratamento']}] "
            f"[{tratamento['tipo_tratamento']}] "
            f"[{tratamento['descricao_tratamento']}] "
            f"[{tratamento['duracao_tratamento']}] "
            f"[Remédio: {tratamento['nome_remedio']}]"
        ) 






def atualizar_tratamento(conexao):

    print("\n=== TRATAMENTOS CADASTRADOS ===")
    listar_tratamentos(conexao)

    id_tratamento = input("\nDigite o ID do tratamento: ").strip()

    if not id_tratamento.isdigit():
        print("ID inválido.")
        return

    novo_nome = input("Novo nome do tratamento: ").strip()

    if not novo_nome:
        print("Nome inválido.")
        return

    nova_descricao = input("Nova descrição: ").strip()

    if not nova_descricao:
        print("Descrição inválida.")
        return

    novo_tipo = input("Novo tipo: ").strip()

    if not novo_tipo:
        print("Tipo inválido.")
        return

    nova_duracao = input("Nova duração: ").strip()

    if not nova_duracao:
        print("Duração inválida.")
        return

    novo_fk_remedio = input("Novo ID do remédio: ").strip()

    if not novo_fk_remedio.isdigit():
        print("ID do remédio inválido.")
        return
    
    cursor = conexao.cursor()

    try:

        cursor.execute(
            """
            UPDATE tratamentos
            SET nome_tratamento = %s,
                descricao_tratamento = %s,
                tipo_tratamento = %s,
                duracao_tratamento = %s,
                fk_tratamento_remedios = %s
            WHERE id_tratamento = %s
            """,
            (novo_nome, nova_descricao, novo_tipo, nova_duracao, novo_fk_remedio, id_tratamento)
        )

        conexao.commit()

        if cursor.rowcount == 0:
            print("Tratamento não encontrado.")
        else:
            print("Tratamento atualizado com sucesso!")

    except mysql.connector.Error:
        print("Não foi possível atualizar o tratamento.")


 

def excluir_tratamento(conexao, id_tratamento):
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM tratamentos WHERE id_tratamento = %s", (id_tratamento,))

    conexao.commit()
    
    print(f"Tratamento com ID {id_tratamento} excluído com sucesso.")






# =========================
# CONEXÃO
# =========================

conexao = conectar()

if conexao is None:
    print('Erro ao conectar com o banco de dados.')
    exit()


# =========================
# MENU PRINCIPAL
# =========================

try:
    while True:

        print('\n===== MENU PRINCIPAL =====')
        print('1 - Listar')
        print('2 - Adicionar')
        print('3 - Atualizar')
        print('4 - Excluir')
        print('5 - Sair')

        opcao = input('\nEscolha uma opção: ')

        # =========================
        # LISTAR
        # =========================
        if opcao == '1':

            print('\n===== LISTAR =====')
            print('1 - Usuários')
            print('2 - Remédios')
            print('3 - Tratamentos')
            print('4 - Contatos de Emergência')
            print('0 - Voltar ao menu principal')

            escolha = input('\nEscolha uma opção: ')

            if escolha == '1':
                listar_usuarios(conexao)

            elif escolha == '2':
                listar_remedio(conexao)

            elif escolha == '3':
                listar_tratamentos(conexao)

            elif escolha == '4':
                listar_contatoemergencia(conexao)

            elif escolha == '0':
                continue

            else:
                print('Opção inválida.')

        # =========================
        # ADICIONAR
        # =========================
        elif opcao == '2':

            print('\n===== ADICIONAR =====')
            print('1 - Usuários')
            print('2 - Remédios')
            print('3 - Tratamentos')
            print('4 - Contatos de Emergência')
            print('0 - Voltar ao menu principal')

            escolha = input('\nEscolha uma opção: ')

            if escolha == '1':
                adicionar_usuario(conexao)

            elif escolha == '2':
                adicionar_remedio(conexao)

            elif escolha == '3':
                adicionar_tratamento(conexao)

            elif escolha == '4':
                adicionar_contatoemergencia(conexao)

            elif escolha == '0':
                continue

            else:
                print('Opção inválida.')

        # =========================
        # ATUALIZAR
        # =========================
        elif opcao == '3':

            print('\n===== ATUALIZAR =====')
            print('1 - Usuários')
            print('2 - Remédios')
            print('3 - Tratamentos')
            print('4 - Contatos de Emergência')
            print('0 - Voltar ao menu principal')

            escolha = input('\nEscolha uma opção: ')

            if escolha == '1':
                atualizar_usuario(conexao)

            elif escolha == '2':
                atualizar_remedio(conexao)

            elif escolha == '3':
                atualizar_tratamento(conexao)

            elif escolha == '4':
                atualizar_contatoemergencia(conexao)

            elif escolha == '0':
                continue

            else:
                print('Opção inválida.')

        # =========================
        # EXCLUIR
        # =========================
        elif opcao == '4':

            print('\n===== EXCLUIR =====')
            print('1 - Usuários')
            print('2 - Remédios')
            print('3 - Tratamentos')
            print('4 - Contatos de Emergência')
            print('0 - Voltar ao menu principal')

            escolha = input('\nEscolha uma opção: ')

            if escolha == '1':
                print("Ainda não implementado delete de usuário.")

            elif escolha == '2':
                id_remedio = input("ID do remédio: ")
                excluir_remedio(conexao, id_remedio)

            elif escolha == '3':
                id_tratamento = input("ID do tratamento: ")
                excluir_tratamento(conexao, id_tratamento)

            elif escolha == '4':
                id_contato = input("ID do contato: ")
                excluir_contatoemergencia(conexao, id_contato)

            elif escolha == '0':
                continue

            else:
                print('Opção inválida.')

        # =========================
        # SAIR
        # =========================
        elif opcao == '5':
            print("Encerrando sistema...")
            fechar_conexao(conexao)
            break

        else:
            print("Opção inválida.")

        input('\nPressione ENTER para continuar...')

except Exception as e:
    print(f"Erro inesperado: {e}")
    fechar_conexao(conexao)