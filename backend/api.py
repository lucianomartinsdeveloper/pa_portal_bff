from ninja import NinjaAPI

from client.api import router as expense_router

api = NinjaAPI()

api.add_router('/client/', expense_router)
