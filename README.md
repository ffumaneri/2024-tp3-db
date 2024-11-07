# 2024-tp3-db

Completar ejercicio1 y ejercicio2

## Como correr el ejemplo

* Instalar las librerías:

```
pip install -r requirements.txt
```

* Correr PostgreSQL. Se puede instalar el PostgreSQL o usar docker

  ```
  docker run --name tp3-db \
      -e POSTGRES_PASSWORD=dbpassword \
      -e POSTGRES_USER=dbuser \
      -e POSTGRES_DB=tp3-db \
      -p 5433:5432 \
      -d postgres
  ```
* Setear en `common.py` el string de conexión. `engine = create_engine('postgresql://dbuser:dbpassword@localhost:5432/tp3-db')`
* Correr el código

```
python -m ejemplo
```

## Ejercicio 1

Completar el código que está comentado en `jefe.py` y `oficina.py`

Es una relación 1 a 1. Quiere decir que la oficina tiene un ID de *jefe*. Y el *jefe* tiene una relación hacia *oficina*.

Usar la función [relationship](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-one) de *sqlalchemy* en la clase *Jefe*

Para ejecutar el ejercicio correr `python -m ejercicio1`

## Ejercicio 2

Completar el código que está comentado en `alumno.py` y `aula.py`. En `__main__.py` hay que hacer el query para traer todos los alumnos con sus aulas.

Usar la función [relationship](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-many) de *sqlalchemy* en la clase *Aula* ya que un aula tiene muchos (many) alumnos.

Para ejecutar el ejercicio correr `python -m ejercicio2`