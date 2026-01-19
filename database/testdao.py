from database.dao import DAO
from model import model
from UI import controller
from UI import view
dao = DAO()
model = model.Model()





print(model.get_album(120))
