from fastapi import status


def success_res(Status: bool, status_code: status, message: str, data: dict):
    response_dict = {
        "status": Status,
        "status_code": status_code,
        "message": message,
        "data": data,
    }
    return response_dict
