# Song_Rating
- Uma API que o usuario logado poderá avaliar uma ou várias músicas com uma nota e um comentário. As músicas avaliadas tem Albuns, e esses Albuns são gravados por um Artista/Banda. 
Projeto da Disciplina de Programação para Internet II - IFPI.

### Requisitos
* Python 3.8.2;
* Django 3.1.4;
* Django Rest Framework 3.12.2;
* Django Filter 2.4.0;
* Django Rest Framework Simple JWT 4.6.0.

#### Bibliotecas
```
  python -m pip install Django
  pip install djangorestframework
  pip install django-filter
  pip install djangorestframework-simplejwt
```

| url                         | Funcionalidade                                                       |
|-----------------------------|----------------------------------------------------------------------|
| server/artists            | Listagem e cadastro de Artistas                                      |
| server/artist/1           | Informações de um artista                                            |
| server/albums             | Listagem e cadastro de albuns.                                       |
| server/album/1            | Informações de um album especifico                                   |
| server/songs              | Listagem e cadastro de musicas                                       |
| server/song/1             | Informações de uma musica especifica                                 |
| server/profile-list       | Listagem e cadastro de perfis                                        |
| server/profile-list/1     | Informações de um perfil específico                                  |
| server/ratings            | Listagem e cadastro de avaliação das musicas.                        |
| server/ratings/1          | Informações de uma avaliação especifica de uma musica.               |
| server/api/token/         | Login com token JWT (JSON Web Token)                                 |
| server/api/token/refresh/ | Atualização do token JWT                                             |
| server/swagger/ 	        | Documentação da API                                                  |

### Permissões:
Somente o superusuário tem permissão para cadastrar artistas, albums e musicas. Um usuário Normal cadastrado pode fazer avaliações nas músicas que ele deseja. Quem não for usuário pode apenas visualizar. 

### Paginação:
* songs?name= field
* user?search= field
* user?ordering= field
  
### Throttling:
*  Quem não é usuário da api só tem permissão de acesso aos endpoints no maximo 2 vezes por hora. 
*  Quem é usuário da api(usuario normal e Superusuário) só tem permissão de acesso aos endpoints no maximo 10 vezes por hora.
  
### [Vídeo-Youtube] https://www.youtube.com/watch?v=nLctkyZ9QUE
