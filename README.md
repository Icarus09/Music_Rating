# music_rating
Uma API que engloba artistas, albuns e musicas, e os usuários cadastrados podem classificar musicas dando uma nota e comentando. Projeto da disciplina de Programação para internet II.

### Requisitos
* [Python 3.8.2](https://www.python.org);
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
| servidor/artists            | Listagem e cadastro de Artistas                                      |
| servidor/artist/1           | Informações de um artista                                            |
| servidor/albums             | Listagem e cadastro de albuns.                                       |
| servidor/album/1            | Informações de um album especifico                                   |
| servidor/songs              | Listagem e cadastro de musicas                                       |
| servidor/song/1             | Informações de uma musica especifica                                 |
| servidor/profile-list       | Listagem e cadastro de perfis                                        |
| servidor/profile-list/1     | Informações de um perfil específico                                  |
| servidor/ratings            | Listagem e cadastro de avaliação das musicas.                        |
| servidor/ratings/1          | Informações de uma avaliação especifica de uma musica.               |
| servidor/api/token/         | Login com token JWT (JSON Web Token)                                 |
| servidor/api/token/refresh/ | Atualização do token JWT                                             |

### Permissões:
Somente o superusuário tem permissão para cadastrar artistas, albums e musicas. Um usuário Normal cadastrado pode fazer avaliações nas músicas que ele deseja. Quem não for usuário pode apenas visualizar. 

### [Vídeo-Youtube] https://www.youtube.com/watch?v=nLctkyZ9QUE
