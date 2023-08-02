import edgedb
from fastapi import APIRouter, HTTPException, status

from queries import create_company_async_edgeql as create_company_qry
from queries import get_company_async_edgeql as get_company_qry
from responses_list.success_response import success_res
from schemas.company_schema import Company

router = APIRouter()
client = edgedb.create_async_client()


@router.get("/company_profile")
async def get_company():
    """
    Get company profile.
    """
    company = await get_company_qry.get_company(client)
    return success_res(
        True,
        status.HTTP_200_OK,
        "Success",
        {"company": company},
    )


@router.post("/company_profile", status_code=status.HTTP_201_CREATED)
async def create_company(company: Company):
    """
    Create a new company profile.
    """
    try:
        created_company = await create_company_qry.create_company(
            client,
            name=company.name,
            founded_date=company.founded_date,
            country=company.country,
            website=company.website,
            email=company.email,
            contact_no=company.contact_no,
        )
    except edgedb.errors.ConstraintViolationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": f"Company '{company.name}' already exists."},
        )
    return success_res(
        True,
        status.HTTP_201_CREATED,
        "Company created",
        {
            "company": created_company,
        },
    )
