from ma import ma
from authlogin.models.user import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ("password",)
        dump_only = ("id", "confirmation")  # only show ID when dumping
        load_instance = True
        # include_fk = True

        # @pre_dump
        # def _pre_dump(self, user):
        #     user.confirmation = [user.most_recent_confirmation]
        #     return user
