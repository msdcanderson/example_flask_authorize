from ma import ma

from main.models.store import StoreModel


class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StoreModel
        dump_only = ("id",)  # only show ID when dumping
        load_instance = True
