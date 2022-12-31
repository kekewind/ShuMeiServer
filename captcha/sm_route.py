from typing import Optional

from fastapi import APIRouter

from captcha.SM import SM

sm_router = APIRouter(prefix='/sm', tags=['数美'])


@sm_router.get("/slide/{organization}", summary="滑块")
def slide(organization: Optional[str]):
    return SM(organization, 'slide').register().verify()


@sm_router.get("/select/{organization}", summary="文字点选")
def select(organization: Optional[str]):
    return SM(organization, 'select').register().verify()


@sm_router.get("/icon_select/{organization}", summary="图标点选")
def icon_select(organization: Optional[str]):
    return SM(organization, 'icon_select').register().verify()


@sm_router.get("/seq_select/{organization}", summary="语序点选")
def seq_select(organization: Optional[str]):
    return SM(organization, 'seq_select').register().verify()


@sm_router.get("/spatial_select/{organization}", summary="空间点选")
def spatial_select(organization: Optional[str]):
    return SM(organization, 'spatial_select').register().verify()
