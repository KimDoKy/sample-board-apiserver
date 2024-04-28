# sample board api server

```bash
# get board list
## method: GET
/boards/

# create post
## method: POST
/boards/

json
title: string
content: string

# detail post
## method: GET
/boards/<pk>/

# update post
## method: PUT
/boards/<pk>/

json
title: string
content: string

# delete post
### method: Delete
/boards/<pk>/
```

migration은 파일은 걍 모두 추가해두었고,
SQL은 sqlite로 되어 있음

그냥 8000번 포트로 docker로 실행하면 됨

```bash
# build docker imagee
$ docker build -t board-api-server .

# run server
$ docker run -p 8000:8000 board-api-server
```
