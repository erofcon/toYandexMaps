from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.post('/create_route')
async def create_route():
    print('create_route')

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/get_route')
async def get_route():
    print('get_route')

    return HTTPException(status_code=status.HTTP_200_OK)


@router.post('/update_route')
async def update_route():
    print('update_route')

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/delete_route')
async def delete_route():
    print('delete_route')

    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
