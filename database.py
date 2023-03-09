from sqlalchemy import create_engine, text
from keyss import connection_string


engine = create_engine(connection_string,
                       connect_args={
                            "ssl": {
                                "ssl_ca": "/etc/ssl/cert.pem"
                            }
                       })

with engine.connect() as conn:
    result = conn.execute(text("Select * from computadoras"))

    # d, a = {}, []

    # for row in result:
    #     for column, value in row.items():
    #         d = {**d, **{column: value}}
    #     a.append(d)

    # print(a)

    # data = [dict(row) for row in result]
    # print(data)
    data = [dict(data._mapping) for data in result]
    print(data)
    # result_all = result.all()
    # first_result = result_all[0]
    # first_result_dict = first_result
    # print(result_all)
    # print(first_result_dict)