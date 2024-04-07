import client
import models

def read():
    try:
        conn = client.db_client()
        cur = conn.cursor()
        cur.execute(f"select * from public.product")
        prod = cur.fetchone()
        data = {"status": 1, "data": prod}
        
    except Exception as e:
        data = {"status": -1, "error": f'{e}'}
        
    finally:
        conn.close()
        
    return data



def readId(id:int):
    try:
        conn = client.db_client()
        cur = conn.cursor()
        cur.execute(f"select * from public.product where product_id={id}")
        prod = cur.fetchone()
        data = {"status": 1, "data": prod}
        
    except Exception as e:
        data = {"status": -1, "error": f'{e}'}
        
    finally:
        conn.close()
        
    return data

def createproduct(product:models.PostProduct):
    try:
        conn = client.db_client()
        cur = conn.cursor()

        query = """INSERT INTO public.product (
                        product_id, name, company, price, units, subcategory_id, created_at, updated_at
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

        values = (
            product.product_id, 
            product.name, 
            product.company, 
            product.price, 
            product.units, 
            product.subcategory_id, 
            product.created_at, 
            product.updated_at
        )

        cur.execute(query, values)
        conn.commit()
        data = {"status": 1, "message": "Producto agregado correctamente"}
    except Exception as e:
        data = {"status": -1, "error": str(e)}
    finally:
        if conn:
            conn.close()
    return data

def updateProducts(product_id: int, product: models.PostProduct):
    try:
        conn = client.db_client()
        cur = conn.cursor()
        query = f"""UPDATE public.product 
                    SET 
                        name = '{product.name}', 
                        company = '{product.company}', 
                        price = {product.price}, 
                        units = {product.units}, 
                        subcategory_id = {product.subcategory_id}, 
                        created_at = '{product.created_at}', 
                        updated_at = '{product.updated_at}'
                    WHERE
                        product_id = {product_id};""" 
        cur.execute(query)
        conn.commit()
        data = {"status": 1, "message": "S’ha modificat correctement"}
    except Exception as e:
        data = {"status": -1, "error": str(e)}
    finally:
        conn.close()
        return data



        
