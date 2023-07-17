from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.post('/create_city_name')
async def create_city_name():
    print('create_route')

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/get_city_name')
async def get_city_name():
    print('get_city_name')

    return HTTPException(status_code=status.HTTP_200_OK)


@router.post('/update_city_name')
async def update_city_name():
    print('update_city_name')

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/delete_city_name')
async def delete_city_name():
    print('delete_city_name')

    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
