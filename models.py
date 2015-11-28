from flaskapp import db

class Symbol(db.Model):
	__tablename__ = "Symbol"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(8), index=True, unique=True)
	v1s = db.relationship('V1', backref='number', lazy='dynamic')
	v2s = db.relationship('V2', backref='number', lazy='dynamic')
	v3s = db.relationship('V3', backref='number', lazy='dynamic')
	v4s = db.relationship('V4', backref='number', lazy='dynamic')
	v5s = db.relationship('V5', backref='number', lazy='dynamic')
	v6s = db.relationship('V6', backref='number', lazy='dynamic')
	v7s = db.relationship('V7', backref='number', lazy='dynamic')
	v8s = db.relationship('V8', backref='number', lazy='dynamic')
	v9s = db.relationship('V9', backref='number', lazy='dynamic')
	v10s = db.relationship('V10', backref='number', lazy='dynamic')
	v11s = db.relationship('V11', backref='number', lazy='dynamic')
	v12s = db.relationship('V12', backref='number', lazy='dynamic')
	v13s = db.relationship('V13', backref='number', lazy='dynamic')
	v14s = db.relationship('V14', backref='number', lazy='dynamic')
	v15s = db.relationship('V15', backref='number', lazy='dynamic')
	V16s = db.relationship('V16', backref='number', lazy='dynamic')

class V1(db.Model):
	__tablename__ = "V1"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V2(db.Model):
	__tablename__ = "V2"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))


class V3(db.Model):
	__tablename__ = "V3"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V4(db.Model):
	__tablename__ = "V4"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V5(db.Model):
	__tablename__ = "V5"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V6(db.Model):
	__tablename__ = "V6"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V7(db.Model):
	__tablename__ = "V7"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V8(db.Model):
	__tablename__ = "V8"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V9(db.Model):
	__tablename__ = "V9"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V10(db.Model):
	__tablename__ = "V10"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V11(db.Model):
	__tablename__ = "V11"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V12(db.Model):
	__tablename__ = "V12"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V13(db.Model):
	__tablename__ = "V13"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V14(db.Model):
	__tablename__ = "V14"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V15(db.Model):
	__tablename__ = "V15"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

class V16(db.Model):
	__tablename__ = "V16"
	id = db.Column(db.Integer, primary_key=True)
	histogram_value = db.Column(db.Float)
	symbol_id = db.Column(db.Integer, db.ForeignKey('Symbol.id'))

