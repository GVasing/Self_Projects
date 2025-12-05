# import psycopg2
# from config import Config
# from psycopg2.extras import RealDictCursor

# def get_db_connection():
#     try:
#         conn = psycopg2.connect(
#             host=Config.DB_HOST,
#             port=Config.DB_PORT,
#             database=Config.DB_NAME,
#             user=Config.DB_USER,
#             password=Config.DB_PASSWORD
#         )
#         return conn
#     except psycopg2.Error as err:
#         print(f"Database connection error: {err}")
#         return None