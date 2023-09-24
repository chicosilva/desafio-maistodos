from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

from app.internal.config import (PROJECT_CONTACT_API, PROJECT_DESCRIPTION_API,
                                 PROJECT_NAME_API, PROJECT_VERSION_API)
from app.routers import credit_card, healthcheck, user, welcome

__version__ = PROJECT_VERSION_API


def create_app() -> FastAPI:
    app: FastAPI

    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]

    app = FastAPI(
        title=PROJECT_DESCRIPTION_API,
        description=f"MaisTodos - ({PROJECT_NAME_API})",
        version=PROJECT_VERSION_API,
        contact=PROJECT_CONTACT_API,
        middleware=middleware,
    )

    app.include_router(credit_card.router, prefix="/api/v1")

    app.include_router(router=healthcheck.router, tags=["Health"])
    app.include_router(user.router, prefix="/users", tags=["Users"])
    app.include_router(router=welcome)
    return app
