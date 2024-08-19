# Sistema para controle de Leads


Nesse projeto vc encontrará a criação de usuarios com relacionamento de grupos.
Foi desenvolvido pensando no relacionamento N:N na criação de usuário.

+----------------+     +-----------------+     +----------------+
|     User       |     |   UserGroups    |     |     Group      |
+----------------+     +-----------------+     +----------------+
| id: Integer    |     | id_user: Integer|     | id: Integer    |
| email: String  |     | id_group: Integer|    | name: String   |
| name: String   |     +-----------------+     | note: String   |
| password: String|     |                 |     | status: Integer|
| status: Integer |     +-----------------+     +----------------+
+----------------+                    |
        |                             |
        |                             |
        |                             |
        |                             |
        |                             |
        +-----------------------------+
                   (many-to-many)



## Getting started

instale as dependências em requirements.txt.

rode create_db.py em app para criar o banco de dados.

depois rode o run.py.

