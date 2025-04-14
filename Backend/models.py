from sqlalchemy import *
import hashlib

engine = create_engine("sqlite:///mia.db", echo=False)
metadata_obj = MetaData()


table_etudiant = Table("Etudiant", metadata_obj,
                       Column("numeroEtudiant", Integer, primary_key=True),
                       Column("nom", String(100), nullable=False),
                       Column("prenom", String(100), nullable=False),
                       Column("dateDeNaissance", DateTime, nullable=False),
                       Column("motDePasse", String(64), nullable=False),
                       Column("classe", String(100), nullable=True))

table_admin = Table("Admin", metadata_obj, Column("clef", String(64), primary_key=True))


# à n'appeler qu'une seule fois, si mia.db n'existe pas !
def init_db():
    metadata_obj.create_all(engine)

def get_mdp_from_etudiant(numEtudiant):
    stmt = select(table_etudiant.c.motDePasse).where(
        table_etudiant.c.numeroEtudiant == int(numEtudiant))
    with engine.connect() as conn:
        result = conn.execute(stmt)
        row = result.fetchone()  # <- DOIT être dans le `with`
    if row is not None:
        return row[0]
    else:
        return None



def get_clefs_from_admin():
    stmt = select(table_admin.c.clef)
    with engine.connect() as conn:
        result = conn.execute(stmt)
    conn.close()
    return result.fetchall()


def create_new_etudiant(numEtudiant, nom, prenom, dateDeNaissance, motDePasse, classe):
    try:
        mdpHashe = hashlib.sha256(motDePasse.encode()).hexdigest()
        stmt = insert(table_etudiant).values(
            numeroEtudiant=numEtudiant
            ,nom=nom
            ,prenom=prenom
            ,dateDeNaissance=dateDeNaissance
            ,motDePasse=mdpHashe
            ,classe=classe
            )

        with engine.begin() as conn:
            conn.execute(stmt)
        return True
    except Exception as e:    
        return False
    conn.close()


def create_new_clef_admin(clef):
    clefHashee = hashlib.sha256(clef.encode()).hexdigest()
    stmt = insert(table_admin).values(clef=clefHashee)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


def update_mdp_etudiant(numEtudiant, nouveauMdp):
    nouveauMdpHashe = hashlib.sha256(nouveauMdp.encode()).hexdigest()
    stmt = update(table_etudiant).where(
        table_etudiant.c.numeroEtudiant == numEtudiant).values(motDePasse=nouveauMdpHashe)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
    conn.close()


def delete_etudiant(numEtudiant):
    if get_mdp_from_etudiant(numEtudiant):
        stmt = delete(table_etudiant).where(
            table_etudiant.c.numeroEtudiant == numEtudiant)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        conn.close()

def get_all_etudiants():
    stmt = select(table_etudiant)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        rows = result.fetchall()
    conn.close()
    return rows

def get_etudiant_by_id(numEtudiant):
    stmt = select(table_etudiant).where(table_etudiant.c.numeroEtudiant == numEtudiant)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        row = result.fetchone()
    conn.close()
    return row

    
def get_all_admins():
    stmt = select(table_admin)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        rows = result.fetchall()
    conn.close()
    return rows

# fonction qui trouve l'id du dernier étudiant et l'icremente par 1
def get_next_etudiant_id():
    stmt = select(table_etudiant.c.numeroEtudiant).order_by(table_etudiant.c.numeroEtudiant.desc()).limit(1)
    with engine.connect() as conn:
        result = conn.execute(stmt).fetchone()
    if result is None:
        return 1
    return result[0] + 1

# fonction qui modifie le password de l'étudiant
def update_password_etudiant(etudiant_id, new_password_hash):
    try:
        stmt = (
            update(table_etudiant)
            .where(table_etudiant.c.numeroEtudiant == etudiant_id)
            .values(motDePasse=new_password_hash)
        )
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        return True
    except Exception as e:
        print("Erreur update_password_etudiant:", e)
        return False