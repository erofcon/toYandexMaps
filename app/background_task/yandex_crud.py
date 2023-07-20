from loguru import logger
import asyncio
import xml.etree.ElementTree as elTree

import requests

from app.crud import city_name as city_name_crud
from app.crud import transport as transport_crud
from app.crud import nddata as nddata_crud


async def yandex_post_send(city_id: int, clid: str):
    root = elTree.Element('tracks', clid=clid)

    transport_list = await transport_crud.get_transport_data(city_id=city_id)

    if len(transport_list) > 0:
        for i in transport_list:
            location_data = await nddata_crud.get_nddata(i.device_id)

            if location_data is not None:
                track = elTree.SubElement(root, 'track', uuid=str(i.device_id), category=i.category, route=i.route,
                                          vehicle_type=i.vehicle_type)

                elTree.SubElement(track, 'point',
                                  latitude=str(location_data.lat), longitude=str(location_data.lon),
                                  avg_speed=str(location_data.speed), direction=str(location_data.direction),
                                  time=location_data.createddatetime.utcnow().strftime('%d%m%Y:%H%M%S')
                                  )

        data = f"""compressed=0&data={elTree.tostring(root, xml_declaration=True, encoding='utf-8').decode()}"""
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        try:
            r = requests.post(url='http://extjams.maps.yandex.net/mtr_collect/1.x/', data=data, headers=headers)

            logger.info(f'to yandex send with status code {r.status_code}')

        except Exception as e:
            logger.info(e)


async def yandex_crud_task():
    tasks = []
    city_names = await city_name_crud.get_send_city_name()

    if len(city_names) > 0:
        for i in city_names:
            tasks.append(
                asyncio.ensure_future(yandex_post_send(city_id=i.id, clid=i.clid))
            )

        await asyncio.gather(*tasks)
