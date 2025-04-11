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
    conn.close()
    row = result.fetchone()
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
    mdpHashe = hashlib.sha256(motDePasse.encode()).hexdigest()
    stmt = insert(table_etudiant).values(numeroEtudiant=numEtudiant, nom=nom,
                                         prenom=prenom, dateDeNaissance=dateDeNaissance, motDePasse=mdpHashe, classe=classe)
    with engine.begin() as conn:
        conn.execute(stmt)

    conn.close()


def create_new_clef_admin(clef):
    clefHashee = hashlib.sha256(clef.encode()).hexdigest()
    stmt = insert(table_admin).values(clef=clefHashee)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
    conn.close()


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

def get_all_admins():
    stmt = select(table_admin)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        rows = result.fetchall()
    conn.close()
    return rows