from connection import db
import datetime
class RegistroModel(db.Model):
    __tablename__ = 'registros'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dth_registro = db.Column(db.Date, nullable=False, default=datetime.now)

    # 0 saida | 1 entrada
    tipo = db.Column(db.Bolean, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    fk_produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)

    produtos = db.relationship('Produto', back_populates='registro')