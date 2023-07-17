from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.post('/create_transport')
async def create_transport():
    print('create_transport')

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/get_transport')
async def get_transport():
    print('get_transport')

    return HTTPException(status_code=status.HTTP_200_OK)


@router.post('/update_transport')
async def update_transport():
    print('update_transport')

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/delete_transport')
async def delete_transport():
    print('delete_transport')

    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
