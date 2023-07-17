from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.post('/create_vehicle_type')
async def create_vehicle_type():
    print('create_vehicle_type')

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/get_vehicle_type')
async def create_vehicle_type():
    print('get_vehicle_type')

    return HTTPException(status_code=status.HTTP_200_OK)


@router.post('/update_vehicle_type')
async def create_vehicle_type():
    print('update_vehicle_type')

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/delete_vehicle_type')
async def create_vehicle_type():
    print('delete_vehicle_type')

    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
