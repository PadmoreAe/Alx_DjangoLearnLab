from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        import relationship_app.signals

    # REMOVE OR COMMENT OUT THE CODE BELOW
    # def ready(self):
    #     import relationship_app.signals


# from django.apps import AppConfig


# class RelationshipAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'relationship_app'

#     def ready(self):
#         import relationship_app.signals
#         # (Only do this if you moved signals to signals.py,
#         # otherwise keep them at the bottom of models.py)