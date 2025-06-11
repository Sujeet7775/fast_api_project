import asyncpg
import asyncio

async def fetch_all_tables():
    conn = await asyncpg.connect(
        user='postgres',
        password='root',
        database='master_db',
        host='localhost',
        port=5433
    )
    
    rows = await conn.fetch("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
          AND table_type = 'BASE TABLE';
    """)
    
    await conn.close()
    return [row['table_name'] for row in rows]

if __name__ == "__main__":
    tables = asyncio.run(fetch_all_tables())
    print("All Tables:", tables)
