# models.py

from sqlalchemy import Column, ForeignKey, Boolean, String, Integer, DateTime, func
from sqlalchemy.orm import relationship
from database import Base



class Thesis(Base):
    __tablename__ = 'soutenance'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    numero = Column(String(length=200), unique=True, nullable=False)
    theme = Column(String(length=200), nullable=True)
    lieu_stage = Column(Boolean, default=False, nullable=True)
    responsable = Column(String(length=200), nullable=True)
    cahier_charge = Column(String(length=200), nullable=True)
    is_theme_valide = Column(Boolean, default=False)
    is_binome_valide = Column(Boolean, default=False)
    choix1_id = Column(Integer, ForeignKey('enseignant.id', ondelete='CASCADE'), nullable=True)
    choix2_id = Column(Integer, ForeignKey('enseignant.id', ondelete='CASCADE'), nullable=True)
    maitre_memoire_id = Column(Integer, ForeignKey('enseignant.id', ondelete='CASCADE'), nullable=True)
    annee_id = Column(Integer, ForeignKey('annee.id', ondelete='CASCADE'), nullable=True)
    
    maitre_memoire = relationship('Enseignant', foreign_keys=[maitre_memoire_id], backref='soutenances_maitre_memoire')
    annee =  relationship('Annee', foreign_keys=[annee_id], backref='annee_id')
    choix1 = relationship('Enseignant', foreign_keys=[choix1_id], backref='soutenances_choix1')
    choix2 = relationship('Enseignant', foreign_keys=[choix2_id], backref='soutenances_choix2')
    created = Column(DateTime, server_default=func.now())
    updated = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f'Thesis: {self.numero}'


class Appartenir(Base):
    __tablename__ = 'appartenir'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    etudiant_id = Column(Integer, ForeignKey('etudiant.id', ondelete='CASCADE'))
    soutenance_id = Column(Integer, ForeignKey('soutenance.id', ondelete='CASCADE'))

    etudiant_rel = relationship('users.auth.models.Etudiant', backref='appartenir')
    soutenance_rel = relationship('Thesis', backref='appartenir')

    def __repr__(self) -> str:
        return f'Appartenir: {self.id}'


