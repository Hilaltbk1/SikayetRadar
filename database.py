from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlmodel import SQLModel

DATABASE_URL = "mysql+aiomysql://root:hellohilal123@127.0.0.1:3306/mydatabase1"

# Asenkron motor
engine = create_async_engine(DATABASE_URL, echo=True)

# Asenkron session yaratmak için sessionmaker
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False, future=True
)

Base = declarative_base()

async def init_db():
    try:
        # Veritabanı bağlantısı kurulabilir, tablolar yaratılabilir.
        async with engine.begin() as conn:
            # Eğer SQLModel kullanıyorsanız, aşağıdaki satırı güncelledim:
            await conn.run_sync(SQLModel.metadata.create_all)
        print("Veritabanı bağlantısı başarıyla kuruldu.")
    except Exception as e:
        print(f"Veritabanı bağlantısı hatası: {e}")

async def close_db():
    await engine.dispose()
    print("Veritabanı bağlantısı başarıyla kapatıldı.")
