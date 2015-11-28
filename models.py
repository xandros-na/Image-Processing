from flaskapp import db

class Symbol(db.Model):
	__tablename__ = "symbol"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(8), index=True, unique=True)
	v1s = db.relationship('V1', backref='symbol', lazy='dynamic')
	v2s = db.relationship('V2', backref='symbol', lazy='dynamic')
	v3s = db.relationship('V3', backref='symbol', lazy='dynamic')
	v4s = db.relationship('V4', backref='symbol', lazy='dynamic')
	v5s = db.relationship('V5', backref='symbol', lazy='dynamic')
	v6s = db.relationship('V6', backref='symbol', lazy='dynamic')
	v7s = db.relationship('V7', backref='symbol', lazy='dynamic')
	v8s = db.relationship('V8', backref='symbol', lazy='dynamic')
	v9s = db.relationship('V9', backref='symbol', lazy='dynamic')
	v10s = db.relationship('V10', backref='symbol', lazy='dynamic')
	v11s = db.relationship('V11', backref='symbol', lazy='dynamic')
	v12s = db.relationship('V12', backref='symbol', lazy='dynamic')
	v13s = db.relationship('V13', backref='symbol', lazy='dynamic')
	v14s = db.relationship('V14', backref='symbol', lazy='dynamic')
	v15s = db.relationship('V15', backref='symbol', lazy='dynamic')
	V16s = db.relationship('V16', backref='symbol', lazy='dynamic')

class V1(db.Model):
	__tablename__ = "v1"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V2(db.Model):
	__tablename__ = "v2"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))


class V3(db.Model):
	__tablename__ = "v3"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V4(db.Model):
	__tablename__ = "v4"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V5(db.Model):
	__tablename__ = "v5"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V6(db.Model):
	__tablename__ = "v6"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V7(db.Model):
	__tablename__ = "v7"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V8(db.Model):
	__tablename__ = "v8"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V9(db.Model):
	__tablename__ = "v9"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V10(db.Model):
	__tablename__ = "v10"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V11(db.Model):
	__tablename__ = "v11"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V12(db.Model):
	__tablename__ = "v12"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V13(db.Model):
	__tablename__ = "v13"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V14(db.Model):
	__tablename__ = "v14"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V15(db.Model):
	__tablename__ = "v15"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

class V16(db.Model):
	__tablename__ = "v16"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))

